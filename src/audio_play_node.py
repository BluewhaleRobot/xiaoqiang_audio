#!/usr/bin/env python
# encoding=utf-8
# The MIT License (MIT)
#
# Copyright (c) 2018 Bluewhale Robot
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Randoms
# 

import time
import rospy
from audio_common_msgs.msg import AudioData
from std_msgs.msg import Bool
from subprocess import Popen
import subprocess
import os

if __name__ == "__main__":
    rospy.init_node("xiaoqiang_audio_play", anonymous=False)
    # get to know if a audio is playing
    playing_audio_pub = rospy.Publisher("~audio_status", Bool, queue_size=10)

    processing_flag = False
    def play_audio(audio_data):
        global processing_flag
        if processing_flag:
            return
        processing_flag = True
        # write content to file 
        audio_file_name = "audio_" + str(int(time.time()))
        with open(audio_file_name, "w+") as audio_file:
            audio_file.write(audio_data.data)
        # play it with mplaer
        play = Popen(["mplayer", audio_file_name], universal_newlines=True,
            stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        play.wait()
        os.remove(audio_file_name)
        processing_flag = False
    sub = rospy.Subscriber("~audio", AudioData, play_audio)

    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        audio_status = Bool()
        audio_status.data = processing_flag
        playing_audio_pub.publish(audio_status)
        rate.sleep()