#!/bin/bash

echo "========================================"
echo "   Cedi Trakka – Intelligent Agent"
echo "   DCIT 403 | SPADE Implementation"
echo "========================================"

# Activate virtual environment if one exists
if [ -d "venv" ]; then
    echo "[INFO] Activating virtual environment..."
    source venv/bin/activate
fi

# Install dependencies if missing
echo "[INFO] Installing required Python packages..."
pip install spade >/dev/null 2>&1

# Run the SPADE agent
echo "[INFO] Starting the Cedi Trakka agent..."
python3 cedi_trakka_agent.py