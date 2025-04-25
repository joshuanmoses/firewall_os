#!/bin/bash

echo "Building the Live Linux Firewall ISO..."

# Clean previous build
rm -f filesystem.squashfs

# Create new SquashFS filesystem
mksquashfs rootfs/ filesystem.squashfs -comp xz -e boot

echo "SquashFS filesystem created successfully!"

# Optionally: Create ISO image (assuming bootloader already set up)
mkdir -p iso/boot/grub
cp boot/grub.cfg iso/boot/grub/grub.cfg
cp filesystem.squashfs iso/
cp -r boot/vmlinuz boot/initrd.img iso/boot/

grub-mkrescue -o firewall_os.iso iso/

echo "ISO build complete: firewall_os.iso"
