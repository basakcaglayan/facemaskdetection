# 🔥 Real-Time Fire Detection with YOLOv8 and OpenCV

This project demonstrates real-time fire detection using a webcam and a fine-tuned YOLOv8 model. The system captures frames from your webcam, runs object detection to identify fire, and overlays bounding boxes and labels on the live video stream.
## ✨ Features

### 📸 Live Demo Features

- Real-time video feed from a webcam.
- YOLOv8 model for detecting fire.
- Bounding boxes and labels displayed over detected fire regions.
- Simple user interface using OpenCV.
- Exit cleanly with `Esc` key.

## 🧰 Requirements

Install dependencies from `requirements.txt`:

```bash
pip install opencv-python ultralytics supervision
```
Make sure you have the following:

- A working webcam
- Python 3.8+
- A trained YOLOv8 model saved as yolo.pt in the project directory

## 🚀 Usage
Run the script with:
```bash
python yolo.py
```
- A window will pop up showing the live webcam feed.
- If fire is detected, it will draw bounding boxes and labels on the frame.
- Press Esc to close the application.

## 📁 Project Structure
```plaintext
.
├── yolo.py               # Main script for real-time detection
├── yolo.pt               # Pretrained YOLOv8 model
├── requirements.txt      # Python dependencies

```

## 🔧 Customization
- You can fine-tune your own YOLOv8 model using Ultralytics and replace yolo.pt with your custom best.pt.
- To adjust labels or colors, modify the supervision annotators.

## 🙏 Acknowledgements

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)
- [Supervision by Roboflow](https://github.com/roboflow/supervision)

## 📄 License
This project is intended for educational and experimental use. Please contact the author for reuse or distribution permissions.
