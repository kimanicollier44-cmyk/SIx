#!/usr/bin/env bash
set -e

echo "========================================"
echo " Deploying SI-X Secure Mesh Node"
echo "========================================"

# 1. Navigate to Root Workspace
cd "$(dirname "$0")/.."

# 2. Launching Docker Compose cluster services
echo "[1/4] Launching Docker Compose cluster services..."
docker compose -f config/docker-compose.yml up -d --build

# 3. Initialize Security Watchdogs & Rclone Sync
echo "[2/4] Activating HoneypotX & rclone state synchronization..."
rclone mkdir secure-mesh:checkpoints/si-x/ || true

# 4. Launch Edge ROS 2 Nodes & Fault-Tolerant Routing
echo "[3/4] Starting ROS 2 Edge Spike & Actuator Bridges..."
python3 ros2_nodes/spike_bridge_node.py &
python3 ros2_nodes/actuator_bridge_node.py &

echo "========================================"
echo " SI-X Mesh Workflow Successfully Deployed & Active"
echo "========================================"
