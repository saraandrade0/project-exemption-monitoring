import schedule
import time
import subprocess
from datetime import datetime

def run_validation():
    """Run the validation script and log the result with timestamp."""
    print(f"Running validation at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        # Call your validation script
        subprocess.run(["python", "validate_exemption_rule.py"], check=True)
        print("Validation completed successfully\n")
    except subprocess.CalledProcessError as e:
        print(f"Validation failed: {e}\n")

# Schedule the job every day at 08:00
schedule.every().day.at("08:00").do(run_validation)

print(" Daily validation job scheduled for 08:00.")
print("Press Ctrl+C to stop.\n")

# Keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(30)  # check every 30 seconds