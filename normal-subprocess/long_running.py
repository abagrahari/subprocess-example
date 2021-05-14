import logging
import os
import time

logging.basicConfig(
    format="%(filename)s: %(asctime)s; %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)


def long_running_func() -> None:
    logging.info(f"PID of long-running Process:{os.getpid()}")
    time.sleep(7)  # Simulate long-running function
    logging.info(
        f"Long-running process {os.getpid()} finished before being terminated. Was not terminated by parent!"
    )


long_running_func()
