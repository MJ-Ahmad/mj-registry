#!/bin/bash
# Starts the Quraner Fariwala node network on a local host.
# Requires Node.js (no npm install needed — no external packages used).

cd "$(dirname "$0")"
echo "Starting local host..."
node server.js
