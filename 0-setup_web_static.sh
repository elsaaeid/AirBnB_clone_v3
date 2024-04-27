#!/usr/bin/env bash
# A bash script that sets up your web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install -y nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
<head>
</head>
<body>
    Holberton School
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate the symbolic link
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership of the /data/ folder to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
sudo sed -i '/^\s*location \/hbnb_static {/a \        alias /data/web_static/current/;' "$config_file"

# Restart Nginx
sudo service nginx restart
