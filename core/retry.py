import time
from typing import Callable
from core.logger import get_logger

logger = get_logger("Retry")

def retry(func, retries=3, delay=0.1):
    for attempt in range(1,retries+1):
        try:
            return func()
        except Exception as e:
            logger.error(f"Attempt {attempt} failed: {e}")
            if attempt == retries:
                raise
            else:
                time.sleep(delay)