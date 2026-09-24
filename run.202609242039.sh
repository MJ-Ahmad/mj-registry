#!/usr/bin/env bash
# ./run.sh task|note|audit|done|check|serve [args...]
cd "$(dirname "$0")"
c="$1"; shift
case "$c" in
  task) python3 add_task.py "$@" && python3 validate.py ;;
  note) python3 add_note.py "$@" && python3 validate.py ;;
  audit) python3 add_audit.py "$@" && python3 validate.py ;;
  done) python3 complete_task.py "$@" && python3 validate.py ;;
  check) python3 validate.py ;;
  serve) echo "Open http://localhost:8000"; python3 -m http.server 8000 ;;
  *) echo "usage: ./run.sh task|note|audit|done|check|serve ..." ;;
esac
