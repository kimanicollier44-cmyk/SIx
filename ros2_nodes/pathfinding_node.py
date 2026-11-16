import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import torch

class PathfindingBridgeNode(Node):
    """ROS 2 Edge Node executing neuromorphic path planning based on multi-sensor fusion."""
    def __init__(self):
        super().__init__('pathfinding_bridge_node')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'si_x/navigation_vector', 10)
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'si_x/spike_bus',
            self.navigation_callback,
            10
        )
        self.get_logger().info("SIx Pathfinding Bridge Node Active.")

    def navigation_callback(self, msg):
        input_tensor = torch.tensor(msg.data)
        steering_vector = torch.tanh(input_tensor * 1.5)
        
        out_msg = Float32MultiArray()
        out_msg.data = steering_vector.tolist()
        self.publisher_.publish(out_msg)

def main(args=None):
    rclpy.init(args=args)
    node = PathfindingBridgeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
