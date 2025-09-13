#!/bin/sh
set -e

echo "=== Python version ==="
python3 --version 2>/dev/null || python --version

echo "=== Copying workspace to writable directory ==="
cp -r /workspace /workspace-rw
cd /workspace-rw

echo "=== Running tests ==="
make -C tests all

echo "=== Tests completed successfully ==="
