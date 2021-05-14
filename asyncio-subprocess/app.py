import asyncio
import logging
import os
import time

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
    process = await asyncio.create_subprocess_exec("script.sh")
    logging.info(f"PID of subprocess created using asyncio: {process.pid}")


asyncio.get_event_loop().run_until_complete(queue())

# Terminate subprocess after some time
time.sleep(3)
logging.info("Terminating subprocess")
process.terminate()
logging.info(f"Terminated subprocess")

time.sleep(10)  # Simulated delay
logging.info("Program stopped")
