#!/bin/bash

set -e  # Exit on error

VENV_PATH=".venvs/env"
NODE_MODULES_PATH="Code/webscrape-app/node_modules"

# Delete Python virtual environment if it exists
if [ -d "$VENV_PATH" ]; then
  echo "🗑 Removing virtual environment at $VENV_PATH"
  rm -rf "$VENV_PATH"
else
  echo "ℹ️ No virtual environment found at $VENV_PATH"
fi

# Delete node_modules if it exists
if [ -d "$NODE_MODULES_PATH" ]; then
  echo "🗑 Removing node_modules at $NODE_MODULES_PATH"
  rm -rf "$NODE_MODULES_PATH"
else
  echo "ℹ️ No node_modules found at $NODE_MODULES_PATH"
fi

echo "Cleanup complete."