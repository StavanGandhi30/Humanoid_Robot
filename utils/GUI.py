import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import tkinter as tk
from hardware.driver import ServoDriver
from utils import hex_to_decimal

def on_slider_change(servo, index, value):
    servo.set_servo_angle(value)
    output[index] = value
    print(output)

def create_sliders(root):
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=100)

    num_sliders = 16
    cols = 4
    rows = num_sliders // cols

    for i in range(rows):
        frame.rowconfigure(i, weight=1)

    for j in range(cols):
        frame.columnconfigure(j, weight=1)

    for idx in range(num_sliders):
        slider = tk.Scale(frame, from_=0, to=180, orient='horizontal', command=lambda value, idx=idx: on_slider_change(ServoDriver(hardware_id=f"{hex_to_decimal('0x44')}{idx}"), idx, value))
        slider.grid(row=idx // cols, column=idx % cols, padx=5, pady=5, sticky="nsew")

def main():
    root = tk.Tk()
    root.title("16 Scroll Inputs")
    create_sliders(root)
    root.mainloop()


if __name__ == "__main__":
    output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    main()