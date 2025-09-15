from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import cv2

app = Flask(__name__)
model = load_model('brain_tumor_model.h5')

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Load and preprocess image
    img = image.load_img(file_path, target_size=(64, 64))  
    img_array = image.img_to_array(img)
    img_array = cv2.warpAffine(cv2.cvtColor(np.clip(cv2.cvtColor(img_array, cv2.COLOR_BGR2HSV).astype("float32") * 
                                                          [1,1,1.3], 0, 255).astype("uint8"), cv2.COLOR_HSV2BGR),
                                     cv2.getRotationMatrix2D((64//2, 64//2), 10, 1.0), 
                                     (64, 64))
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Predict
    prediction = model.predict(img_array)
    class_names = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']
    predicted_class = class_names[np.argmax(prediction)]

    # Pass the relative path for display
    return render_template('index.html', prediction=predicted_class, image_filename='uploads/' + file.filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
