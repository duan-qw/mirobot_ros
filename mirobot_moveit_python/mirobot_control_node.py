import rospy
from sensor_msgs.msg import JointState
from time import sleep
from mirobot import Mirobot

class mirobot_control_node():
    def __init__(self, mirobot):
        rospy.init_node('mirobot_node', anonymous=True)
        rospy.Subscriber('joint_states', JointState, self.callback)
        self.m = mirobot

        self.postion = []

    def callback(self,data):
        datas = []
        # joint postion change to degree
        datas.append(round(data.position[0] * 52.297, 2))
        datas.append(round(data.position[1] * 52.297, 2))
        datas.append(round(data.position[2] * 52.297, 2))
        datas.append(round(data.position[3] * 52.297, 2))
        datas.append(round(data.position[4] * 52.297, 2))
        datas.append(round(data.position[5] * 52.297, 2))

        # move when postion change
        if cmp(self.postion, datas) != 0:
            self.postion = datas
            print "change postion to:", self.postion
            self.m.go_to_axis(self.postion[0],self.postion[1],self.postion[2],self.postion[3],self.postion[4],self.postion[5],2000)



if __name__ == '__main__':
    m = Mirobot(debug=True)
    m.connect('/dev/ttyUSB0')

    # set mirobot to init postion
    m.home_simultaneous()

    sleep(15)
    try:
        #mirobot control init
        mirobot_control_node(m)
    except rospy.ROSInterruptException:
        pass

    while True:
        rospy.spin()
        sleep(0.1)

    m.disconnect()
