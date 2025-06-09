# 😷 Real-Time Face Mask Detection with YOLO and OpenCV

This project uses a YOLO object detection model to detect whether a person is wearing a face mask **correctly**, **incorrectly**, or **not at all** in real-time using a webcam. The application overlays bounding boxes and labels directly on the video stream to provide instant visual feedback.


## 📌 Project Overview

Ensuring proper mask usage is vital in many public settings. This project leverages the power of the **YOLOv8 object detection model** and **OpenCV** to create a lightweight, fast, and accurate real-time system for monitoring face mask compliance.

The model can detect and classify:
- ✅ Mask Worn Correctly
- ⚠️ Mask Worn Incorrectly
- ❌ No Mask


## ✨ Features

- 🧠 **YOLOv8-Powered Detection**: Uses a pretrained model (`yolo.pt`) for fast and accurate predictions.
- 🎥 **Real-Time Webcam Feed**: Live video processing with OpenCV.
- 🖼️ **Bounding Boxes + Labels**: Visual overlay using `supervision` annotators.
- 🪶 **Lightweight and Easy to Use**: Minimal dependencies and straightforward code structure.


## 🧰 Tech Stack

- **Language**: Python 3.8+
- **Libraries**:
  - [`ultralytics`](https://github.com/ultralytics/ultralytics) - YOLOv8
  - [`opencv-python`](https://pypi.org/project/opencv-python/) - Camera and image processing
  - [`supervision`](https://github.com/roboflow/supervision) - Drawing bounding boxes and labels


## 📁 File Structure
```yaml
face-mask-detection/
├── yolo.py # Real-time webcam mask detection script
├── yolo.pt # YOLO model trained to detect face mask usage
└── README.md # Project documentation
```
## ⚙️ Installation

1. **Clone the Repository**  
```bash
git clone https://github.com/yourusername/face-mask-detection.git
cd face-mask-detection
```
2. **Create a Virtual Environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```
3. **Install Requirements**

```bash
pip install opencv-python ultralytics supervision
```
## 🚀 Usage
Run the face mask detection script using your webcam:
```bash
python yolo.py
```
Controls:
- Press ESC to exit the webcam stream.

## 📦 Model Weights
- Ensure yolo.pt (a YOLO model trained to detect mask, no-mask, and incorrect-mask) is in the same directory as yolo.py.
- You can train your own model using Ultralytics YOLOv8 or obtain a pretrained one suitable for mask detection.

## 🖼️ Example Output
Bounding boxes in different colors are drawn for each class with corresponding labels (e.g., "Mask", "No Mask", "Incorrect Mask").
## 📄 License
This project is intended for educational and experimental use. Please contact the author for reuse or distribution permissions.
## 🙏 Acknowledgements

 - [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
 - [OpenCV](https://opencv.org/)
 - [Roboflow Supervision](https://github.com/roboflow/supervision)
Thanks to open-source contributors and dataset providers who make projects like this possible!

