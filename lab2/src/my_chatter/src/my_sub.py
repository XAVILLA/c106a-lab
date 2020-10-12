#!/usr/bin/env python

import rospy
from my_chatter.msg import TimestampString


def callback(TimeString):
    time = rospy.get_time()
    print("Message: " + TimeString.s + ", Sent at: " + str(TimeString.f) + ", Received at: " + str(time))




def listener():
    rospy.Subscriber("my_chatter_talk", TimestampString, callback)
    rospy.spin()









if __name__ == '__main__':
    rospy.init_node('my_listener', anonymous=True)

    listener()
