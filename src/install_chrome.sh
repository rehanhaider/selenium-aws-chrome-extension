#!/bin/bash

apt-get update && apt-get upgrade -y

echo "Download the latest Chrome .deb file..."
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -q

echo "Install Google Chrome..."
dpkg -i google-chrome-stable_current_amd64.deb

echo "Fix dependencies..."
apt-get --fix-broken install -y
