#!/bin/bash

# Check if virtualenv is installed, install if missing
#if ! command -v virtualenv &> /dev/null; then
#    echo "virtualenv not found, installing..."
#    pip3 install virtualenv
#fi


# Step 1: Create a virtual environment
python3 -m venv venv

# Step 2: Activate the virtual environment
source venv/bin/activate

echo "Virtual environment created and activated."

# Step 3: Upgrade pip (optional but recommended)
pip install --upgrade pip

# Step 4: Install dependencies
pip install -r requirements.txt

echo "Dependencies installed successfully."

echo "Run 'source venv/bin/activate' to activate the environment."
