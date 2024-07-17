from ultralytics import YOLO
import pandas as pd
import matplotlib.pyplot as plt
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

model.train(
    data = "ASL-DB\\data.yaml",
    epocs = 40,
    batch = 32,
    imgsz = 416,
    augment = True,
    verbose = True,
    project = "model-data",
    name = "exp",
    save_period = 20,
    warmup_epoc = 4,
    val = True, 
    weigth_decay = 0.0005,
    device = "cpu"
)