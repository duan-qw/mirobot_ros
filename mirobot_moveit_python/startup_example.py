from time import sleep
from mirobot import Mirobot


m = Mirobot(debug=True)
m.connect('/dev/ttyUSB0')

sleep(3)

m.home_simultaneous()

sleep(10)

m.go_to_axis(0.03,20.53,-22,-0.08,2.04,-10,2000)

sleep(15)
m.home_simultaneous()
m.disconnect()