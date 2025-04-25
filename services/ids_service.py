import time
from core.intrusion_detector import start_ids
from core.logger import setup_logger

logger = setup_logger(__name__)

def run():
    start_ids()
    while True:
        time.sleep(600)  # Let IDS handle alerts separately
