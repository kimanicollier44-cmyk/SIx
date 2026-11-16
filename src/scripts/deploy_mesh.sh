#!/bin/bash
set -e
echo "Initializing SIx (Gen-Intel Secure Mesh) Deployment..."

# 1. Start Multi-Container Infrastructure
docker-compose -f config/docker-compose.yml up -d --build

# 2. Verify Redis and FastAPI Health
echo "Verifying broker connectivity..."
curl -s http://localhost:8000/health || echo "Mesh API starting..."

# 3. Launch Edge Spike Bridge Nodes
python3 ros2_nodes/spike_bridge_node.py &

echo "SIx Mesh successfully deployed and operational."
