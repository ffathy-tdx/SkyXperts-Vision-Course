<p align="center">
  <img src="assets/SkyX.png" width="75%" alt="SkyXperts UAVs Club Banner"/>
</p>

<h1 align="center"><b>SkyXperts UAVs Club</b></h1>
<p align="center"><i>Computer Vision Training Sessions – Hands-On for Future Robotics</i></p>

---

<div align="center">
  <!-- Badges -->
  <img src="https://img.shields.io/badge/python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Git-Required-E44C30?style=for-the-badge&logo=git&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-Required-%23white.svg?style=for-the-badge&logo=opencv&logoColor=green"/>
  <img src="https://img.shields.io/badge/VS%20Code-Recommended-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
</div>

---

## 🚀 Quick Start

1. **Fork** this repo to your GitHub account.
2. **Clone** your fork to your PC using `git clone`.
3. **Install** Anaconda (or Python 3.6+) & OpenCV.
4. **Complete** the tasks in each session folder inside `tasks/`.
5. **Push** your solution for each session to your own fork.

---

## 🛠️ Prerequisites

| Requirement        | Details                                                                                                 |
|--------------------|--------------------------------------------------------------------------------------------------------|
| Python             | ≥ 3.6 ([Download](https://www.python.org/downloads/))                                                  |
| Anaconda (optional)| [Install Guide](https://docs.anaconda.com/free/anaconda/install/)                                       |
| OpenCV-Python      | [Installation Guide](https://web.cecs.pdx.edu/~fliu/courses/cs410/python-opencv.html)                  |
| Git                | [Install Guide](https://github.com/git-guides/install-git)                                             |
| GitHub Account     | [Sign Up](https://github.com/join)                                                                     |
| VS Code + Git Ext. | [VS Code Download](https://code.visualstudio.com/), [Git Extension](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) |

---

## 📅 Sessions Overview

| Session   | Topics Covered & Materials                                                                                          |
|-----------|---------------------------------------------------------------------------------------------------------------------|
| **1**     | [Session 1 Content](./Session1/Session1.ipynb)  <br> - Reading, displaying, and saving images  <br> - Image representation (pixels, color channels, arrays)  <br> - Basic operations: resize, crop, rotate, flip  <br> - Handling images with OpenCV functions   |
| **2**     | [Session 2 Content](./Session2/Session2.ipynb) <br> - Image acquisition techniques (cameras, video, sensors)  <br> - Image formats & color spaces  <br> - BGR, grayscale, HSV conversions  <br> - Enhancement & filtering   |
| **2 (cont.)** | [Session 2 Continued](./Session2/Session2_cont.ipynb) <br> - Image gradients (horizontal, vertical, magnitude, orientation) <br> - Edge detection filters: Roberts, Prewitt, Sobel, Laplacian <br> - Canny edge detection pipeline <br> - Gaussian derivatives, LoG, DoG <br> - Connection to feature detection methods like SIFT |
| **3**     | [Session 3 Content](./Session3/Session3.ipynb) <br> - Feature extraction & keypoint detection <br> - Harris Corner Detector, SIFT, ORB <br> - Feature description & matching (BFMatcher) <br> - Feature-based image alignment |
| **4**     | [Session 4 Content](./Session4) <br> - CNN layers: convolutions, pooling, feature maps <br> - FashionMNIST: loading, training & visualizing a simple CNN <br> - Convolutional filters, Gaussian blur, Canny edge detection <br> - Haar Cascade face detection <br> - Feature vectors: ORB, HOG <br> - Object detection with YOLO |
| **5**     | [Session 5 Content](./Session5/Session5.ipynb) <br> - Image & color thresholding, Otsu thresholding <br> - Morphological operations: erosion, dilation, opening, closing, top-hat <br> - Edge & Canny edge detection revisited |
| **6**     | [Session 6 Content](./Session6/Session6.ipynb) <br> - Intro to neural networks with Keras/TensorFlow <br> - Loading & splitting the MNIST dataset <br> - Building, compiling & training a model <br> - Making predictions |
| **7**     | [Session 7 Content](./Session7/Session7.ipynb) <br> - Convolution layers & dataset preprocessing <br> - Training configuration parameters & result plotting <br> - Max pooling <br> - Data augmentation & training with augmented data |
| **8**     | [Session 8 Content](./Session8/Session8.ipynb) <br> - Pre-trained models & transfer learning <br> - Case study: an automated doggy door <br> - Loading a model, input/output dimensions <br> - Building on a base model |
| **9**     | [Session 9 Content](./Session9/Session9%5BOCR%5D.ipynb) <br> - Optical Character Recognition (OCR) <br> - Image preprocessing for OCR <br> - Text detection & extraction <br> - Using pytesseract for character recognition |

### 📝 Tasks

| Task | Covers | Link |
|------|--------|------|
| **1** | Sessions 1 & 2: basic image ops, resizing, cropping, rotating, color spaces, sharpening, noise & median filtering | [tasks1.ipynb](./tasks/tasks1.ipynb) |
| **2** | Sessions 2 (cont.) & 3: DoG/LoG & edge-preserving denoising filters, SIFT vs. ORB, feature matching | [tasks2.ipynb](./tasks/tasks2.ipynb) |
| **3** | Session 4: convolutional filters, a simple CNN on FashionMNIST, feature map visualization, Haar Cascade face detection | [tasks3.ipynb](./tasks/tasks3.ipynb) |
| **4** | Session 5+: CNN on MNIST and YOLOv8 (pretrained inference & a small training demo) | [tasks4.ipynb](./tasks/tasks4.ipynb) |

---

## 📚 Resources

- [OpenCV-Python Installation](https://web.cecs.pdx.edu/~fliu/courses/cs410/python-opencv.html)  
- [OpenCV Installation using Anaconda](https://medium.com/@pranav.keyboard/installing-opencv-for-python-on-windows-using-anaconda-or-winpython-f24dd5c895eb)
- [YOLOv1 – You Only Look Once (Redmon et al., 2016)](https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Redmon_You_Only_Look_CVPR_2016_paper.html)  
- [Viola-Jones Face Detection (2001)](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf)  
- [Canny Edge Detector (1988 BMVC Paper)](https://www.bmva-archive.org.uk/bmvc/1988/avc-88-023.pdf)  
- [An Introduction to Convolutional Neural Networks (2015)](https://arxiv.org/abs/1511.08458)


---

## 🙌 Contribution & Community

- Complete tasks, share your solutions, and collaborate with the team!
- **Issues or questions?** Open an Issue or contact me at <a href="mailto:ffathy2004@gmail.com">ffathy2004@gmail.com</a>.

<p align="center">
  <i>SkyXperts UAVs Club</i>
</p>
