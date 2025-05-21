from hardware import *
from utils import *
import time

class Eyelids:
    def __init__(self, debug=False):
        self.__left_upper_eyelid = Servo (
            name="Left Upper Eyelid",
            hardware_id=(f"{hex_to_decimal('0x41')}02"),
            min_angle=50, max_angle=0, rest_angle=25, debug=debug
        )

        self.__left_lower_eyelid = Servo (
            name="Left Lower Eyelid",
            hardware_id=(f"{hex_to_decimal('0x41')}03"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )

        self.__right_upper_eyelid = Servo (
            name="Right Upper Eyelid",
            hardware_id=(f"{hex_to_decimal('0x41')}04"),
            min_angle=0, max_angle=50, rest_angle=25, debug=debug
        )

        self.__right_lower_eyelid = Servo (
            name="Right Lower Eyelid",
            hardware_id=(f"{hex_to_decimal('0x41')}05"),
            min_angle=20, max_angle=0, rest_angle=10, debug=debug
        )

        self.left_eyelids = [ self.__left_upper_eyelid, self.__left_lower_eyelid ]
        self.right_eyelids = [ self.__right_upper_eyelid, self.__right_lower_eyelid ]
        self.debug=debug
    
    def blink(self, pause=0.25):
        self.close()
        time.sleep(pause)
        self.open()
        
    def close(self, type="both"):
        if (type=="both"):
            self.__left_upper_eyelid.move_to_min_pos()
            self.__right_upper_eyelid.move_to_min_pos()
            time.sleep(0.001)
            self.__left_lower_eyelid.move_to_min_pos()
            self.__right_lower_eyelid.move_to_min_pos()
            time.sleep(0.001)
        elif (type=="left"):
            self.__left_upper_eyelid.move_to_min_pos()
            self.__left_lower_eyelid.move_to_min_pos()
        elif (type=="right"):
            self.__right_upper_eyelid.move_to_min_pos()
            self.__right_lower_eyelid.move_to_min_pos()
        else:
            if self.debug:
                print("Invalid Parameter")

    def open(self, type="both"):
        if (type=="both"):
            self.__left_upper_eyelid.move_to_max_pos()
            self.__right_upper_eyelid.move_to_max_pos()
            time.sleep(0.001)
            self.__left_lower_eyelid.move_to_max_pos()
            self.__right_lower_eyelid.move_to_max_pos()
            time.sleep(0.001)
        elif (type=="left"):
            self.__left_upper_eyelid.move_to_max_pos()
            self.__left_lower_eyelid.move_to_max_pos()
        elif (type=="right"):
            self.__right_upper_eyelid.move_to_max_pos()
            self.__right_lower_eyelid.move_to_max_pos()
        else:
            if self.debug:
                print("Invalid Parameter")

    def get_motors(self):
        return [self.__left_upper_eyelid, self.__left_lower_eyelid, self.__right_upper_eyelid, self.__right_lower_eyelid]
    
    def __str__(self):
        motors = self.get_motors()
        return f"EyeLids ({len(motors)}) :\n\t" + "\n\t".join(str(motor) for motor in motors)