from serial.tools import list_ports

from pydobot import Dobot

port = list_ports.comports()[0].device
print(port)
device = Dobot(port=port)

pose = device.get_pose()
print(pose)
position = pose.position

device.move_to(position.x + 20, position.y, position.z, position.r, wait=False)
device.move_to(position.x, position.y, position.z, position.r, wait=True)  # we wait until this movement is done before continuing

device.close()