#!/bin/bash

# ReVanced Version Updater
# Simple wrapper script for update_versions.py

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

echo "🔄 ReVanced Version Updater"
echo "=========================="

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Error: Not in a git repository"
    exit 1
fi

# Check if Python dependencies are installed
echo "📦 Checking dependencies..."
python3 -c "import requests, packaging" 2>/dev/null || {
    echo "❌ Missing dependencies. Installing..."
    pip3 install -r python/requirements.txt
}

# Run the updater
echo "🚀 Running version updater..."
if [ "$1" = "--dry-run" ]; then
    echo "🧪 Dry-run mode enabled"
    DRY_RUN=1 python3 python/update_versions.py
elif [ "$1" = "--force" ]; then
    echo "⚡ Force mode enabled"
    FORCE=1 python3 python/update_versions.py
else
    python3 python/update_versions.py
fi

echo "✅ Done!"
