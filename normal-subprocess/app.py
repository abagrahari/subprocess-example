import logging
import os
import subprocess
import time

logging.basicConfig(
    format="%(filename)s: \t %(asctime)s; %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)

logging.info(f"PID of `app.py` Process: {os.getpid()}")
process: subprocess.Popen = None


def queue():
    """Execute long-running task using a subprocess."""
    global process
    process = subprocess.Popen(["./script.sh"], start_new_session=True)
    logging.info(f"PID of subprocess created using subprocess: {process.pid}")


queue()

# Terminate subprocess after some time
time.sleep(3)
logging.info("Terminating subprocess")
process.kill()
logging.info(f"Terminated subprocess")

time.sleep(10)  # Simulated delay
logging.info("Program stopped")
