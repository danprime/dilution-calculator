import subprocess
import sys

# Call get_water_quality_value.py and capture its output
try:
    result = subprocess.run([
        sys.executable, 'get_water_quality_value.py'
    ], capture_output=True, text=True, check=True)
    ppm_value = result.stdout.strip()
except Exception as e:
    print(f"Error running get_water_quality_value.py: {e}")
    sys.exit(1)

# Call update_ppm.py with the value
try:
    subprocess.run([
        sys.executable, 'update_ppm.py', ppm_value
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
