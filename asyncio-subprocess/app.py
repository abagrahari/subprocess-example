import asyncio
import logging
import os
import time
import signal

logging.basicConfig(
    format="%(filename)s: \t %(asctime)s; %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)

logging.info(f"PID of `app.py` Process: {os.getpid()}")
process: asyncio.subprocess.Process = None


async def queue():
    """Execute long-running task using a subprocess."""
    global process
    process = await asyncio.create_subprocess_exec("script.sh", preexec_fn=os.setpgrp)
    logging.info(f"PID of subprocess created using asyncio: {process.pid}")


asyncio.get_event_loop().run_until_complete(queue())

# Terminate subprocess after some time
time.sleep(3)
logging.info("Terminating subprocess")
# process.terminate() # does not work

# Send the signal to the process group
os.killpg(os.getpgid(process.pid), signal.SIGTERM)  # works

logging.info(f"Terminated subprocess")

time.sleep(8)  # Simulated delay
logging.info("Program stopped")
