from ultralytics import YOLO
import pandas as pd
import matplotlib.pyplot as plt
import torch_directml as dml
import torch
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
    data = "ASL-DB\data.yaml",
    epochs = 500, # r1 was 100 r2 was 200
    batch = 16, # r1 was 16 r2 was 8
    imgsz = 416,
    augment = True,
    verbose = True,
    project = output_path,
    patience= 10,
    name = "exp",
    save_period = 50,
    warmup_epochs = 5,
    val = True, 
    weight_decay = 0.0005,
    device = 0
)
