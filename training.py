from ultralytics import YOLO
import pandas as pd
import matplotlib.pyplot as plt
import time
import os

data_path = "ASL-DB"
output_path = "model-data"

model = YOLO("yolov8n.pt")

augmentationParams = {
    'fliplr': 0.55,
    'flipud': 0.35,
    'mixup': 0.1,
    'perspective': 0.00025,
    'hsv_h': 0.015
}

start_time = time.time()
model.train(
    data = "ASL-DB\data.yaml",
    epochs = 100,
    batch = 16,
    imgsz = 416,
    augment = True,
    verbose = True,
    project = output_path,
    name = "exp",
    save_period = 20,
    warmup_epochs = 4,
    val = True, 
    weight_decay = 0.0005,
    device = "cpu"
)
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time for 5 epochs: {elapsed_time} seconds")

# Estimate total time for desired number of epochs
total_epochs = 100  # Example total epochs
estimated_total_time = (elapsed_time / 5) * total_epochs
print(f"Estimated total training time: {estimated_total_time / 3600} hours")
