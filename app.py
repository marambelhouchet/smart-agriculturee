from flask import Flask, request, jsonify, render_template, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)

# Load models
soil_model = load_model('soil_classification_model.h5')
plant_model = load_model('plant_disease_model.h5')

# Define class indices
soil_class_indices = {
    0: 'Alluvial soil',
    1: 'Black Soil',
    2: 'Clay soil',
    3: 'Red soil'
}

plant_class_indices = {
    0: 'Blight',
    1: 'Common Rust',
    2: 'Gray Leaf Spot',
    3: 'Healthy'
}

# Function to preprocess images
def preprocess_image(image_path, target_size):
    image = load_img(image_path, target_size=target_size)
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_soil', methods=['POST'])
def predict_soil():
    image_file = request.files['image']
    image_path = "./temp.jpg"
    image_file.save(image_path)
    image = preprocess_image(image_path, (224, 224))
    predictions = soil_model.predict(image)
    predicted_class = np.argmax(predictions, axis=1)
    return jsonify({'class': soil_class_indices[int(predicted_class)]})

@app.route('/predict_plant', methods=['POST'])
def predict_plant():
    image_file = request.files['image']
    image_path = "./temp.jpg"
    image_file.save(image_path)
    image = preprocess_image(image_path, (224, 224))
    predictions = plant_model.predict(image)
    predicted_class = np.argmax(predictions, axis=1)
    return jsonify({'class': plant_class_indices[int(predicted_class)]})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
