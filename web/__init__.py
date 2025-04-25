from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from web.firewall_routes import firewall_bp
    from web.vlan_routes import vlan_bp

    app.register_blueprint(firewall_bp, url_prefix='/firewall')
    app.register_blueprint(vlan_bp, url_prefix='/vlan')
    
    @app.route('/')
    def index():
        return "<h1>Welcome to Firewall OS Control Panel</h1><p><a href='/firewall'>Manage Firewall</a> | <a href='/vlan'>Manage VLANs</a></p>"
    
    return app
