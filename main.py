from ultralytics import YOLO
import cv2
import math
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
cap.set(3, 416) 
cap.set(4, 416)

# Load the YOLO model
model = YOLO("model-data\exp2\weights\last.pt")

# Define class names
classNames = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
    'W', 'X', 'Y', 'Z'
]

fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', lambda event: plt.close() if event.key == 'q' else None)

while plt.fignum_exists(fig.number):
    ret, img = cap.read()
    if not ret:
        break

    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence: ", confidence)

            cls = int(box.cls[0])
            print("Class name: ", classNames[cls])

            org = (x1, y1 - 10)
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (0, 0, 0)
            thickness = 2

            cv2.putText(img, f'{classNames[cls]} {confidence}', org, font, fontScale, color, thickness)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ax.imshow(img_rgb)
    ax.axis('off')
    plt.draw()
    plt.pause(0.001)
    ax.cla()

cap.release()
plt.close()
