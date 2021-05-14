import logging
import os
import subprocess
import time
import signal

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
    process = subprocess.Popen(["./script.sh"], preexec_fn=os.setpgrp)
    logging.info(f"PID of subprocess created using subprocess: {process.pid}")


def handler(signum, frame):
    import sys

    logging.info("\nSignal received")
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)  # works
    sys.exit(0)


# Set signal handler so CTRL+C also ends the subprocess
# signal.signal(signal.SIGINT, handler)

queue()

# Terminate subprocess after some time
time.sleep(3)
logging.info("Terminating subprocess")
# process.terminate() # does not work

# Send the signal to the process group
os.killpg(os.getpgid(process.pid), signal.SIGTERM)  # works

logging.info(f"Terminated subprocess")

time.sleep(8)  # Simulated delay
logging.info("Program stopped")
