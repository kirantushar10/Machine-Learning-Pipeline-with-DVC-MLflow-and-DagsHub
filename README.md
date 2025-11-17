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

## 📝 Project Summary

This project implements a fully reproducible **⚙️ Machine Learning Pipeline** using  
**📦 DVC**, **📘 MLflow**, **☁️ DagsHub**, and **🐍 Python** to train a  
**🌲 Random Forest Classifier** on the **🩺 Pima Indians Diabetes dataset**.

It follows a real MLOps workflow with clearly separated, version-controlled stages:

---

# 📐 Pipeline Architecture (ASCII Graphic)

┌─────────────────────────────────────────────────────┐
│ 📥 RAW DATA │
└───────────────▲─────────────────────────────────────┘
│
│ 1️⃣ Preprocessing (DVC Stage)
│
┌───────────────┴─────────────────────────────────────┐
│ 🧹 CLEAN / PROCESSED DATA │
└───────────────▲─────────────────────────────────────┘
│
│ 2️⃣ Training (MLflow + DVC Stage)
│
┌───────────────┴─────────────────────────────────────┐
│ 🤖 TRAINED MODEL │
│ (versioned using DVC, logged using MLflow) │
└───────────────▲─────────────────────────────────────┘
│
│ 3️⃣ Evaluation (MLflow Stage)
│
┌───────────────┴─────────────────────────────────────┐
│ 📊 METRICS & REPORTS │
│ (Accuracy, Confusion Matrix, Classification Report) │
└──────────────────────────────────────────────────────┘
