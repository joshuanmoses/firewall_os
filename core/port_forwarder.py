import json
from core.utils import run_command
from core.logger import setup_logger

logger = setup_logger(__name__)

def load_port_forwarding():
    with open('config/port_forwarding.json') as f:
        forwarding = json.load(f)
    return forwarding

def apply_port_forwarding():
    forwarding_rules = load_port_forwarding()
    for fwd in forwarding_rules:
        cmd = f"iptables -t nat -A PREROUTING -p {fwd['protocol']} --dport {fwd['external_port']} -j DNAT --to-destination {fwd['internal_ip']}:{fwd['internal_port']}"
        stdout, stderr, code = run_command(cmd)
        if code == 0:
            logger.info(f"Applied port forwarding: {cmd}")
        else:
            logger.error(f"Failed port forwarding: {stderr}")
