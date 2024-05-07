# #!/usr/bin/env bash

# sudo apt install -y python3-pip
# sudo apt install -y nginx
# sudo apt install -y virtualenv
# sudo apt-get install libpq-dev
# pip3 install psycopg2
# pip3 install psycopg2-binary
#!/usr/bin/env bash

# # Install system-level dependencies
# sudo apt install -y python3-pip
# sudo apt install -y nginx
# sudo apt install -y virtualenv
# sudo apt-get install libpq-dev
# sudo chown -R ubuntu:ubuntu /home/ubuntu/django-cicd

# # Navigate to your project directory
# cd /home/ubuntu/django-cicd
# sudo apt install python3-venv
# # Create a virtual environment
# python3 -m venv venv

# # Activate the virtual environment
# source venv/bin/activate

# # Install Python dependencies
# pip install -r requirements.txt  # Assuming you have a requirements.txt file
#!/bin/bash

# Install system-level dependencies
sudo apt update
sudo apt install -y python3-pip nginx virtualenv libpq-dev

# Navigate to your project directory
cd /home/ubuntu/django-cicd

# Install Python3 venv if not installed already
sudo apt install -y python3-venv

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt  # Assuming you have a requirements.txt file

# Set permissions for the project directory (optional)
sudo chown -R ubuntu:ubuntu /home/ubuntu/django-cicd
