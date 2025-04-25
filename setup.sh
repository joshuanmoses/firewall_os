#!/bin/bash

echo "Setting up Firewall OS..."

apt update
apt install -y iptables nftables vlan suricata snort python3-pip
pip3 install flask

echo "Enabling IP Forwarding..."
sysctl -w net.ipv4.ip_forward=1

echo "Setup Complete."
