#!/bin/bash
cd "$(dirname "$0")"
export PATH="/opt/homebrew/opt/postgresql@16/bin:$PATH"
source .venv/bin/activate
uvicorn main:app --reload --port 8000 --host 0.0.0.0

