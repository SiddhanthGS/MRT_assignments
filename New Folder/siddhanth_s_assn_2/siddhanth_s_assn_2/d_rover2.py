#!/usr/bin/env python3
import rclpy
import random
from rclpy.node import Node
from geometry_msgs.msg import Point

class DaughterTwoNode(Node):

    def __init__(self):
        super().__init__("d_rover2")
        self.rand_loc_genrtr_=self.create_publisher(Point,"topic_2",10)
        self.timer_ = self.create_timer(3, self.send_location_command)
    
    def send_location_command(self):
        msg = Point()
        msg.x = random.uniform(0,200)
        msg.y = random.uniform(0,200)
        msg.z = random.uniform(0,200)
        self.rand_loc_genrtr_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node=DaughterTwoNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
   main()




