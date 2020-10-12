#!/usr/bin/env python

import rospy
from my_chatter.msg import TimestampString



def stimulate():

  pub = rospy.Publisher('my_chatter_talk', TimestampString, queue_size=10)

  while not rospy.is_shutdown():
    user_input =raw_input('Please enter a line of text and press <Enter>:')
    time = rospy.get_time()
    user_object = TimestampString(f = time, s = user_input)
    #user_object.s = user_input
    #user_object.f = time
    pub.publish(user_object)













if __name__ == '__main__':
  rospy.init_node('my_pub_node', anonymous=True)
  try:
    stimulate()
  except rospy.ROSInterruptException: pass


