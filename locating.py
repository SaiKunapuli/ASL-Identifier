import tensorflow as tf

from official.vision.beta.projects.object_detection import main

# Load the object detection model
model = main.ObjectDetectionModel()

# Use the model for object detection
outputs = model.predict(image)