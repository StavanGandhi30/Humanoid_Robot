import cv2
import numpy as np
from picamera2 import Picamera2

# Initialize Picamera2
picam2 = Picamera2()
# Configure the camera (adjust resolution as needed)
config = picam2.create_preview_configuration({"format": 'XRGB8888'})
picam2.configure(config)

# Start the camera
picam2.start()

try:
    while True:
        # Capture frame
        frame = picam2.capture_array()

        # Display the frame
        cv2.imshow("IMX708 Feed", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Release resources
    picam2.close()
    cv2.destroyAllWindows()
