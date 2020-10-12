#!/usr/bin/env python

import rospy
import tf2_ros
import sys



def listener(frame1, frame2):
  tfBuffer = tf2_ros.Buffer()
  tfListener = tf2_ros.TransformListener(tfBuffer)
  #r = rospy.Rate(1)

  while not rospy.is_shutdown():
    #r.sleep()
    rospy.sleep(1.)
    trans = tfBuffer.lookup_transform(frame1, frame2, rospy.Time())
    print("At time")
    print(rospy.get_time())
    print("Translation: ")
    print(trans.transform.translation.x, trans.transform.translation.y, trans.transform.translation.z)
    print("Rotation: ")
    print(trans.transform.rotation.x, trans.transform.rotation.y, trans.transform.rotation.z, trans.transform.rotation.w)
    

    









if __name__ == '__main__':
    rospy.init_node('tf_listener', anonymous=True)
    frame1 = sys.argv[1]
    frame2 = sys.argv[2]
    listener(frame1, frame2)
#    try:
#      listener(frame1, frame2)
#    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, #tf2_ros.ExtrapolationException):
#      print("error")
