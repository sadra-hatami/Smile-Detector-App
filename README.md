<div align="center">

# Smile Detector App
# 😊📷

### A Real-Time Smile Detector Built with Python and OpenCV

A small computer-vision app that finds **faces** and **smiles** with Haar cascades — live from a **webcam**, or from a **still image**.

<br>

# 👨‍💻 **Sadra Hatami**

### *Developer • Software Engineer • Creator*

<br>

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Haar](https://img.shields.io/badge/Detector-Haar%20Cascades-orange?style=for-the-badge)
![Mode](https://img.shields.io/badge/Modes-Webcam%20%7C%20Image-0078D6?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-2C3E50?style=for-the-badge)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
![GitHub](https://img.shields.io/badge/Open_Source-Project-black?style=for-the-badge&logo=github)

<br>

[🌐 GitHub Profile](https://github.com/sadra-hatami)
•
[📧 Contact](mailto:sadra.hatami.1732@gmail.com)

</div>

---

# 📑 Table of Contents

- [About](#-about)
- [Why Smile Detector?](#-why-smile-detector)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Technologies](#️-technologies)
- [Usage](#️-usage)
- [Target Audience](#-target-audience)
- [Roadmap](#-roadmap)
- [FAQ](#-frequently-asked-questions)
- [Contributing](#-contributing)
- [Contact](#-contact)
- [License](#-license)
- [Copyright](#-copyright)
- [Support](#-support)

---

# 📖 About

**Smile Detector App** is a Python and OpenCV tool that looks for faces first, then looks for a smile inside each face.

There are two entry points:

- `smile_detector.py` — live webcam
- `smile_detector_on_image.py` — one local photo

Both scripts use OpenCV’s built-in Haar models (`haarcascade_frontalface_default.xml` and `haarcascade_smile.xml`). No extra model files are required.

When a smile is found, the app draws a box around the face, a box around the smile, and the label `SMILE :)`.

> **Tagline:** *A Python and OpenCV app that detects faces and smiles from a webcam or a still image using Haar cascades.*

---

# 🚀 Why Smile Detector?

Many vision demos need a large model download and a GPU.

This project stays small:

- Two short Python files
- Haar models that already ship with OpenCV
- One script for the camera and one script for a photo
- Immediate visual feedback

It is a compact computer-vision app, not a full machine-learning platform.

---

# ✨ Key Features

- 📷 Live webcam detection
- 🖼️ Still-image detection
- 😊 Face box, smile box, and `SMILE :)` label
- 📦 Built-in OpenCV Haar cascades
- ⚡ Grayscale frames for faster detection
- ⌨️ Press `q` to leave the webcam window
- 🖥️ Works on Windows, macOS, and Linux

---

# ⚙️ How It Works

1. Load the face cascade and the smile cascade from `cv2.data.haarcascades`.
2. Read a webcam frame or a file such as `test.jpg`.
3. Convert the frame to grayscale.
4. Find faces with `detectMultiScale`.
5. Crop each face and search that region for smiles.
6. Draw green face rectangles, blue smile rectangles, and the text label.

Webcam settings in `smile_detector.py`:

- Face: `scaleFactor=1.2`, `minNeighbors=5`, `minSize=(80, 80)`
- Smile: `scaleFactor=1.7`, `minNeighbors=20`, `minSize=(25, 25)`

The smile search runs only inside a detected face, not over the whole frame.

---

# 📁 Project Structure

```text
Smile-Detector-App/
├── smile_detector.py            # Live webcam detector
└── smile_detector_on_image.py   # Still-image detector
```

| File | Role |
|------|------|
| `smile_detector.py` | Opens camera `0`, loops until `q`, prints Persian status messages |
| `smile_detector_on_image.py` | Reads `test.jpg` from the same folder and shows one result window |

Place a photo named `test.jpg` next to `smile_detector_on_image.py` before running the image script.

---

# 🛠️ Technologies

- Python 3.8+
- OpenCV (`cv2`)
- Haar cascade classifiers bundled with OpenCV

---

# ▶️ Usage

### Install

```bash
git clone https://github.com/sadra-hatami/Smile-Detector-App.git
cd Smile-Detector-App
pip install opencv-python
```

### Live webcam

```bash
python smile_detector.py
```

Press `q` to quit. If the camera does not open, try changing `VideoCapture(0)` to `1`.

### Still image

Put `test.jpg` in the project folder, then:

```bash
python smile_detector_on_image.py
```

---

# 🎓 Target Audience

- Developers trying OpenCV for the first time
- Students learning Haar face detection
- Anyone who wants a small webcam or photo demo

---

# 🚀 Roadmap

Possible later improvements:

- 📁 Choose any image path from the command line
- 📸 Save a snapshot when a smile is found
- 🎛️ Sliders for `scaleFactor` and `minNeighbors`
- 👥 Stronger multi-face handling
- 🌙 A small desktop window around the camera view

---

# ❓ Frequently Asked Questions

### Does this use a neural network?

No. It uses classic Haar cascades from OpenCV.

### Why was no smile found?

Haar smile detection is lighting-sensitive. Face the camera, keep the face large enough, and smile clearly. You can raise or lower `minNeighbors` if the detector is too strict or too loose.

### The webcam did not open. What now?

Check camera permission and the camera index. The script starts with device `0`.

### Do I need to download XML files?

No. The scripts load them from `cv2.data.haarcascades`.

---

# 🤝 Contributing

Contributions are welcome.

You can:

- Report camera or detection bugs
- Improve default Haar parameters
- Add a command-line image path
- Submit Pull Requests

---

# 📬 Contact

**Developer:**

### **Sadra Hatami**

📧 [Email](mailto:sadra.hatami.1732@gmail.com)

🌐 [GitHub](https://github.com/sadra-hatami)

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project under the terms of the MIT License.

---

# © Copyright

© 2026 **Sadra Hatami**

All rights reserved.

The source code, application design, documentation, and project structure are protected under applicable copyright laws.

---

# ⭐ Support the Project

If this detector was useful, please consider:

⭐ Starring this repository

🐛 Reporting issues

💡 Suggesting improvements

---

<div align="center">

## Designed & developed with ❤️ for the developer community of Iran and the world

<br>

## 👨‍💻 **Sadra Hatami**

### Developer • Software Engineer • Creator

⭐ If you like this project, don't forget to star the repository!

</div>
