#!/bin/bash

echo "Downloading Chromium"
mkdir -p "/opt/chrome/stable"
curl -Lo "/opt/chrome/stable/chrome-linux.zip" \
    "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F954502%2Fchrome-linux.zip?generation=1640815524872726&alt=media"
unzip -q "/opt/chrome/stable/chrome-linux.zip" -d "/opt/chrome/stable/"
ls -al /opt/chrome/stable/chrome-linux
mv /opt/chrome/stable/chrome-linux/* /opt/chrome/stable/
rm -rf /opt/chrome/stable/chrome-linux /opt/chrome/stable/chrome-linux.zip