import os
import sys
from utils import *
from models import *

# Initialize application
app = App()

# Load pre-trained models
yolo_v3 = load_yolo_v3()
ssd = load_ssd()

# Define detection function
def detect(image):
    # Preprocess image
    image = preprocess_image(image)
    
    # Run object detection
    detections = yolo_v3.predict(image)
    
    # Return detections
    return detections

# Define classification function
def classify(image):
    # Preprocess image
    image = preprocess_image(image)
    
    # Run object classification
    classification = ssd.predict(image)
    
    # Return classification
    return classification

# Run application
if __name__ == "__main__":
    app.run()
