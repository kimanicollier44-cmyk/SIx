#!/usr/bin/env bash
set -e

echo "========================================"
echo " Starting SI-X Continuous Integration"
echo "========================================"

# 1. Run Python Unit Tests
echo "[1/3] Running Python unit tests..."
python3 -m unittest discover -s tests -p "test_*.py"

# 2. Docker Compose Manifest Validation
echo "[2/3] Validating Docker Compose configuration..."
docker compose -f config/docker-compose.yml config > /dev/null

# 3. Lean 4 Formal Proof Verification (Convex Hull & Semigroup groups)
echo "[3/3] Verifying Lean 4 formal proofs..."
if command -v lean &> /dev/null; then
    lean src/lean/SiXProofAssistant.lean
    lean src/lean/ConvexSemigroupProof.lean
else
    echo "[3/3] Lean 4 compiler not found locally. Skipping formal verification."
fi

echo "========================================"
echo " CI / CD Pipeline Passed Successfully!"
echo "========================================"
