import cv2
import numpy as np
from picamera2 import Picamera2
from pycoral.adapters.detect import get_objects
from pycoral.adapters.common import input_size
from pycoral.utils.edgetpu import make_interpreter

import time

# Load Edge TPU model
interpreter = make_interpreter("./coral-models/ssd_mobilenet_v2_coco_quant_postprocess_edgetpu.tflite")
interpreter.allocate_tensors()

# Load labels
with open("./coral-models/coco_labels.txt", 'r') as f:
    labels = {int(i): name.strip() for i, name in enumerate(f.readlines())}

# Initialize Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (int(1000), int(600))
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()
time.sleep(2)

while True:
    start_time = time.time()

    frame = picam2.capture_array()
    input_w, input_h = input_size(interpreter)

    # Resize and convert for model
    resized = cv2.resize(frame, (input_w, input_h))
    input_tensor = np.expand_dims(resized, axis=0)

    interpreter.set_tensor(interpreter.get_input_details()[0]['index'], input_tensor)
    interpreter.invoke()

    objs = get_objects(interpreter, score_threshold=0.5)

    for obj in objs:
        bbox = obj.bbox
        x0, y0, x1, y1 = bbox.xmin, bbox.ymin, bbox.xmax, bbox.ymax

        # Scale box to original image
        scale_x, scale_y = frame.shape[1] / input_w, frame.shape[0] / input_h
        x0, x1 = int(x0 * scale_x), int(x1 * scale_x)
        y0, y1 = int(y0 * scale_y), int(y1 * scale_y)

        label = labels.get(obj.id, obj.id)
        cv2.rectangle(frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
        cv2.putText(frame, f"{label}: {obj.score:.2f}", (x0, y0 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        
    fps = 1.0 / (time.time() - start_time)
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    
    cv2.imshow("Coral Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
picam2.close()
