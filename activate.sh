#!/bin/bash
# Simple script to activate the virtual environment and run the Flask app

echo "Activating virtual environment..."
source venv/bin/activate

echo "Virtual environment activated!"
echo "Python interpreter: $(which python)"
echo "Flask version: $(python -c "import flask; print(flask.__version__)")"

echo ""
echo "To run the Flask app, use: python app.py"
echo "To deactivate, use: deactivate"
