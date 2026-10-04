#!/bin/bash
# ============================================
# MJ :: Development Environment Setup Script
# ============================================

# Update system
sudo apt update && sudo apt upgrade -y

# Install essential packages
sudo apt install -y git curl wget vim build-essential python3 python3-pip nodejs npm

# Install Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb

# Install Tor Browser
sudo apt install -y torbrowser-launcher

# Set Bing as default search engine (for Chrome)
CHROME_PREFS="$HOME/.config/google-chrome/Default/Preferences"
if [ -f "$CHROME_PREFS" ]; then
  sed -i 's/"default_search_provider_data":{[^}]*}/"default_search_provider_data":{"template_url":"https:\/\/bing.com\/search?q={searchTerms}","name":"Bing","keyword":"bing"}/' "$CHROME_PREFS"
fi

# Create Desktop directories
DESKTOP="$HOME/Desktop"
mkdir -p "$DESKTOP/ali-baba"
mkdir -p "$DESKTOP/.mj"

# Backup current Desktop data into ali-baba
cp -r $DESKTOP/* "$DESKTOP/ali-baba/" 2>/dev/null

# Create audit log inside .mj
AUDIT_FILE="$DESKTOP/.mj/setup_audit.log"
echo "======================================" >> $AUDIT_FILE
echo " MJ :: Development Setup Audit Log" >> $AUDIT_FILE
echo " Timestamp: $(date '+%Y-%m-%d %H:%M:%S')" >> $AUDIT_FILE
echo " Installed: Git, Python3, Node.js, npm, Chrome, Tor Browser" >> $AUDIT_FILE
echo " Default Search Engine: Bing" >> $AUDIT_FILE
echo " Backup Directory: ali-baba" >> $AUDIT_FILE
echo " Audit Directory: .mj" >> $AUDIT_FILE
echo "======================================" >> $AUDIT_FILE

echo "✅ Setup Complete! Restart Chrome to apply Bing search engine."
