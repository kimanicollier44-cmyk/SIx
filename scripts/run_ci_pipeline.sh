#!/bin/bash
set -e
echo "=== Starting SIx Continuous Integration Pipeline ==="

# 1. Run Python Unit Tests
echo "Executing test suite..."
python3 -m unittest discover -s tests -p "test_*.py"

# 2. Validate Configuration Manifests
echo "Validating Docker Compose configuration..."
docker-compose -f config/docker-compose.yml config > /dev/null

echo "=== CI Pipeline Completed Successfully ==="
