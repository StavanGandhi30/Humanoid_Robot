from hardware import *
from utils import *

class Eyebrows:
    def __init__(self, debug=False):
        self.left_eyebrow_outer = Servo (
            name="Left Outer Eyebrow",
            hardware_id=(f"{hex_to_decimal('0x41')}06"),
            min_angle=15, max_angle=0, rest_angle=10, debug=debug
        )
        self.left_eyebrow_inner = Servo (
            name="Left Inner Eyebrow",
            hardware_id=(f"{hex_to_decimal('0x41')}07"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )

        self.right_eyebrow_outer = Servo (
            name="Right Outer Eyebrow",
            hardware_id=(f"{hex_to_decimal('0x41')}08"),
            min_angle=0, max_angle=15, rest_angle=10, debug=debug
        )
        
        self.right_eyebrow_inner = Servo (
            name="Right Inner Eyebrow",
            hardware_id=(f"{hex_to_decimal('0x41')}09"),
            min_angle=20, max_angle=0, rest_angle=10, debug=debug
        )

    def move_left_eyebrow_outer(self, to=0.0):
        self.left_eyebrow_outer.move_to(map_range(to, self.left_eyebrow_outer.min_angle, self.left_eyebrow_outer.max_angle))

    def move_left_eyebrow_inner(self, to=0.0):
        self.left_eyebrow_inner.move_to(map_range(to, self.left_eyebrow_inner.min_angle, self.left_eyebrow_inner.max_angle))
    
    def move_right_eyebrow_outer(self, to=0.0):
        self.right_eyebrow_outer.move_to(map_range(to, self.right_eyebrow_outer.min_angle, self.right_eyebrow_outer.max_angle))

    def move_right_eyebrow_inner(self, to=0.0):
        self.right_eyebrow_inner.move_to(map_range(to, self.right_eyebrow_inner.min_angle, self.right_eyebrow_inner.max_angle))
    
    def get_motors(self):
        return [ self.left_eyebrow_outer, self.left_eyebrow_inner, self.right_eyebrow_outer, self.right_eyebrow_inner ]
    
    def __str__(self):
        motors = self.get_motors()
        return f"Eyebrows ({len(motors)}) :\n\t" + "\n\t".join(str(motor) for motor in motors)