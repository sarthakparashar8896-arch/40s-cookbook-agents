#!/bin/bash
# The 40's Cookbook — Dashboard (auto-restarts on crash)
set -e
cd "$(dirname "$0")"

# ── Dependencies ───────────────────────────────────────────────────────────────
python3 -c "import streamlit, plotly, pandas, anthropic, supabase" 2>/dev/null || {
  echo "Installing dependencies…"
  pip3 install -q -r requirements.txt
}

# ── cloudflared binary ─────────────────────────────────────────────────────────
CF=/tmp/cloudflared
if [ ! -f "$CF" ]; then
  echo "Downloading tunnel binary…"
  ARCH=$(uname -m)
  [ "$ARCH" = "arm64" ] && SUFFIX="arm64" || SUFFIX="amd64"
  curl -sL "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-${SUFFIX}.tgz" \
    | tar xz -C /tmp/
  chmod +x "$CF"
fi

# ── Cleanup helper ─────────────────────────────────────────────────────────────
cleanup() {
  echo ""
  echo "  Shutting down…"
  kill "$STREAMLIT_PID" "$TUNNEL_PID" 2>/dev/null || true
  exit 0
}
trap cleanup INT TERM

echo ""
echo "  🫙  The 40's Cookbook — Dashboard"
echo "  ────────────────────────────────────────"

# ── Streamlit supervisor loop (restarts on crash) ──────────────────────────────
run_streamlit() {
  while true; do
    python3 -m streamlit run app.py \
      --server.port 8501 \
      --server.headless true \
      --browser.gatherUsageStats false \
      --server.fileWatcherType none \
      2>&1 | grep -Ev "^$|Watching|file watcher|Usage stats|warning" &
    STREAMLIT_PID=$!
    wait "$STREAMLIT_PID"
    echo "  ⚠  Streamlit stopped — restarting in 3s…"
    sleep 3
  done
}

# ── Tunnel supervisor loop (restarts and prints new URL each time) ─────────────
run_tunnel() {
  sleep 3   # give Streamlit a head start
  while true; do
    "$CF" tunnel --url http://localhost:8501 --no-autoupdate 2>&1 | while IFS= read -r line; do
      if echo "$line" | grep -q "trycloudflare.com"; then
        URL=$(echo "$line" | grep -o 'https://[^ ]*trycloudflare\.com')
        echo ""
        echo "  ✅  Share this URL with your team:"
        echo ""
        echo "      $URL"
        echo ""
        echo "  ⚠️  Keep this window open. If the URL changes, share the new one."
        echo ""
      fi
    done
    echo "  ⚠  Tunnel disconnected — reconnecting in 5s…"
    sleep 5
  done
}

run_streamlit &
STREAMLIT_PID=$!

run_tunnel &
TUNNEL_PID=$!

echo "  Both processes running. Press Ctrl+C to stop."
echo ""
wait
