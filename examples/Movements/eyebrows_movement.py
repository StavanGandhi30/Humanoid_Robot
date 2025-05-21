import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from body import Head
import time

robot_eyebrows = Head().eyebrows

for i in range(0, 10):
    value = i/10.0
    robot_eyebrows.move_left_eyebrow_outer(to=value)    
    robot_eyebrows.move_left_eyebrow_inner(to=value)   
    robot_eyebrows.move_right_eyebrow_outer(to=value)
    robot_eyebrows.move_right_eyebrow_inner(to=value)
    time.sleep(1)

for i in range(10, 0, -1):
    value = i/10.0
    robot_eyebrows.move_left_eyebrow_outer(to=value)   
    robot_eyebrows.move_left_eyebrow_inner(to=value)
    robot_eyebrows.move_right_eyebrow_outer(to=value)
    robot_eyebrows.move_right_eyebrow_inner(to=value)
    time.sleep(1)
