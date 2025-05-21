import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from body import Head
import time

robot_mouth = Head().mouth

for i in range(0, 10):
    value = i/10.0
    robot_mouth.move_upper_lips(to=value)    
    robot_mouth.move_lower_lips(to=value)   
    robot_mouth.move_left_lips_corner(to=value)
    robot_mouth.move_right_lips_corner(to=value)
    robot_mouth.move_jaw(to=value)
    time.sleep(1)

for i in range(10, 0, -1):
    value = i/10.0
    robot_mouth.move_upper_lips(to=value)   
    robot_mouth.move_lower_lips(to=value)
    robot_mouth.move_left_lips_corner(to=value)
    robot_mouth.move_right_lips_corner(to=value)
    robot_mouth.move_jaw(to=value)
    time.sleep(1)