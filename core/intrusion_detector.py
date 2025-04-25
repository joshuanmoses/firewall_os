import json
import os
from core.logger import setup_logger

logger = setup_logger(__name__)

def load_ids_settings():
    with open('config/ids_settings.json') as f:
        return json.load(f)

def start_ids():
    settings = load_ids_settings()
    if settings['engine'] == "suricata":
        os.system("systemctl start suricata")
        logger.info("Suricata IDS started")
    elif settings['engine'] == "snort":
        os.system("systemctl start snort")
        logger.info("Snort IDS started")
