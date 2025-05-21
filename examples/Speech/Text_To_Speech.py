import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from body import Head

robot_mouth = Head().mouth

robot_mouth.say("Hello, World! My name is Shiv and I'm a programmer")
