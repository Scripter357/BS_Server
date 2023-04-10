#!/bin/bash
echo "Installing postgresql..."
sudo apt update && sudo apt install postgresql postgresql-contrib && systemctl enable --now postgresql
echo "Installing python..."
sudo apt install python3 python3-venv python3-pip
echo "Installing uvicorn..."
pip install uvicorn
echo "Creating virtual environment..."
python3 -m venv ./venv
sudo apt install python3-venv
echo "Activating virtual environment..."
source ./venv/bin/activate
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Setting up the database..."
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres'"
sudo -u postgres psql -c "CREATE database server_db"
python3 db_setup.py
