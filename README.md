# mirobot_ros
Mirobot ROS packages
These packages support Moveit!, RViz and serial communication with Mirobot.
It can use in kinetic for python 2.x

# 1. Download and install
----
Download ros packages for mirobot

then manually copy package folders mirobot_urdf_2 and irobot_moveit_config into a catkin_ws/src.

Install ros serial package

```
$ sudo apt-get install ros-kinetic-serial
```

Compile

```
$ catkin_make
```
# 2. Set up enviroment
----
Source all setup.bash files to set up your enviroment.
```
# System configure ROS environment variables automatically every time you open a ternimal
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
# 3. Simulation and Control
----
Before ROS control, make sure that your manipulator is in the "homing" position. Connect your mirobot to computer and get USB permission to access mirobot
```
$ sudo chmod +777 /dev/ttyUSB0
```
If you are using a virtual machine running Linux, turn off graphics hardware acceleration, otherwise gazebo may not start properly.

## 3.1 Rviz Control Mode:
Show the xacro model of mirobot in rviz
```
roslaunch mirobot_moveit_config demo.launch
```
## 3.2 Control mirobot 
Run mirobot_moveit_python/


