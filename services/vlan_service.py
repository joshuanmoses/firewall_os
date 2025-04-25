import time
from core.vlan_manager import setup_vlans
from core.logger import setup_logger

logger = setup_logger(__name__)

def run():
    while True:
        setup_vlans()
        time.sleep(300)
