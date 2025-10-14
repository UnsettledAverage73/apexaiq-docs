#!/bin/bash

# Simple script to run the backend API

cd "$(dirname "$0")"

echo "Starting DBF Scraper Backend API"
echo "==============================="

# Run the FastAPI application using Uvicorn
python3 -m uvicorn app:app --host 0.0.0.0 --port 8000 "$@"

echo ""
echo "Backend API stopped."
