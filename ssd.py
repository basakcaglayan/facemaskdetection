import cv2
import os
import numpy as np
import tensorflow as tf

model_path = "saved_model"
if not os.path.exists(model_path):
    print(f"Model file not found: {model_path}")
    exit()
try:
    model = tf.saved_model.load(model_path)
    infer = model.signatures["serving_default"]
except Exception as e:
    print(f"Error loading the model: {e}")
    exit()

labels = ["with_mask", "without_mask", "mask_weared_incorrect"]

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Webcam could not be opened.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame (end of video?). Exiting...")
        break

    input_tensor = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    input_tensor = cv2.resize(input_tensor, (300, 300))
    input_tensor = np.expand_dims(input_tensor, 0)
    input_tensor = input_tensor / 255.0
    input_tensor = tf.convert_to_tensor(input_tensor, dtype=tf.float32) 

    try:
        output_dict = infer(input_tensor)

        scores = output_dict['output_0'].numpy()
        boxes = output_dict['output_1'].numpy()
        classes = output_dict['output_2'].numpy()

        threshold = 0.5
        if  scores > threshold:
                ymin, xmin, ymax, xmax = boxes
                h, w, _ = frame.shape
                left = int(xmin * w)
                top = int(ymin * h)
                right = int(xmax * w)
                bottom = int(ymax * h)
                
                class_id = int(classes) - 1
                if 0 <= class_id < len(labels):
                    label = labels[class_id]
                else:
                    label = f"Unknown class {class_id}"
                
                confidence = scores
                label_text = f"{label} {confidence:.2f}"

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, label_text, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
    except Exception as e:
        print(f"Error during inference: {e}")
        
    cv2.imshow("Webcam", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        print("Escape key pressed, exiting...")
        break

cap.release()
cv2.destroyAllWindows()