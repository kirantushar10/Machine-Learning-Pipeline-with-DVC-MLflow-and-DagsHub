# 🧠 Machine Learning Pipeline with DVC, MLflow & DagsHub

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python" />
  <img src="https://img.shields.io/badge/DVC-Enabled-purple?logo=dvc" />
  <img src="https://img.shields.io/badge/MLflow-Tracking-orange?logo=mlflow" />
  <img src="https://img.shields.io/badge/DagsHub-Connected-yellow" />
  <img src="https://img.shields.io/badge/Scikit--Learn-RandomForest-green?logo=scikit-learn" />
</p>

<p align="center">
  <img height="140" src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/python.svg" />
  <img height="140" src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/dvc.svg" />
  <img height="140" src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/mlflow.svg" />
  <img height="140" src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/github.svg" />
</p>

---

## 🎨 Overview

Welcome to a fully reproducible **Machine Learning Pipeline** integrating real-world **MLOps tools**:

         ┌───────────────────────────┐
         │     Data Preprocessing     │
         └─────────────┬─────────────┘
                       ▼
         ┌───────────────────────────┐
         │     Model Training         │
         │  (Hyperparameter Tuning)   │
         └─────────────┬─────────────┘
                       ▼
         ┌───────────────────────────┐
         │       Evaluation           │
         └───────────────────────────┘

🔹 **DVC** handles dataset + model versioning  
🔹 **MLflow** reports metrics, params, artifacts  
🔹 **DagsHub** integrates remote data + experiment UI  
🔹 **Scikit-learn** provides the ML model  
🔹 **Git** manages code versioning  

Clean. Reproducible. Collaborative.

---

# 📝 Project Summary

This project demonstrates how to build an end-to-end Machine Learning workflow using **DVC** for versioning and **MLflow** for experiment tracking.  
A **Random Forest Classifier** is trained on the **Pima Indians Diabetes Dataset**, with the pipeline organized into clear stages:

### 🔧 Preprocessing  
Runs `preprocess.py` → loads raw CSV → outputs a clean processed dataset.  
Ensures consistent data for every ML run.

### 🤖 Training  
`train.py` handles:
- Grid Search hyperparameter tuning  
- Random Forest model training  
- MLflow logging for metrics & artifacts  
- DVC model versioning  

### 📊 Evaluation  
`evaluate.py`:
- Loads the trained model  
- Computes accuracy  
- Logs evaluation metrics & reports to MLflow  

### 🎯 Why this setup?
- ✔ Reproducible experiments  
- ✔ Structured pipeline with automated stage execution  
- ✔ Easy experiment comparison  
- ✔ Perfect for research, teaching, or team collaboration  

---

# 📁 Project Structure

