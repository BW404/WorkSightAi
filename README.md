# **WorkSightAI**

WorkSightAI is an advanced object detection solution built on the YOLOv5 architecture. This repository provides tools for training, testing, and deploying object detection models tailored for workplace monitoring and safety applications. The system is designed to identify and alert on specific behaviors, such as the use of mobile phones in restricted areas.

## **Table of Contents**

- **Features**
- **Installation**
- **Usage**
    - **Training**
    - **Testing**
    - **Inference**
- **Datasets**
- **Model Architecture**
- **Results**
- **Contributing**
- **License**

## **Features**

- **Real-Time Detection**: Fast and accurate detection of objects in real-time.
- **Custom Alerts**: Configurable alerts for specific behaviors, such as detecting mobile phones in hand.
- **User -Friendly Interface**: Simple command-line interface for training and inference.
- **Pre-trained Models**: Access to pre-trained weights for quick setup and testing.
- **Integration**: Compatible with various logging and visualization tools (WandB, TensorBoard, ClearML).

## **Installation**

To install WorkSightAI, clone this repository and install the required dependencies.

```
bashVerifyOpen In EditorEditCopy code
1# Clone the repository
2git clone https://github.com/BW404/WorkSightAI.git
3cd WorkSightAI
4
5# Install dependencies
6pip install -r requirements.txt

```

## **Usage**

### **Training**

To train the WorkSightAI model, use the following command:

```
bashVerifyOpen In EditorEditCopy code
1python train.py --img 640 --batch 16 --epochs 50 --data your_dataset.yaml --weights yolov5s.pt

```

- **`-img`**: Size of the input images.
- **`-batch`**: Batch size for training.
- **`-epochs`**: Number of training epochs.
- **`-data`**: Path to the dataset configuration file.
- **`-weights`**: Path to the pre-trained weights file.

### **Testing**

To test a trained model, use the following command:

```
bashVerifyOpen In EditorEditCopy code
1python val.py --weights runs/train/exp/weights/best.pt --data your_dataset.yaml

```

### **Inference**

To perform inference on images or videos, use the following command:

```
bashVerifyOpen In EditorEditCopy code
1python detect.py --source data/images/ --weights runs/train/exp/weights/best.pt --img 640

```

- **`-source`**: Path to the input images or video files.
- **`-weights`**: Path to the trained weights file.
- **`-img`**: Size of the input images.

## **Datasets**

WorkSightAI supports various datasets. You can use custom datasets or standard datasets such as COCO or VOC. Ensure your dataset is formatted correctly for training.

To download a sample dataset, you can use the provided script:

```
bashVerifyOpen In EditorEditCopy code
1bash data/scripts/get_dataset.sh

```

## **Model Architecture**

WorkSightAI is based on the YOLOv5 architecture, which includes:

- Backbone: CSPNet
- Neck: PANet
- Head: YOLO head for detection

This architecture allows for efficient processing and high accuracy in object detection tasks.

## **Results**

WorkSightAI achieves competitive results on various benchmarks, particularly in workplace monitoring scenarios. You can visualize the results using TensorBoard or other logging tools.