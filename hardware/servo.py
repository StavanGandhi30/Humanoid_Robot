from hardware.driver import ServoDriver
from utils.utils import *

class Servo:
    def __init__(self, name, hardware_id, min_angle=0, max_angle=180, rest_angle=90, debug=False):
        self.name = name
        self.hardware_id = hardware_id
        self.min_angle = min_angle if self.__isValid(min_angle, between=[0,360]) else 0
        self.max_angle = max_angle if self.__isValid(max_angle, between=[0,360]) else 360
        self.rest_angle = rest_angle if self.__isValid(rest_angle) else self.min_angle
        self.current_angle = rest_angle
        self.debug = debug
        self.servo = ServoDriver(hardware_id=self.hardware_id)
        
    def move_to(self, angle):
        if self.__isValid(angle):
            self.servo.set_servo_angle(angle)
            self.current_angle = angle
            if self.debug:
                print(f"Moving motor {self.name} (ID: {self.hardware_id}) to {angle} degrees.")
        else:
            if self.debug:
                print(f"Motor {self.name} (ID: {self.hardware_id}) cannot move to {angle} degrees.")

    def move_to_max_pos(self):
        self.move_to(self.max_angle)

    def move_to_min_pos(self):
        self.move_to(self.min_angle)

    def move_to_rest_pos(self):
        self.move_to(self.rest_angle)

    def get_pos(self):
        return self.current_angle

    def __isValid(self, angle, between=[None, None]):
        return in_range(angle, self.min_angle, self.max_angle) if between[0] == None else in_range(angle, between[0], between[1])
    
    def __str__(self):
        return f"Motor: {self.name}, ID: {self.hardware_id}, Current Angle: {self.current_angle}°, Minimum Angle: {self.min_angle}°, Maximum Angle: {self.max_angle}°, Rest Angle: {self.rest_angle}°"