import subprocess
import os
import sys

# Call get_water_quality_value.py and capture its output
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    child_script = os.path.join(script_dir, 'get_water_quality_value.py')
    result = subprocess.run([
        sys.executable, child_script
    ], capture_output=True, text=True, check=True)
    ppm_value = result.stdout.strip()
except Exception as e:
    print(f"Error running get_water_quality_value.py: {e}")
    sys.exit(1)

# Call update_ppm.py with the value
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    child_script = os.path.join(script_dir, 'update_ppm.py')
    subprocess.run([
        sys.executable, child_script, ppm_value
    ], check=True)
    print(f"Updated LATEST_PPM to {ppm_value} using update_ppm.py")
except Exception as e:
    print(f"Error running update_ppm.py: {e}")
    sys.exit(1)

# Commit and push the change using git
try:
    subprocess.run(['git', 'add', 'ppm-constant.js'], check=True)
    subprocess.run(['git', 'commit', '-m', f'Update LATEST_PPM to {ppm_value}'], check=True)
    subprocess.run(['git', 'push'], check=True)
    print("Committed and pushed ppm-constant.js to git repository.")
except Exception as e:
    print(f"Error running git commands: {e}")
    sys.exit(1)
