import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleController(Node):
    def __init__(self):
        super().__init__('circle_controller')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.declare_parameter('radius', 2.0)
        self.declare_parameter('speed', 1.5)
        self.timer = self.create_timer(0.1, self.move_circle)
        self.get_logger().info("Elite Circle Controller Active!")

    def move_circle(self):
        r = self.get_parameter('radius').get_parameter_value().double_value
        v = self.get_parameter('speed').get_parameter_value().double_value
        omega = v / r        
        msg = Twist()
        msg.linear.x = v
        msg.angular.z = omega
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CircleController()
    rclpy.spin(node)
    rclpy.shutdown()