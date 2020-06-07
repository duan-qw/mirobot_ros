import sys
import copy

import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',
                anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "mirobot_arm"
group = moveit_commander.MoveGroupCommander(group_name)

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)

# We can get the name of the reference frame for this robot:
planning_frame = group.get_planning_frame()
print "============ Reference frame: %s" % planning_frame

# We can also print the name of the end-effector link for this group:
eef_link = group.get_end_effector_link()
print "============ End effector: %s" % eef_link

# We can get a list of all the groups in the robot:
group_names = robot.get_group_names()
print "============ Robot Groups:", robot.get_group_names()

# Sometimes for debugging it is useful to print the entire state of the
# robot:
print "============ Printing robot state"
print robot.get_current_state()
print ""

# We can get the joint values from the group and adjust some of the values:
#joint_goal = group.get_current_joint_values()
#joint_goal[0] = joint_goal[0] + pi/4
#joint_goal[1] = 0.5
#joint_goal[2] = 0.5
#joint_goal[3] = 0.5

# The go command can be called with joint values, poses, or without any
# parameters if you have already set the pose or joint target for the group
#group.go(joint_goal, wait=True)

# Calling ``stop()`` ensures that there is no residual movement
#group.stop()

# pose_goal = geometry_msgs.msg.Pose()
# pose_goal.orientation.w =  0.135019244044
# pose_goal.orientation.x = -0.959524768969
# pose_goal.orientation.y = -3.00387332443e-05
# pose_goal.orientation.z = -0.247147770716
# pose_goal.position.x = 0.137206540744
# pose_goal.position.y = 0.0749533779735
# pose_goal.position.z = 0.14220353605
#
#
# #group.set_goal_position_tolerance(0.01)
# #group.set_goal_orientation_tolerance(0.01)
#
# group.set_pose_target(pose_goal)
# group.go(wait=True)
# # Calling `stop()` ensures that there is no residual movement
# group.stop()
# # It is always good to clear your targets after planning with poses.
# # Note: there is no equivalent function for clear_joint_value_targets()
# group.clear_pose_targets()
group.allow_replanning(True)
group.set_pose_reference_frame('dummy')
group.set_goal_position_tolerance(0.001)
group.set_goal_orientation_tolerance(0.001)
group.set_named_target('home')
group.go()
rospy.sleep(1)


start_pose = group.get_current_pose(eef_link).pose
print start_pose

wpose = copy.deepcopy(start_pose)

wpose = geometry_msgs.msg.Pose()

# wpose.position.z = 0.255026692607
# wpose.position.x = 0.133188800585
# wpose.position.y = 0.147771995049
#
#
# wpose.orientation.x = 0.653360443524
# wpose.orientation.y = 0.270366548255
# wpose.orientation.z = 0.270521315026
# wpose.orientation.w = 0.653330145133
# #wpose.orientation.w = 1
#
# group.set_pose_target(wpose)
#
# group.go(wait=True)
#
# group.stop()
# 0,1,2,3,4,5 : xyzrpy
#group.shift_pose_target(4,-0.707,eef_link)
#group.shift_pose_target(3,-1.59,eef_link)

#group.shift_pose_target(0,-0.05,eef_link)
group.shift_pose_target(1,0.1,eef_link)
#group.shift_pose_target(2,-0.05,eef_link)

group.go(wait=True)
group.stop()