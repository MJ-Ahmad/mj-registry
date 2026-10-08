#!/usr/bin/env bash
# ./run.sh audit|code|codedir|menu|check|serve [args...]
cd "$(dirname "$0")"
c="$1"; shift
case "$c" in
  audit) python3 add_audit.py "$@" && python3 validate.py ;;
  code) python3 add_code.py "$@" && python3 validate.py ;;
  codedir) python3 add_code_dir.py "$@" && python3 validate.py ;;
  menu) python3 menu.py "$@" && python3 validate.py ;;
  check) python3 validate.py ;;
  serve) echo "Open http://localhost:8000"; python3 -m http.server 8000 ;;
  *) echo "usage: ./run.sh audit|code|codedir|menu|check|serve ..." ;;
esac
