#!/usr/bin/env python

# Copyright (c) 2013-2015, Rethink Robotics
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the Rethink Robotics nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""
Baxter RSDK Joint Position Example: keyboard
"""
import argparse

import rospy
import time

import baxter_interface
import baxter_external_devices

from baxter_interface import CHECK_VERSION

def rotate(joint_angles):
    left = baxter_interface.Limb('left')
    limb = left
    lj = left.joint_names()
    for i in range(7):
        if rospy.is_shutdown():
            exit()
        jname = lj[i]
        current_position = limb.joint_angle(jname)
        destination = joint_angles[i]
        difference  = destination - current_position
        delta = (difference/abs(difference)) * 0.1

        while abs(limb.joint_angle(jname)-destination) > .1 and not rospy.is_shutdown():
            joint_command = {jname: limb.joint_angle(jname) + delta}
            limb.set_joint_positions(joint_command)
            time.sleep(.1)
        joint_command = {jname: destination}
        limb.set_joint_positions(joint_command)
        time.sleep(.1)

    for i in range(7):
        print('joint' +  str(i) + "has currrent angle" + str(limb.joint_angle(lj[i])))

def main():
    rospy.init_node("joint_position_keyboard")
    joints = []
    for i in range(7):
        user_input = raw_input('please type in angle for joint ' + str(i+1) + ":")
        print("input angle for joint " +  str(i+1)  + ":"+ user_input)

        input_num = float(user_input)
        joints.append(input_num)

    rotate(joints)


if __name__ == '__main__':
    main()
