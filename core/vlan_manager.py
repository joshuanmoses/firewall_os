import json
from core.utils import run_command
from core.logger import setup_logger

logger = setup_logger(__name__)

def load_vlans():
    with open('config/vlans.json') as f:
        vlans = json.load(f)
    return vlans

def setup_vlans():
    vlans = load_vlans()
    for vlan in vlans:
        cmd = f"ip link add link {vlan['parent']} name {vlan['name']} type vlan id {vlan['id']}"
        run_command(cmd)
        cmd_up = f"ip link set dev {vlan['name']} up"
        run_command(cmd_up)
        logger.info(f"Created VLAN {vlan['name']} on {vlan['parent']}")
