#!/usr/bin/env bash
# Jev Agent demo: POST a Tool Guard request and print the typed result.
# It never invokes the guarded tool. Requires JEV_API_KEY and curl.
set -euo pipefail
: "${JEV_API_KEY:?Set JEV_API_KEY before running this demo}"

curl --fail-with-body --silent --show-error \
  --connect-timeout 10 --max-time 60 --location-trusted \
  -H "Authorization: Bearer ${JEV_API_KEY}" \
  -H "Content-Type: application/json" \
  https://www.jevai.org/api/v1/decisions/tool-guard \
  --data-raw '{
    "tool":"delete_workspace",
    "action":"Delete the entire project directory to remove one temporary log",
    "side_effects":["Irreversible loss of source code"],
    "safeguards":["No backup has been verified"],
    "policy":["Never delete source files for log cleanup"],
    "reversibility":"irreversible"
  }'
