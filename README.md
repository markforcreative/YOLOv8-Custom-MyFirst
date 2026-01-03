# Custom YOLOv8 Object Detection Training

[![Language](https://img.shields.io/badge/Language-English-blue)](#english) [![Language](https://img.shields.io/badge/Language-简体中文-red)](#简体中文)

---

<div id="english"></div>

## 📖 Introduction
This repository contains the training scripts and configuration for a custom **YOLOv8** object detection model. The model is trained to detect specific objects: **Nongfu Spring bottles (fs_bottle)** and **Powerbanks**.

The trained model is optimized and exported for edge deployment on Android devices.

## 🛠️ Environment & Requirements
- **Hardware**: Trained on NVIDIA RTX 4070 (12GB VRAM).
- **System**: Windows 11 + WSL2 (Ubuntu).
- **Framework**: Ultralytics YOLOv8, PyTorch.

## 🚀 Quick Start
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Prepare your dataset structure.
3.  Run training:
    ```bash
    python train.py
    ```
4.  Export to TFLite (for Android):
    ```bash
    yolo export model=best.pt format=tflite
    ```

## 📱 Android Deployment
The Android application source code that uses this model can be found here:
👉 **[YOLOv8-TFLite-Custom-Android-MyFirst](https://github.com/markforcreative/YOLOv8-TFLite-Custom-Android-MyFirst)**

---

<div id="简体中文"></div>

## 📖 简介
本仓库包含自定义 **YOLOv8** 目标检测模型的训练脚本和配置文件。该模型专门针对 **农夫山泉瓶身 (fs_bottle)** 和 **充电宝 (powerbank)** 进行训练。

训练后的模型已经过优化并导出，支持在 Android 设备上进行边缘端部署。

## 🛠️ 环境与依赖
- **硬件**：使用 NVIDIA RTX 4070 (12GB 显存) 训练。
- **系统**：Windows 11 + WSL2 (Ubuntu)。
- **框架**：Ultralytics YOLOv8, PyTorch。

## 🚀 快速开始
1.  安装依赖：
    ```bash
    pip install -r requirements.txt
    ```
2.  准备数据集（需符合 YOLO 格式）。
3.  运行训练：
    ```bash
    python train.py
    ```
4.  导出为 TFLite 模型（用于安卓）：
    ```bash
    yolo export model=best.pt format=tflite
    ```

## 📱 安卓端部署
使用此模型的 Android 应用源代码请访问下方链接：
👉 **[YOLOv8-TFLite-Custom-Android-MyFirst](https://github.com/markforcreative/YOLOv8-TFLite-Custom-Android-MyFirst)**


## 📂 Dataset (数据集)

> **Note**: The specific dataset used for training this model is **private** and is not included in this repository.
> 
> **注意**：本项目训练所使用的具体数据集为**私有数据**，暂不予公开。

If you want to train your own model, please prepare your dataset in the standard YOLO format as follows:
如果您想训练自己的模型，请按照以下标准的 YOLO 格式准备您的数据集：

```text
datasets/
└── my_datasets/
    ├── images/
    │   ├── train/
    │   └── val/          
    └── labels/
        ├── train/
        └── val/
```
Sample images can be found in assets/samples/ for testing inference.
（您可以在 assets/samples/ 目录下找到用于测试推理的样本图片。）