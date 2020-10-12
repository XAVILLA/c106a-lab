#!/usr/bin/env python

import rospy
import sys
from std_msgs.msg import String
from geometry_msgs.msg import Twist



def stimulate(name):

  pub = rospy.Publisher(name+"/cmd_vel", Twist, queue_size=10)
  print("Reading from keyboard")
  print("---------------------------")
  print("Use arrow keys to move the turtle.")

  while not rospy.is_shutdown():
    user_input =raw_input()
    msg = Twist()
    if user_input == 'w':
      msg.linear.x = 2
    elif user_input == 's':
      msg.linear.x = -2
    elif user_input == 'a':
      msg.angular.z = 2
    elif user_input == 'd':
      msg.angular.z = -2
    pub.publish(msg)






if __name__ == '__main__':
  turtlename = sys.argv[1]
  rospy.init_node(turtlename, anonymous=True)
  try:
    stimulate(turtlename)
  except rospy.ROSInterruptException: pass
