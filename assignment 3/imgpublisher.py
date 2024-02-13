#!/usr/bin/env python
import cv2 
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError

#capture=cv2.VideoCapture(0)
#print(capture.isOpened())
#bridge=CvBridge()

class ImagePublishing(Node):
    def __init__(self):
        super().__init__("img_publisher_node")
        self.image_capturer_=self.create_publisher(Image,"webcam",5)
        self.timer_ = self.create_timer(5, self.send_photo_command)

    def send_photo_command(self):
        msg= Image() 
        capture=cv2.VideoCapture(0)
        print(capture.isOpened())
        bridge=CvBridge()
        x=0
        while True:
                isTrue,frame= capture.read()  
                x=x+1
                cv2.imshow('video',frame)
                msg =bridge.cv2_to_imgmsg(frame)
                self.image_capturer_.publish(msg)
                
                if cv2.waitKey(0) & 0xFF==ord('d'):
                  break
        
        

def main(args=None):
    rclpy.init(args=args)
    node=ImagePublishing()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
   main() 
