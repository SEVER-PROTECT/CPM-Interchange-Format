#!/bin/bash

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Setting up..."
    python3 -m venv venv
    echo "Virtual environment created."

    # Activate virtual environment
    source venv/bin/activate
    echo "Virtual environment activated."

    # Upgrade pip
    pip install --upgrade pip

    # Install dependencies
    pip install -r requirements.txt
    echo "Dependencies installed successfully."
else
    # Activate virtual environment
    source venv/bin/activate
    echo "Virtual environment activated."
fi

# Run the provided command inside the virtual environment
if [ "$#" -eq 0 ]; then
    echo "No command provided. Use ./setup_virtualenv.sh <command> to run inside the environment."
    exit 1
fi

python "$@"
