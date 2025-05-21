from body import Head
import time

robot_head = Head()
robot_eyes, robot_eyelids, robot_eyebrows, robot_mouth, robot_neck = robot_head.loadVar()

while True:
    user_input = ("Write Something > ")
    robot_mouth.tts.speak(user_input, robot_mouth)
    