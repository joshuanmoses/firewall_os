import json
from core.utils import run_command
from core.logger import setup_logger

logger = setup_logger(__name__)

def load_firewall_rules():
    with open('config/firewall_rules.json') as f:
        rules = json.load(f)
    return rules

def apply_firewall_rules():
    rules = load_firewall_rules()
    for rule in rules:
        cmd = f"iptables {rule}"
        stdout, stderr, code = run_command(cmd)
        if code == 0:
            logger.info(f"Applied rule: {cmd}")
        else:
            logger.error(f"Failed to apply rule: {stderr}")
