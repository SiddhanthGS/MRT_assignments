#!/usr/bin/env python3
import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Point
from std_msgs.msg import String


class SubscriberNode(Node):
    def callback(self,msg):
          self.get_logger().info(str(msg)) 


    def __init__(self):

      

        super().__init__("basestation")
        self.basestation_sub_=self.create_subscription(Float32,"topic_1",self.callback,10)
        self.basestation_sub_=self.create_subscription(Point,"topic_2",self.callback,10)
        self.basestation_sub_=self.create_subscription(String,"topic_3",self.callback,10)

        #def callback(self,msg):
        #  self.get_logger().info(msg)    
    
           

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
   main()