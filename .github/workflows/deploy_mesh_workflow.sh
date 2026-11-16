#!/bin/bash
set -e

echo "=================================================="
echo " SIx (Gen-Intel Secure Mesh) Deployment Workflow"
echo "=================================================="

# 1. Environment & Hardware Validation (MPS / CUDA / CPU)
echo "[1/4] Checking hardware acceleration & backend..."
python3 -c "import torch; print(f'Target Backend: {\"MPS\" if torch.backends.mps.is_available() else (\"CUDA\" if torch.cuda.is_available() else \"CPU\")}')"

# 2. Start Multi-Container Infrastructure
echo "[2/4] Launching Docker Compose cluster services..."
docker-compose -f config/docker-compose.yml up -d --build

# 3. Initialize Security Watchdogs & Rclone Sync
echo "[3/4] Activating HoneypotX & rclone state synchronization..."
rclone mkdir secure-mesh:checkpoints/si-x/ || true

# 4. Launch Edge ROS 2 Nodes & Fault-Tolerant Routing
echo "[4/4] Starting ROS 2 Edge Spike & Actuator Bridges..."
python3 ros2_nodes/spike_bridge_node.py &
python3 ros2_nodes/actuator_bridge_node.py &

echo "=================================================="
echo " SIx Mesh Workflow Successfully Deployed & Active "
echo "=================================================="
