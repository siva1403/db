import os
import time
from datetime import datetime


#print(timestamp)
timestamp = datetime.now().strftime("%H:%M:%S %d %b %Y")

import subprocess

def run_script():
    subprocess.run(["bash", "db.sh"], check=True)

def build_app():
    print(timestamp)

def main():
    print("Pipeline Started")
    build_app()
    run_script()
    build_app()
    print("Pipeline Completed")

if __name__ == "__main__":
    main()
