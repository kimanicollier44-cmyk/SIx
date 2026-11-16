#!/usr/bin/env bash
set -e

echo "========================================"
echo " Deploying SI-X Secure Mesh Node"
echo "========================================"

# 1. Navigate to Root Workspace
cd "$(dirname "$0")/.."

# 2. Launching Docker Compose cluster services (with CI environment check)
echo "[1/4] Checking Docker Compose cluster services..."
if docker compose version &> /dev/null; then
    docker compose -f config/docker-compose.yml config > /dev/null
    if [ "$CI_MODE" != "true" ]; then
        docker compose -f config/docker-compose.yml up -d --build
    else
        echo "[1/4] CI Mode active: validated docker-compose configuration successfully."
    fi
else
    echo "[1/4] Docker Compose v2 plugin not available. Skipping container launch."
fi

# 3. Initialize Security Watchdogs & Rclone Sync (with graceful CI fallback)
echo "[2/4] Activating HoneypotX & rclone state synchronization..."
if command -v rclone &> /dev/null && rclone listremotes 2>/dev/null | grep -q "secure-mesh:"; then
    rclone mkdir secure-mesh:checkpoints/si-x/ || true
else
    echo "[2/4] rclone remote 'secure-mesh' not configured. Skipping remote sync."
fi

# 4. Launch Edge ROS 2 Nodes & Fault-Tolerant Routing (Syntax checks in CI)
echo "[3/4] Checking ROS 2 Edge Spike & Actuator Bridges..."
if [ "$CI_MODE" = "true" ]; then
    echo "[3/4] CI Mode active: Syntax checking ROS 2 nodes..."
    python3 -m py_compile ros2_nodes/spike_bridge_node.py ros2_nodes/actuator_bridge_node.py
else
    python3 ros2_nodes/spike_bridge_node.py &
    python3 ros2_nodes/actuator_bridge_node.py &
fi

echo "========================================"
echo " SI-X Mesh Workflow Successfully Executed"
echo "========================================"
