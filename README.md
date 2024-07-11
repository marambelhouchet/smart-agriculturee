# Smart Agriculture Project

This project focuses on utilizing artificial intelligence to aid farmers by providing soil classification and plant disease detection based on images. The solution includes a backend, frontend, and API integration to make it accessible and user-friendly.

## Project Structure

- **Backend**: Handles the AI models and predictions.
- **Frontend**: User interface for farmers to upload images.
- **API**: Connects the frontend and backend, enabling communication between them.

## Features

1. **Soil Classification**:
   - Classifies soil images into categories like Alluvial soil, Black soil, Clay soil, and Red soil.
   - Provides recommendations on the best crops to plant based on soil type.

2. **Plant Disease Detection**:
   - Detects plant diseases from images.
   - Currently supports detection of Blight, Common Rust, Gray Leaf Spot, and Healthy plants.
   - Offers suggestions for treating the detected plant diseases.

## Installation

To set up the project, follow these steps:

### Backend Setup

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/marambelhouchet/smart-agriculture-project.git
   cd smart-agriculture-project
2. **Install Dependencies**:
   pip install -r requirements.txt
3. **Place Your Models**:
  Ensure your trained models (soil_classification_model.h5 and plant_disease_model.h5) are in the project directory.
4. **Run the Backend Server**:
   python backend.py
### Frontend Setup
1. **Navigate to the Frontend Directory**:
   cd frontend
2. **Install Frontend Dependencies**:
   npm install
3. **Run the Frontend Server**:
   npm start
### Usage
1. **Soil Classification**:

Upload an image of the soil.
Get the predicted soil type and recommended crops.
2. **Mais plants Disease Detection**:

Upload an image of a mais leaf.
Get the predicted disease and suggested treatment.
### Contributing
Contributions are welcome! Please create an issue or a pull request if you have any ideas for improvements or new features.
   
