from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
   ld =LaunchDescription()

   d_rover1 = Node(
      package = "siddhanth_s_assn_2",
      executable="d_rover1"
   )

   d_rover2 = Node(
      package = "siddhanth_s_assn_2",
      executable="d_rover2"
   )

   d_rover3 = Node(
      package = "siddhanth_s_assn_2",
      executable="d_rover3"
   )

   basestation = Node(
      package = "siddhanth_s_assn_2",
      executable="basestation"

   )
   ld.add_action(d_rover1)
   ld.add_action(d_rover2)
   ld.add_action(d_rover3)
   ld.add_action(basestation)

   return ld

   