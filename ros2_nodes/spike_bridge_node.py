import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import torch

class SpikeBridgeNode(Node):
    """ROS 2 Edge Robotic Node translating sensory sensor arrays into neuromorphic spike trains."""
    def __init__(self):
        super().__init__('spike_bridge_node')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'si_x/spike_bus', 10)
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'si_x/sensor_telemetry',
            self.listener_callback,
            10
        )
        self.get_logger().info("SIx Spike Bridge Node Initialized.")

    def listener_callback(self, msg):
        data_tensor = torch.tensor(msg.data)
        spikes = (data_tensor > 0.5).float()
        
        out_msg = Float32MultiArray()
        out_msg.data = spikes.tolist()
        self.publisher_.publish(out_msg)

def main(args=None):
    rclpy.init(args=args)
    node = SpikeBridgeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
