# 🖐️ Dynamic Finger-Anchored Zoom with OpenCV & cvzone

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![cvzone](https://img.shields.io/badge/cvzone-HandTrackingModule-orange)

A real-time webcam application that lets you zoom in and out of your camera feed using your fingers! Pinch with your thumb and index finger to control the zoom, with the zoom centered dynamically between your fingertips. Built with OpenCV and the cvzone HandTrackingModule for a smooth, interactive experience.

---

## ✨ Features

- **Dynamic Finger-Anchored Zoom**: Zoom in/out by pinching your thumb and index finger.
- **Real-Time Hand Tracking**: Uses cvzone's HandTrackingModule for accurate finger detection.
- **Smooth Zooming**: Zoom is centered between your fingertips for intuitive control.
- **Easy to Use**: Just run and pinch to zoom. Press `q` to quit.

---

## 🚀 Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/genius-0963/AirPointer
   cd pythonOpenCV
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install opencv-python cvzone
   ```
   > You may also need to install `mediapipe`:
   > ```bash
   > pip install mediapipe
   > ```

---

## 🖥️ Usage

1. **Run the application:**
   ```bash
   python main.py
   ```
2. **Controls:**
   - Pinch your thumb and index finger to zoom in/out.
   - The zoom is centered between your fingertips.
   - Press `q` to quit.

---

## 🛠️ Dependencies
- Python 3.8+
- OpenCV
- cvzone
- mediapipe

---

## 🙏 Acknowledgments
- [cvzone](https://github.com/cvzone/cvzone) for the HandTrackingModule
- [OpenCV](https://opencv.org/)

---

## 📄 License
MIT License 
