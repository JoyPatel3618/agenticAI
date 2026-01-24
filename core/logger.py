import logging
import sys

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        layout = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
        formatter = logging.Formatter(layout)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger