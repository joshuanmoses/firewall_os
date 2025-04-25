<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

<h1>🔥 Firewall OS - Live Linux Firewall and IDS Platform</h1>

<blockquote>
  <em>A lightweight, live-boot Linux operating system that transforms any machine into a powerful firewall, VLAN router, and intrusion detection system with a web-based management interface.</em>
</blockquote>

<hr>

<h2>🚀 Project Overview</h2>

<p>Firewall OS is a custom live Linux distribution built for cybersecurity professionals, penetration testers, and network engineers. It provides a fully scriptable, Python-driven firewall and intrusion detection platform. The system supports:</p>

<ul>
  <li>Stateful packet filtering (iptables/nftables)</li>
  <li>Dynamic port forwarding management</li>
  <li>Advanced VLAN setup and tagging</li>
  <li>Intrusion Detection System (IDS) using Suricata or Snort</li>
  <li>Web-based control panel (Flask-powered) for firewall and VLAN management</li>
</ul>

<p>The project aims to make secure network segmentation and monitoring simple, portable, and rapidly deployable in tactical environments.</p>

<hr>

<h2>🛡️ Key Features</h2>

<ul>
  <li>Python-based management of firewall rules and VLANs</li>
  <li>Dynamic IDS activation and monitoring</li>
  <li>Live Linux boot (runs entirely from RAM)</li>
  <li>Web UI to view, add, and remove firewall and VLAN configurations</li>
  <li>ISO builder script to create your own live ISO images</li>
  <li>Support for both BIOS and UEFI boot modes</li>
  <li>Extensible modular architecture (easy to add features)</li>
</ul>

<hr>

<h2>⚙️ System Architecture</h2>

<ul>
  <li><strong>Python Services:</strong> Firewall manager, VLAN manager, IDS service</li>
  <li><strong>Web Interface:</strong> Flask application exposing Firewall and VLAN controls</li>
  <li><strong>Persistence:</strong> Configuration files stored as editable JSON documents</li>
  <li><strong>Bootloader:</strong> GRUB2 with live-boot options (standard and safe mode)</li>
  <li><strong>Core Packages:</strong> iptables, nftables, vlan tools, Suricata IDS, Snort IDS</li>
</ul>

<hr>

<h2>📂 Project Folder Structure</h2>

<pre><code>
firewall_os/
├── boot/                  # GRUB bootloader configuration
├── config/                # Firewall, VLAN, IDS settings in JSON
├── core/                  # Firewall, VLAN, IDS managers
├── services/              # Background daemons for management
├── web/                   # Flask web interface
├── live_build/            # Scripts and output for ISO building
├── setup.sh               # Installer and dependency script
├── app.py                 # Main application entrypoint
├── README.html            # Project documentation
</code></pre>

<hr>

<h2>🛠 Building the Live ISO</h2>

<ol>
  <li>Prepare your root filesystem under <code>rootfs/</code> (kernel, initrd, Python, system binaries).</li>
  <li>Install squashfs-tools:</li>
  <pre><code>sudo apt install squashfs-tools</code></pre>
  <li>Create the compressed filesystem:</li>
  <pre><code>sudo mksquashfs rootfs/ filesystem.squashfs -comp xz -e boot</code></pre>
  <li>Copy boot files (vmlinuz, initrd.img) and GRUB config to <code>iso/</code>.</li>
  <li>Build the ISO:</li>
  <pre><code>grub-mkrescue -o firewall_os.iso iso/</code></pre>
</ol>

<hr>

<h2>📡 Running the Web Interface</h2>

<p>Boot into Firewall OS, then start the Flask web interface:</p>

<pre><code>python3 web/app.py</code></pre>

<p>Access it via your browser at:</p>

<pre><code>http://localhost:5000</code></pre>

<h3>Web Interface Features:</h3>
<ul>
  <li>View and manage firewall rules</li>
  <li>Add and delete iptables rules</li>
  <li>View and manage VLANs</li>
  <li>Create and remove VLAN interfaces dynamically</li>
</ul>

<hr>

<h2>🧪 Example Firewall Rule (JSON)</h2>

<pre><code>[
  "-A INPUT -p tcp --dport 22 -j ACCEPT",
  "-A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT",
  "-A INPUT -j DROP"
]</code></pre>

<h2>🧪 Example VLAN (JSON)</h2>

<pre><code>[
  {
    "parent": "eth0",
    "name": "eth0.10",
    "id": 10
  }
]</code></pre>

<hr>

<h2>📈 Future Roadmap</h2>

<ul>
  <li>Add basic authentication to web interface (Flask-Login)</li>
  <li>Add real-time IDS alert viewing through the web interface</li>
  <li>Implement VPN server integration (WireGuard, OpenVPN)</li>
  <li>Centralized logging dashboard (Elastic Stack or lightweight viewer)</li>
  <li>Support for High Availability (HA) setups with active/passive nodes</li>
</ul>

<hr>

<h2>🏆 Skills Demonstrated</h2>

<ul>
  <li>Custom Live Linux OS Development</li>
  <li>Firewall and IDS Configuration Automation</li>
  <li>Python Service Daemon Architecture</li>
  <li>SquashFS and Live ISO Building</li>
  <li>GRUB Bootloader Customization</li>
  <li>Flask Web Development for Infrastructure Management</li>
  <li>Network Security Engineering (VLAN, IDS, Firewall)</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<ul>
  <li><a href="https://github.com/joshuanmoses">Joshua Moses</a> — AI & Threat Expert</li>
</ul>

</body>
</html>
