#!/usr/bin/env python3
import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import String
class DaughterThreeNode(Node):

    def __init__(self):
        super().__init__("d_rover3")
        self.rand_num_genrtr_=self.create_publisher(String,"topic_3",10)
        self.timer_ = self.create_timer(3, self.send_mission_command)
    
    def send_mission_command(self):
        msg= String()
        
        x = random.randint(1,10)
        if x>=5:
          msg.data = "Task accomplished"
          self.rand_num_genrtr_.publish(msg)
        else:
          msg.data = "Mission failed"
          self.rand_num_genrtr_.publish(msg)    
      

def main(args=None):
    rclpy.init(args=args)
    node=DaughterThreeNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
   main()