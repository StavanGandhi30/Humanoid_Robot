import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from body import Head
import time

robot_head = Head()
robot_eyes, robot_eyelids, _, _, _ = robot_head.loadVar()

print("Looking Center")
robot_eyes.look_center()
time.sleep(2)

for _ in range(3):
    print("Opening Eyes")
    robot_eyelids.open()
    time.sleep(2)
    print("Looking Left")
    robot_eyes.look_left()
    time.sleep(2)
    print("Looking Right")
    robot_eyes.look_right()
    time.sleep(2)
    print("Looking Center")
    robot_eyes.look_center()
    time.sleep(2)
    print("Blinking")
    robot_eyelids.blink()
    time.sleep(2)
    print("Looking Up")
    robot_eyes.look_up()
    time.sleep(2)
    print("Looking Down")
    robot_eyes.look_down()
    time.sleep(2)
    print("Looking Center")
    robot_eyes.look_center()
    time.sleep(2)
    print("Closing Eyes")
    robot_eyelids.close()
    time.sleep(2)