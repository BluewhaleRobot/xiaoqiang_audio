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


# target_include_directories(xunfei_tts
#   ${catkin_INCLUDE_DIRS}
# )

# install(
#   TARGETS ${PROJECT_NAME} ${PROJECT_NAME}
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

# install(
#   DIRECTORY launch
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

# install(
#   DIRECTORY udevs
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

# install(
#   DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
# )

# install(
#   FILES  scripts/fixudev
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )