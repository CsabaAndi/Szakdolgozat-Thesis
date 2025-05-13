#!/bin/bash

set -e  # Exit immediately on error

# Step 1: Create virtual environment
echo "📦 Creating Python virtual environment..."
python3.12 -m venv .venvs/env

# Step 2: Activate the virtual environment
echo "🔗 Activating virtual environment..."
source .venvs/env/bin/activate

# Step 3: Install Python requirements
echo "⬇️ Installing Python dependencies..."
pip install -r pie-requirements.txt
