#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32
import json
import logging

# Configure logging matching repository standards
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class ActuatorBridgeNode(Node):
    """
    ROS 2 Actuator Bridge Node for SIx (Gen-Intel Secure Mesh).
    Listens for control commands/spike telemetry and translates them into physical 
    actuator signals or secure mesh feedback states.
    """
    def __init__(self):
        super().__init__('actuator_bridge_node')
        
        # Subscriptions
        self.command_subscription = self.create_subscription(
            String,
            '/si_x/mesh_commands',
            self.command_callback,
            10
        )
        
        # Publishers
        self.status_publisher = self.create_publisher(
            Float32,
            '/si_x/actuator_status',
            10
        )
        
        self.get_logger().info("ActuatorBridgeNode initialized and listening on /si_x/mesh_commands")

    def command_callback(self, msg: String):
        try:
            payload = json.loads(msg.data)
            action = payload.get("action", "IDLE")
            intensity = float(payload.get("intensity", 0.0))
            
            logging.info(f"Received secure mesh actuator command -> Action: {action}, Intensity: {intensity}")
            
            # Simulate actuator response feedback
            status_msg = Float32()
            status_msg.data = intensity * 0.95  # Simulated feedback efficiency
            self.status_publisher.publish(status_msg)
            
        except json.JSONDecodeError:
            self.get_logger().error(f"Failed to parse incoming command payload: {msg.data}")
        except Exception as e:
            self.get_logger().error(f"Error processing actuator command: {str(e)}")

def main(args=None):
    rclpy.init(args=args)
    node = ActuatorBridgeNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("ActuatorBridgeNode shutting down cleanly.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
