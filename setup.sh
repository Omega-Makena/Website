#!/bin/bash

echo "===================================="
echo "Omega Makena Website Setup"
echo "===================================="
echo

echo "Creating virtual environment..."
python3 -m venv venv
echo

echo "Activating virtual environment..."
source venv/bin/activate
echo

echo "Installing dependencies..."
pip install -r requirements.txt
echo

echo "===================================="
echo "Setup complete!"
echo "===================================="
echo
echo "To run the development server:"
echo "  1. Run: source venv/bin/activate"
echo "  2. Run: python app.py"
echo "  3. Visit: http://localhost:5000"
echo
echo "To generate static site for deployment:"
echo "  Run: python freeze.py"
echo



