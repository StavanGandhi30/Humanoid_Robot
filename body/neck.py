from hardware import *
from utils import *
import time

class Neck:
    def __init__(self, debug=False):
        self.roll_motor = Servo (
            name="Neck Roll Motor",
            hardware_id=(f"{hex_to_decimal('0x44')}10"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )
        self.left_motor = Servo (
            name="Neck Yam Motor",
            hardware_id=(f"{hex_to_decimal('0x44')}11"),
            min_angle=0, max_angle=90, rest_angle=45, debug=debug
        )
        self.right_motor = Servo (
            name="Neck Pitch Motor",
            hardware_id=(f"{hex_to_decimal('0x44')}12"),
            min_angle=90, max_angle=0, rest_angle=45, debug=debug
        )
        
    def rotate_left(self):
        pass
    
    def rotate_right(self):
        pass
    
    def move_neck(self, pitch: float, yaw: float):
        """
        pitch: 0.0 (down) to 1.0 (up)
        yaw:   0.0 (left) to 1.0 (right)
        """

        pitch = max(0.0, min(1.0, pitch))
        yaw = max(0.0, min(1.0, yaw))

        yaw_range = 0.3  # <- increase for stronger left/right movement

        # Calculate motor values
        yaw_offset = (yaw - 0.5) * yaw_range * 2  # range -yaw_range to +yaw_range

        motor1 = pitch - yaw_offset  # Motor 1 goes opposite
        motor2 = pitch + yaw_offset  # Motor 2 goes with yaw

        motor1 = max(0.0, min(1.0, motor1))
        motor2 = max(0.0, min(1.0, motor2))
        
        # Send to motors
        self.left_motor.move_to(map_range(motor1, self.left_motor.min_angle, self.left_motor.max_angle))
        self.right_motor.move_to(map_range(motor2, self.right_motor.min_angle, self.right_motor.max_angle))

    def get_motors(self):
        return [self.roll_motor, self.left_motor, self.right_motor]
    
    def __str__(self):
        motors = self.get_motors()
        return f"Neck ({len(motors)}) :\n\t" + "\n\t".join(str(motor) for motor in motors)