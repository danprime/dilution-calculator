#!/usr/bin/env python3

import warnings
warnings.filterwarnings("ignore")  # Hides all warnings

import sys
import requests
from bs4 import BeautifulSoup

def get_last_cell_second_row(url="https://apps.epcor.ca/DailyWaterQuality/Default.aspx?zone=ELS") -> str:
    try:
#        print(f"Fetching URL: {url}", file=sys.stderr)
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        table_rows = soup.find_all('tr')
#        print(f"Found {len(table_rows)} <tr> elements", file=sys.stderr)

        if len(table_rows) < 2:
            raise ValueError("Table does not have at least two rows.")

        second_row = table_rows[2]
#        print("Second row HTML:", file=sys.stderr)
#        print(second_row.prettify(), file=sys.stderr)

        cells = second_row.find_all(['td', 'th'])
#        print(f"Second row has {len(cells)} cells", file=sys.stderr)

#        for i, cell in enumerate(cells):
#            print(f"  Cell {i}: '{cell.get_text(strip=True)}'", file=sys.stderr)

        if not cells:
            raise ValueError("Second row has no cells.")

        last_cell = cells[-1].get_text(strip=True)
#        print(f"Extracted value from last cell: '{last_cell}'", file=sys.stderr)

        return last_cell

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    value = get_last_cell_second_row()
    print(value)

if __name__ == "__main__":
    main()

