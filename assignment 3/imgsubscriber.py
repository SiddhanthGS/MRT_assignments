#!/usr/bin/env python
import cv2 as cv
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError

bridge=CvBridge()
class SubscriberNode2(Node):
    def callback(self,msg):
       # bridge=CvBridge()
        self.get_logger().info("image received") 
        image_new=bridge.imgmsg_to_cv2(msg)
        canny=cv.Canny(image_new,100,200)
        
        cv.imshow('processed',canny)
        cv.waitKey(0)

    def __init__(self):

      

        super().__init__("imgsubscriber_node")
        
        self.basestation_sub_=self.create_subscription(Image,"webcam",self.callback,10)

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode2()

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
   main()