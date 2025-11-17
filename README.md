# 🧠 Machine Learning Pipeline with DVC, MLflow & DagsHub

A complete end-to-end **MLOps workflow** for reproducible machine learning using  
**DVC**, **MLflow**, **DagsHub**, **Git**, and **Scikit-learn**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python" />
  <img src="https://img.shields.io/badge/DVC-Enabled-purple?logo=dvc" />
  <img src="https://img.shields.io/badge/MLflow-Tracking-orange?logo=mlflow" />
  <img src="https://img.shields.io/badge/DagsHub-Integrated-yellow" />
  <img src="https://img.shields.io/badge/Scikit--Learn-RandomForest-green?logo=scikit-learn" />
</p>

---

## 📝 Project Summary

This project demonstrates how to build a complete **end-to-end Machine Learning pipeline** using:

- **DVC** → Dataset & model versioning  
- **MLflow** → Experiment tracking  
- **DagsHub** → Remote storage + hosted MLflow  
- **Scikit-learn** → RandomForest Classifier  
- **Git** → Code version control  

The pipeline trains a **Random Forest Classifier** on the **Pima Indians Diabetes Dataset** with clear modular stages:

### 🔹 Preprocessing
Runs `preprocess.py` to load raw data and output a cleaned version to `data/processed/`.  
Ensures consistent preprocessing across all runs.

### 🔹 Training
`train.py` performs:
- Hyperparameter tuning  
- Model training  
- MLflow logging (metrics, parameters, artifacts)  
- Saves model via DVC (`model.pkl.dvc`)

### 🔹 Evaluation
`evaluate.py`:
- Loads the trained model  
- Computes accuracy  
- Logs evaluation metrics & reports to MLflow  

### 🎯 Why this pipeline?
- **Reproducibility:** DVC ensures reliable dataset and model version control.  
- **Experimentation:** MLflow enables easy comparison of runs and hyperparameters.  
- **Collaboration:** Git + DVC + DagsHub enable seamless teamwork.  
- **Research-friendly:** Ideal for experimenting, teaching MLOps, or team ML workflows.

### 🧪 Use Cases
- ML research experiments  
- Data science team collaboration  
- Reproducible end-to-end ML prototypes  
- MLOps pipeline learning and deployment  

---

## 📂 Project Structure

