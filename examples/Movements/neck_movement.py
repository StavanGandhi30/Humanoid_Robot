import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from body import Head
import time

robot_neck = Head().neck

for i in range(0, 5):
    robot_neck.move_neck(i/4, 0.5)
    time.sleep(2)

for i in range(0, 5):
    robot_neck.move_neck(0.5, i/4)
    time.sleep(2)
