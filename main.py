import torch
import cv2
from datetime import datetime

torch.set_num_threads(torch.get_num_threads())

# Load YOLOv5 model from torch hub
model = torch.hub.load('ultralytics/yolov5', 'yolov5m', pretrained=True)  #Chnage model here.

def send_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("alert.txt", "a") as f:
        f.write(f"{timestamp} - {message}\n")

# Capture video feed
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)

    # Filter for 'person' and 'cell phone' objects
    detections = results.pandas().xyxy[0]
    persons = detections[detections['name'] == 'person']
    phones = detections[detections['name'] == 'cell phone']

    alert_triggered = False
    for _, person in persons.iterrows():
        for _, phone in phones.iterrows():
            phone_mid_y = (phone['ymin'] + phone['ymax']) / 2

            # Skip alert if the phone is near the bottom of the frame (likely on a table)
            if phone_mid_y > frame.shape[0] * 0.90:
                continue  # Phone likely on table, so skip alert

            # Check if phone bounding box is within the person bounding box (indicating phone in hand)
            if (person['xmin'] < phone['xmax'] and person['xmax'] > phone['xmin'] and
                person['ymin'] < phone['ymax'] and person['ymax'] > phone['ymin']):
                
                # Alert if phone is detected in hand
                alert_triggered = True
                cv2.putText(frame, "ALERT: Phone in hand detected!", (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                send_alert("ALERT: A worker has a phone in their hand!")
                break

        if alert_triggered:
            break

    # Draw bounding boxes for people and phones only
    for _, person in persons.iterrows():
        x_min, y_min, x_max, y_max = int(person['xmin']), int(person['ymin']), int(person['xmax']), int(person['ymax'])
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)  # Green box for person
        cv2.putText(frame, "Person", (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    for _, phone in phones.iterrows():
        x_min, y_min, x_max, y_max = int(phone['xmin']), int(phone['ymin']), int(phone['xmax']), int(phone['ymax'])
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)  # Blue box for phone
        cv2.putText(frame, "Phone", (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Display the frame with detection boxes
    cv2.imshow('Camera Feed', frame)

    # Close with 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
