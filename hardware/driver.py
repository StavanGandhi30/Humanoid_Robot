from Adafruit_PCA9685 import PCA9685

class ServoDriver:
    def __init__(self, hardware_id, frequency=60, servo_min=150, servo_max=600, debug=False):
        self.pwm = PCA9685(address=int(hardware_id[:2]))
        self.pwm.set_pwm_freq(frequency)
        self.servo_min = servo_min
        self.servo_max = servo_max
        self.channel = int(hardware_id[2:])
        self.debug = debug
        self.pwm.set_pwm(self.channel, 0, 0)

    def set_servo_angle(self, angle):
        pulse = int(self.servo_min + (self.servo_max - self.servo_min) * int(angle) / 180)
        self.pwm.set_pwm(self.channel, 0, pulse)
        if self.debug:
            print(f"[ServoDriver] Moving {self.channel} to {angle} degrees")