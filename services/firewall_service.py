import time
from core.firewall_manager import apply_firewall_rules
from core.logger import setup_logger

logger = setup_logger(__name__)

def run():
    while True:
        apply_firewall_rules()
        time.sleep(60)  # Reload every 60 seconds

