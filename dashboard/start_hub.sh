#!/bin/bash
set -e

cd "$(dirname "$0")"

# Check for API key
if [ -z "$ANTHROPIC_API_KEY" ]; then
  echo ""
  echo "  ⚠  ANTHROPIC_API_KEY is not set."
  echo ""
  echo "  Run:  export ANTHROPIC_API_KEY=sk-ant-..."
  echo "  Then: bash start_hub.sh"
  echo ""
  exit 1
fi

# Install deps if needed
if ! python3 -c "import fastapi, uvicorn, anthropic" 2>/dev/null; then
  echo "  Installing dependencies…"
  pip install -q fastapi uvicorn anthropic
fi

echo ""
echo "  🫙  The 40's Cookbook — Agent Hub"
echo "  ────────────────────────────────"
echo "  Open:  http://localhost:8000"
echo ""

python3 backend.py
