from hardware import *
from utils import *

class Eyes:
    def __init__(self, debug=False):
        self.eye_yaw_motor = Servo (
            name="Eye Yaw Motor",
            hardware_id=(f"{hex_to_decimal('0x41')}00"),
            min_angle=0, max_angle=35, rest_angle=34/2, debug=debug
        )

        self.eye_pitch_motor = Servo (
            name="Eye Pitch Motor",
            hardware_id=(f"{hex_to_decimal('0x41')}01"),
            min_angle=0, max_angle=35, rest_angle=34/2, debug=debug
        )

    # Move some amount in left, right, up, or down direction
    def move_left(self, amount):
        self.eye_yaw_motor.move_to(self.eye_yaw_motor.current_angle - amount)

    def move_right(self, amount):
        self.eye_yaw_motor.move_to(self.eye_yaw_motor.current_angle + amount)

    def move_up(self, amount):
        self.eye_pitch_motor.move_to(self.eye_pitch_motor.current_angle - amount)

    def move_down(self, amount):
        self.eye_pitch_motor.move_to(self.eye_pitch_motor.current_angle + amount)

    # Move all the way in left, right, up, or down direction
    def look_left(self):
        self.eye_yaw_motor.move_to_min_pos()

    def look_right(self):
        self.eye_yaw_motor.move_to_max_pos()

    def look_up(self):
        self.eye_pitch_motor.move_to_min_pos()

    def look_down(self):
        self.eye_pitch_motor.move_to_max_pos()

    def look_center(self):
        self.eye_yaw_motor.move_to_rest_pos()
        self.eye_pitch_motor.move_to_rest_pos()
        
    def get_motors(self):
        return [self.eye_yaw_motor, self.eye_pitch_motor]
    
    def get_position(self):
        return [self.eye_yaw_motor.get_pos(), self.eye_pitch_motor.get_pos()]
        
    def __str__(self):
        motors = self.get_motors()
        return f"Eyes ({len(motors)}) :\n\t" + "\n\t".join(str(motor) for motor in motors)