from flask import Flask, request, jsonify
from utils import *
from models import *

app = Flask(__name__)

# Define API endpoint for object detection
@app.route('/detect', methods=['POST'])
def detect():
    image = request.files['image']
    detections = yolo_v3.predict(preprocess_image(image))
    return jsonify(detections)

# Define API endpoint for object classification
@app.route('/classify', methods=['POST'])
def classify():
    image = request.files['image']
    classification = ssd.predict(preprocess_image(image))
    return jsonify(classification)

if __name__ == "__main__":
    app.run()
