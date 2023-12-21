#!/usr/bin/env python3
import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import Float32
class DaughterOneNode(Node):

    def __init__(self):
        super().__init__("d_rover1")
        self.rand_num_genrtr_=self.create_publisher(Float32,"topic_1",10)
        self.timer_ = self.create_timer(3, self.send_altitude_command)
        
    def send_altitude_command(self):
        msg = Float32()
        msg.data = random.uniform(0.0,100.0)
         
        self.rand_num_genrtr_.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)
    node = DaughterOneNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
   main()