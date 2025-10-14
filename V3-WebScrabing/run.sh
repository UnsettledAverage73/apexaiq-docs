#!/bin/bash

# DBF Scraper Automation Runner
# Simple script to run the automation with proper virtual environment

cd "$(dirname "$0")"

echo "DBF Scraper Automation"
echo "====================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Please run ./setup.sh first."
    exit 1
fi

# Run the automation
echo "Starting automation..."
echo ""

./venv/bin/python main.py "$@"

echo ""
echo "Automation completed. Check dbf_automation.log for details."
