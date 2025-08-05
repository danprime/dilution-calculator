import sys
import re

if len(sys.argv) != 2:
    print("Usage: python update_ppm.py <new_ppm_value>")
    sys.exit(1)

new_ppm = sys.argv[1]

try:
    float(new_ppm)
except ValueError:
    print("PPM value must be a number.")
    sys.exit(1)

js_file = "ppm-constant.js"
pattern = re.compile(r"(const LATEST_PPM\s*=\s*)[\d.]+(;)")

with open(js_file, "r") as f:
    content = f.read()

new_content, count = pattern.subn(r"\g<1>{}\2".format(new_ppm), content)

if count == 0:
    print("Could not find LATEST_PPM constant in ppm-constant.js")
    sys.exit(1)

with open(js_file, "w") as f:
    f.write(new_content)

print(f"Updated LATEST_PPM to {new_ppm} in {js_file}")

