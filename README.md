# 🧠 Brain Tumor Classification using CNN

This project implements a **Convolutional Neural Network (CNN)** to classify brain tumors from MRI images into four categories: **Glioma, Meningioma, Pituitary, and No Tumor**.  
The model was trained, evaluated, and deployed (AWS EC2), demonstrating its potential to assist radiologists in early detection and diagnosis.

---

## 📌 Project Overview
- **Objective**: Develop a deep learning model to classify brain tumors from MRI scans.  
- **Dataset**: Can collect the MRI images from Kaggle (multiple files).  
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

## 📊 Results
Training Accuracy vs Validation Accuracy
Model achieved ~97% accuracy after 14 epochs.
Loss decreased steadily, showing good generalization.

## 📚 Future Work
Improve performance using Transfer Learning (ResNet, VGG16).
Deploy model on Streamlit or FastAPI for an interactive demo.
Integrate Grad-CAM for model explainability.
Host dataset preprocessing and model training in Google Colab/Kaggle for reproducibility.

## 🙌 Acknowledgments
Dataset contributors
TensorFlow & Keras documentation
AWS EC2 free tier (deployment)


## 📧  Contact

👤 Amaljith P
📩 syamaism@gmail.com
🌐 https://www.linkedin.com/in/amaljith-p-b8044b248/

