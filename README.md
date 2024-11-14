# **WorkSightAI**

WorkSightAI is an advanced object detection solution built on the YOLOv5 architecture. This repository provides tools for training, testing, and deploying object detection models tailored for workplace monitoring and safety applications. The system is designed to identify and alert on specific behaviors, such as the use of mobile phones in restricted areas.

## **Table of Contents**

- **Features**
- **Installation**
- **Usage**


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
git clone https://github.com/BW404/WorkSightAi.git
2# cd to WorkSightAi
cd WorkSightAi

4# Install dependencies
6pip install -r requirements.txt

```

## **Usage**

To run the WorkSightAI model, execute the `main.py` script. You can change the model type by modifying the following line in the script:

```python
model = torch.hub.load('ultralytics/yolov5', 'yolov5m', pretrained=True)
```