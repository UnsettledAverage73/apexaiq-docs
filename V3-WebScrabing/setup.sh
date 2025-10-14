#!/bin/bash

# DBF Scraper Automation Setup Script

echo "Setting up DBF Scraper Automation..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Install Python dependencies
echo "Installing Python dependencies..."
./venv/bin/pip install -r requirements.txt

# Check if Chrome/Chromium is installed
echo "Checking for Chrome/Chromium browser..."
if ! command -v google-chrome &> /dev/null && ! command -v chromium-browser &> /dev/null && ! command -v chromium &> /dev/null; then
    echo "Chrome/Chromium browser is not installed."
    echo "Please install Google Chrome or Chromium browser."
    echo "On Ubuntu/Debian: sudo apt install chromium-browser"
    echo "On macOS: brew install --cask google-chrome"
    echo "On Arch Linux: sudo pacman -S chromium"
    exit 1
fi

# Create logs directory
mkdir -p logs

echo "Setup completed successfully!"
echo ""
echo "To run the automation:"
echo "  ./venv/bin/python main.py"
echo ""
echo "To test components:"
echo "  ./venv/bin/python main.py --test"
echo ""
echo "To run with visible browser:"
echo "  ./venv/bin/python main.py --headless=false"
echo ""
