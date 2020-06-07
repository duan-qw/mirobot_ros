import sys
import copy

import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
import mirobot_control_node

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

# set base for mirobot
group.allow_replanning(True)
group.set_pose_reference_frame('dummy')
group.set_goal_position_tolerance(0.001)
group.set_goal_orientation_tolerance(0.001)

# set mirobot to home postion
group.set_named_target('home')
group.go()
rospy.sleep(1)

POSTION_BASE = 0.01
ORIENTATION_BASE = 0.05
modeMap = {'x': 0, 'y': 1, 'z': 2, 'R': 3, 'P': 4, 'Y': 5}
while True:
    mode = raw_input('input you control mode(x,y,z,R(roll),P(pitch),Y(yaw):')

    if mode == 'exit':
        break

    if mode not in {'x','y','z','R','P','Y'}:
        continue

    while True:
        direct = raw_input('input you control postion(w:+,s:-):')

        if direct == 'exit':
            break

        if direct not in {'w', 's'}:
            continue

        value = 0
        if mode in {'x','y','z'}:
            value = POSTION_BASE
        else:
            value = ORIENTATION_BASE

        if direct == 's':
            value = value * (-1)

        #move mirobot
        group.shift_pose_target(modeMap[mode], value, eef_link)
        group.go(wait=True)
        group.stop()
        print 'move succeeded'
