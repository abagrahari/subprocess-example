import asyncio
import logging
import os

logging.basicConfig(
    format="%(filename)s: %(asctime)s; %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)


async def long_running_func() -> None:

    logging.info(f"PID of long-running Process:{os.getpid()}")
    await asyncio.sleep(10)  # Simulate long-running function
    logging.info(
        f"Long-running process {os.getpid()} finished before being terminated. Was not terminated by parent!"
    )


asyncio.get_event_loop().run_until_complete(long_running_func())
