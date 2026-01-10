#!/bin/bash
# Simple script to start a local web server for the Iceland POI app

echo "Generating manifest.json..."
python3 generate_manifest.py

echo ""
echo "Starting local web server..."
echo "Open your browser and go to: http://localhost:8000"
echo "Press Ctrl+C to stop the server"
echo ""

cd "$(dirname "$0")"
python3 -m http.server 8000

