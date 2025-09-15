# 🧠 Brain Tumor Classification using CNN

This project implements a **Convolutional Neural Network (CNN)** to classify brain tumors from MRI images into four categories: **Glioma, Meningioma, Pituitary, and No Tumor**.  
The model was trained, evaluated, and deployed (AWS EC2), demonstrating its potential to assist radiologists in early detection and diagnosis.

---

## 📌 Project Overview
- **Objective**: Develop a deep learning model to classify brain tumors from MRI scans.  
- **Dataset**: Publicly available MRI brain tumor dataset.  
- **Classes**:
  - Glioma  
  - Meningioma  
  - Pituitary  
  - No Tumor  
- **Deployment**: Model was deployed on **AWS EC2 instance** with Flask for testing (currently inactive due to cost).  

---

## ⚙️ Features
- Preprocessing of MRI images with **OpenCV & NumPy**  
- CNN model built using **Keras & TensorFlow**  
- Visualizations of training accuracy and loss  
- Model saved in `.h5` format for reuse  
- AWS deployment (Flask + EC2) for real-time predictions  

---

## 🛠️ Technologies Used
- Python  
- TensorFlow / Keras  
- OpenCV  
- NumPy, Pandas  
- Matplotlib, Seaborn  
- AWS EC2 (deployment)  

---

## 📂 Project Structure




---

## 🚀 How to Run the Project

### 🔹 1. Clone the repository
```bash
git clone https://github.com/your-username/brain-tumor-classification.git
cd brain-tumor-classification




🔹 2. Install dependencies
pip install -r requirements.txt


🔹 3. Train the Model
jupyter notebook Brain_Tumor_Classification.ipynb


🔹 4. Run the Flask App (Deployment)
python app.py

Then open http://127.0.0.1:5000/ in your browser

📊 Results
Training Accuracy vs Validation Accuracy
Model achieved ~97% accuracy after 14 epochs.
Loss decreased steadily, showing good generalization.

📚 Future Work
Improve performance using Transfer Learning (ResNet, VGG16).
Deploy model on Streamlit or FastAPI for an interactive demo.
Integrate Grad-CAM for model explainability.
Host dataset preprocessing and model training in Google Colab/Kaggle for reproducibility.

🙌 Acknowledgments
Dataset contributors
TensorFlow & Keras documentation
AWS EC2 free tier (deployment)


# 📧  Contact

👤 Amaljith P
📩 syamaism@gmail.com
🌐 https://www.linkedin.com/in/amaljith-p-b8044b248/

