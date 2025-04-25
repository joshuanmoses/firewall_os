from flask import Blueprint, render_template, request, redirect, url_for
import json
from core.vlan_manager import setup_vlans

vlan_bp = Blueprint('vlan', __name__)

@vlan_bp.route('/', methods=["GET", "POST"])
def vlan():
    if request.method == "POST":
        parent = request.form.get('parent')
        name = request.form.get('name')
        vid = request.form.get('vid')
        
        if parent and name and vid:
            with open('config/vlans.json', 'r+') as f:
                vlans = json.load(f)
                vlans.append({
                    "parent": parent,
                    "name": name,
                    "id": int(vid)
                })
                f.seek(0)
                json.dump(vlans, f, indent=4)
            setup_vlans()
        return redirect(url_for('vlan.vlan'))
    
    with open('config/vlans.json') as f:
        vlans = json.load(f)
    
    return render_template('vlans.html', vlans=vlans)

@vlan_bp.route('/delete/<int:index>')
def delete_vlan(index):
    with open('config/vlans.json', 'r+') as f:
        vlans = json.load(f)
        if 0 <= index < len(vlans):
            vlans.pop(index)
            f.seek(0)
            f.truncate()
            json.dump(vlans, f, indent=4)
    setup_vlans()
    return redirect(url_for('vlan.vlan'))
