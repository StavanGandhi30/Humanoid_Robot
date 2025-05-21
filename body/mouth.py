from hardware import *
from utils import *
import time

class Mouth:
    def __init__(self, debug=False):
        self.left_upper_lip = Servo (
            name="Left Upper Lip",
            hardware_id=(f"{hex_to_decimal('0x44')}00"),
            min_angle=100, max_angle=0, rest_angle=80, debug=debug
        )
        self.left_lower_lip = Servo (
            name="Left Lower Lip",
            hardware_id=(f"{hex_to_decimal('0x44')}01"),
            min_angle=0, max_angle=60, rest_angle=20, debug=debug
        )
        self.right_upper_lip = Servo (
            name="Right Upper Lip",
            hardware_id=(f"{hex_to_decimal('0x44')}02"),
            min_angle=125, max_angle=180, rest_angle=155, debug=debug
        )
        self.right_lower_lip = Servo (
            name="Right Lower Lip",
            hardware_id=(f"{hex_to_decimal('0x44')}03"),
            min_angle=60, max_angle=0, rest_angle=40, debug=debug
        )

        # Lip Corners
        self.left_upper_lip_corner = Servo (
            name="Left Upper Lip Corner",
            hardware_id=(f"{hex_to_decimal('0x44')}04"),
            min_angle=120, max_angle=45, rest_angle=60, debug=debug
        )
        self.left_lower_lip_corner = Servo (
            name="Left Lower Lip Corner",
            hardware_id=(f"{hex_to_decimal('0x44')}05"),
            min_angle=60, max_angle=180, rest_angle=67, debug=debug
        )
        self.right_upper_lip_corner = Servo (
            name="Right Upper Lip Corner",
            hardware_id=(f"{hex_to_decimal('0x44')}06"),
            min_angle=75, max_angle=150, rest_angle=10, debug=debug
        )
        self.right_lower_lip_corner = Servo (
            name="Right Lower Lip Corner",
            hardware_id=(f"{hex_to_decimal('0x44')}07"),
            min_angle=120, max_angle=0, rest_angle=10, debug=debug
        )

        self.left_jaw = Servo (
            name="Left Jaw",
            hardware_id=(f"{hex_to_decimal('0x44')}08"),
            min_angle=0, max_angle=30, rest_angle=10, debug=debug
        )

        self.right_jaw = Servo (
            name="Right Jaw",
            hardware_id=(f"{hex_to_decimal('0x44')}09"),
            min_angle=180, max_angle=150, rest_angle=10, debug=debug
        )
        

        self.lips = [
            self.left_upper_lip, self.left_lower_lip,
            self.right_upper_lip, self.right_lower_lip
        ]

        self.lip_corners = [
            self.left_upper_lip_corner, self.left_lower_lip_corner,
            self.right_upper_lip_corner, self.right_lower_lip_corner
        ]
        
        self.tts = TTS()
       
    def move_to_round_lips(self):
        self.move_lips(to=0.5)
        self.move_lips_corner(to=0.0)
        self.move_jaw(to=0.2)
        
    def move_lips(self, to=0.0):
        self.move_lower_lips(to)
        self.move_upper_lips(to)
        
    def move_lips_corner(self, to=0.0):
        self.move_left_lips_corner(to)
        self.move_right_lips_corner(to)
            
    def move_upper_lips(self, to=0.0):
        self.left_upper_lip.move_to(map_range(to, self.left_upper_lip.min_angle, self.left_upper_lip.max_angle))
        self.right_upper_lip.move_to(map_range(to, self.right_upper_lip.min_angle, self.right_upper_lip.max_angle))
            
    def move_lower_lips(self, to=0.0):
        self.left_lower_lip.move_to(map_range(to, self.left_lower_lip.min_angle, self.left_lower_lip.max_angle))
        self.right_lower_lip.move_to(map_range(to, self.right_lower_lip.min_angle, self.right_lower_lip.max_angle))
    
    def move_left_lips_corner(self, to=0.0):
        self.left_upper_lip_corner.move_to(map_range(to, self.left_upper_lip_corner.min_angle, self.left_upper_lip_corner.max_angle))
        self.left_lower_lip_corner.move_to(map_range(to, self.left_lower_lip_corner.min_angle, self.left_lower_lip_corner.max_angle))
        
    def move_right_lips_corner(self, to=0.0):
        self.right_upper_lip_corner.move_to(map_range(to, self.right_upper_lip_corner.min_angle, self.right_upper_lip_corner.max_angle))
        self.right_lower_lip_corner.move_to(map_range(to, self.right_lower_lip_corner.min_angle, self.right_lower_lip_corner.max_angle))
        
    def move_jaw(self, to=0.0):
        self.left_jaw.move_to(map_range(to, self.left_jaw.min_angle, self.left_jaw.max_angle))
        self.right_jaw.move_to(map_range(to, self.right_jaw.min_angle, self.right_jaw.max_angle))
        
    def get_motors(self):
        return [
            self.left_upper_lip, self.left_lower_lip,
            self.right_upper_lip, self.right_lower_lip,
            self.left_upper_lip_corner, self.left_lower_lip_corner,
            self.right_upper_lip_corner, self.right_lower_lip_corner,
            self.jaw
        ]
    
    def __str__(self):
        motors = self.get_motors()
        return f"Mouth ({len(motors)}) :\n\t" + "\n\t".join(str(motor) for motor in motors)