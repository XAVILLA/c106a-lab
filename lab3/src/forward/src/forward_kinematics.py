#!/usr/bin/env python

import rospy
import tf2_ros
import sys
import numpy as np
from lab3_skeleton import lab3
from sensor_msgs.msg import JointState


def callback(jointS):
    left = np.array(jointS.position[2:9])
    #print(type(left))
    trans = lab3(left)
    print(trans)


def forward():
    rospy.Subscriber("robot/joint_states", JointState, callback)
    rospy.spin()










if __name__ == '__main__':
    rospy.init_node("forward")
    forward()
#    try:
#      listener(frame1, frame2)
#    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, #tf2_ros.ExtrapolationException):
#      print("error")