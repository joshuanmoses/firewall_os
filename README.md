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

<h3>1. Prepare the Root Filesystem</h3>
<p>Build your minimal Linux filesystem inside a folder called <code>rootfs/</code>. This should include:</p>
<ul>
  <li>Kernel (<code>vmlinuz</code>) and initial ramdisk (<code>initrd.img</code>)</li>
  <li>Python runtime and necessary libraries (Flask, etc.)</li>
  <li>iptables, vlan tools, Suricata or Snort</li>
  <li>All Python management scripts (firewall, VLAN, IDS managers)</li>
</ul>

<h3>2. Install SquashFS Tools</h3>

<pre><code>sudo apt update
sudo apt install squashfs-tools
</code></pre>

<h3>3. Create filesystem.squashfs</h3>

<p>Use <strong>mksquashfs</strong> to compress your <code>rootfs/</code> into a SquashFS image:</p>

<pre><code>
sudo mksquashfs rootfs/ filesystem.squashfs -comp xz -e boot
</code></pre>

<ul>
  <li><strong>rootfs/</strong>: the folder containing your Linux filesystem.</li>
  <li><strong>filesystem.squashfs</strong>: the compressed filesystem image needed for live boot.</li>
  <li><strong>-comp xz</strong>: use xz compression for smaller image size.</li>
  <li><strong>-e boot</strong>: exclude the boot directory (it must stay separate).</li>
</ul>

<h3>4. Assemble ISO Directory Structure</h3>

<p>Create a directory called <code>iso/</code> and copy the necessary components:</p>

<pre><code>
mkdir -p iso/boot/grub
cp boot/grub.cfg iso/boot/grub/grub.cfg
cp boot/vmlinuz iso/boot/vmlinuz
cp boot/initrd.img iso/boot/initrd.img
cp filesystem.squashfs iso/
</code></pre>

<h3>5. Build the ISO Image</h3>

<p>Use GRUB to create the bootable ISO:</p>

<pre><code>
grub-mkrescue -o firewall_os.iso iso/
</code></pre>

<p>The output <code>firewall_os.iso</code> is now ready to be burned to a USB drive or run in a virtual machine.</p>

<hr>

<h2>📡 Running the Web Interface</h2>

<p>Once the system boots, you can start the Flask Web Interface:</p>

<pre><code>python3 web/app.py</code></pre>

<p>Access it via your browser at:</p>

<pre><code>http://localhost:5000</code></pre>

<h3>Web Interface Features:</h3>
<ul>
  <li>View, add, and delete firewall rules</li>
  <li>View, add, and delete VLAN configurations</li>
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
  <li>Display IDS alerts in the web dashboard</li>
  <li>VPN server integration (WireGuard, OpenVPN)</li>
  <li>HA (High Availability) support with node clustering</li>
  <li>Cloud-based centralized logging support</li>
</ul>

<hr>

<h2>🏆 Skills Demonstrated</h2>

<ul>
  <li>Linux Live OS Customization and Building</li>
  <li>Secure Network Architecture and Firewall Management</li>
  <li>Python System Service Development</li>
  <li>Web Development with Flask and Jinja2</li>
  <li>Filesystem Compression and SquashFS Management</li>
  <li>GRUB Bootloader Configuration for Live Systems</li>
</ul>

<hr>


<h2>👨‍💻 Author</h2>

<ul>
  <li><a href="https://github.com/joshuanmoses">Joshua Moses</a> — AI & Threat Expert</li>
</ul>

</body>
</html>
