# Project 4: Building the Machine's Optic Nerve
### Domain: Deep Learning, Object Detection & Multi-Stream Computer Vision
**Developer:** Trishi Thakur  
**Batch:** 2026  
**Provider:** DecodeLabs Industrial Training Track  

---

## Project Overview
This repository contains the official implementation of **Project 4: Building the Machine's Optic Nerve**. Stepping away from passive data arrays, this project acts as an optional mastery phase to engineer a high-performance Python perception pipeline capable of translating unstructured physical world data into machine-readable digital intelligence.

The framework leverages **Transfer Learning** utilizing a pre-trained **MobileNet-SSD** (Single Shot Detector) network optimized for low-latency inference. By detaching the final classification layer, the script maps incoming visual arrays directly against localized feature geometries, instantly isolating and drawing visual bounding boundaries over real-world physical entities with exact statistical confidence.

---

## Architectural Framework: Input -> Process -> Output (IPO)
[cite_start]The application acts as an assembly pipeline processing dimensional matrix streams:

1. **Input (Multi-Stream Data Ingestion Engine):**
   * Processes high-resolution raw media files across four dynamic pathways: Local Image Arrays, Remote Web URL Targets, Live Video Streams (Webcam Feed), or Local Video Source Files.
   * Leverages `cv2.VideoCapture` protocols to ingest continuous frame buffers, sequentially decomposing each raw visual frame into a standard three-dimensional spatial array $(H \times W \times C)$ holding intensity coordinates from 0 to 255.

2. **Process (4D Blob Construction & Neural Inference):**
   * Executes **Matrix Pre-Processing Automation** utilizing `cv2.dnn.blobFromImage` to resize input grids to standard $300\times300$ network shapes, normalize scale factors, and execute mean color pixel subtraction.
   * Feeds the structured 4D input tensor into the **MobileNet-SSD Architecture Layer**.
   * Computes forward-pass deep learning inference across depthwise separable convolutional channels to isolate structural patterns.
   * Subjects raw output records to a **Softmax Function Matrix** to calculate probability frequencies across a pre-trained 21-class dataset.

3. **Output (The 80% Confidence Gate & Spatial Rendering):**
   * Implements a strict mathematical **80% Validation Threshold Gate**. Any localized detection output scoring a confidence index below $0.80$ is instantly dropped to eliminate hallucinations and minimize False Positives.
   * Decodes normalized matrix endpoints by scaling dimensions against the actual native pixel resolutions of the frame matrix.
   * Generates a high-contrast **Visual Confirmation Overlay**, drawing green boundary boxes around verified shapes and appending high-visibility uppercase typography tracking class tags and live confidence percentages.

---

## Core Project Files
* **`Task-4-Trishi_Thakur.py`** — The primary executable Python script containing the unified input routers, tensor scaling blob builders, confidence gates, and live rendering overlays.
* **`MobileNetSSD_deploy.prototxt`** — The network structural definition catalog defining the underlying neural layer paths and node configurations.
* **`MobileNetSSD_deploy.caffemodel`** — The foundational transfer learning weights file holding deep network coefficients built from millions of pre-trained ImageNet items.
* **`download_weights.py`** — An automated utility script built to dynamically fetch architecture target components over network sockets directly to the project workspace.

---

## Technical Validation Met
This pipeline satisfies all four mandatory validation milestones required by architectural blueprints:
* **Library Integration:** Error-free deployment of deep architecture layers through the native `cv2.dnn` wrapper.
* **Pre-Processing Integrity:** Seamless automated translation of arbitrary image matrices into uniform input blobs.
* **Accuracy Benchmarking:** Uncompromising evaluation of output predictions matching the minimum absolute 80% threshold standard.
* **Visual Confirmation:** Clean generation of high-contrast scaled rectangles and typography over the output stream.

---

## How To Setup & Run the Engine
Ensure your computing framework has access to web sockets and camera interfaces.

### 1. Ingestion Requirements:
```bash
pip install opencv-python numpy
```

### 2. Download Core Network Weights:
Run the automatic dependency utility tool to construct local architecture files:
```bash
python3 download_weights.py
```

### 3. Execution Flow:
Run the main pipeline loop and select your desired visual input routing pathway (1-4) inside the terminal selector interface:
```bash
python Task-4-Trishi_Thakur.py
```

Note: While inside a video stream mode window, tap the 'q' key on your keyboard to gracefully break and exit out of frame computation hooks.

Developed as part of the DecodeLabs AI Engineering Framework Portfolio.