cmake_minimum_required(VERSION 2.8.3)
project(xiaoqiang_audio)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  std_msgs
  audio_common_msgs
)


catkin_package(
  CATKIN_DEPENDS roscpp rospy sensor_msgs std_msgs audio_common_msgs
)