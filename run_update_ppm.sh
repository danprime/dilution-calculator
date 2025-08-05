#!/bin/bash
echo "Starting script" > /tmp/debug.log
which python3 >> /tmp/debug.log
python3 --version >> /tmp/debug.log
cd /Users/danielt/workspace/dilution-calculator
python3 /Users/danielt/workspace/dilution-calculator/update_ppm_from_quality.py >> /tmp/debug.log 2>&1
echo "Script finished with exit code $?" >> /tmp/debug.log
exit 0
