from flask import Blueprint, render_template, request, redirect, url_for
import json
from core.firewall_manager import apply_firewall_rules

firewall_bp = Blueprint('firewall', __name__)

@firewall_bp.route('/', methods=["GET", "POST"])
def firewall():
    if request.method == "POST":
        rule = request.form.get('rule')
        if rule:
            with open('config/firewall_rules.json', 'r+') as f:
                rules = json.load(f)
                rules.append(rule)
                f.seek(0)
                json.dump(rules, f, indent=4)
            apply_firewall_rules()
        return redirect(url_for('firewall.firewall'))
    
    with open('config/firewall_rules.json') as f:
        rules = json.load(f)
    
    return render_template('firewall.html', rules=rules)

@firewall_bp.route('/delete/<int:index>')
def delete_rule(index):
    with open('config/firewall_rules.json', 'r+') as f:
        rules = json.load(f)
        if 0 <= index < len(rules):
            rules.pop(index)
            f.seek(0)
            f.truncate()
            json.dump(rules, f, indent=4)
    apply_firewall_rules()
    return redirect(url_for('firewall.firewall'))
