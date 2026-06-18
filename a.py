import os
import time


timestamp = int(time.time())

print(timestamp)

import subprocess

def run_script():
    subprocess.run(["bash", "db.sh"], check=True)

def main():
    print("Pipeline Started")
    run_script()
    print("Pipeline Completed")

if __name__ == "__main__":
    main()
