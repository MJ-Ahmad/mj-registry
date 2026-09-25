#!/usr/bin/env bash
# ./run.sh init "Name" | node ... | log ... | verify [--anchor] | build | serve
cd "$(dirname "$0")"; c="$1"; shift
case "$c" in
  init) python3 add_node.py --init "$@" ;;
  node) python3 add_node.py "$@" && python3 build.py ;;
  log) python3 log.py "$@" && python3 build.py ;;
  verify) python3 verify.py "$@" ;;
  build) python3 build.py ;;
  serve) echo "Open http://localhost:8001"; python3 -m http.server 8001 ;;
  *) echo "usage: ./run.sh init|node|log|verify|build|serve" ;;
esac
