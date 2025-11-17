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

This project delivers a fully modular and reproducible  
**⚙️ Machine Learning Pipeline** powered by **DVC**, **MLflow**, and **DagsHub**,  
designed to train a **🌲 Random Forest Classifier** on the  
**🩺 Pima Indians Diabetes Dataset**.

The pipeline consists of **three core stages**, each visually represented below:

📥 RAW DATA
│
▼
🧹 PREPROCESSING ──► 📄 CLEAN DATA
│
▼
🤖 TRAINING ──► 🎯 TRAINED MODEL
│
▼
📊 EVALUATION ──► 📈 METRICS + REPORTS (MLflow)

---

### 🔹 **🧹 Preprocessing**  
`preprocess.py`  
- Loads raw dataset  
- Applies cleaning & formatting  
- Saves consistent output to `data/processed/`  
- Ensures every run uses identical processed data  

✔ Powered by: **DVC Data Versioning**  
✔ Output: `data/processed/data.csv`  

---

### 🔹 **🤖 Training**  
`train.py`  
- Trains Random Forest model with Grid Search  
- Logs everything to MLflow:  
  - 📈 Accuracy  
  - ⚙️ Hyperparameters (`n_estimators`, `max_depth`, etc.)  
  - 📊 Confusion Matrix  
  - 🧾 Classification Report  
  - 📦 Trained Model Artifact  

✔ Model versioned with **DVC**  
✔ Metrics + Params tracked via **MLflow**  

---

### 🔹 **📊 Evaluation**  
`evaluate.py`  
- Loads trained model  
- Evaluates accuracy on test data  
- Logs final performance metrics & reports to MLflow  

✔ Enables easy experiment comparison  
✔ Fully reproducible evaluation  

---

## 🎯 Why This Pipeline?

### ✔ **Reproducibility**  
📦 **DVC** ensures any change in data/code/parameters reruns only the necessary stages — guaranteeing identical results across environments.

### ✔ **Experimentation**  
📘 **MLflow** makes it effortless to compare:  
- Runs  
- Hyperparameters  
- Metrics  
- Models  

### ✔ **Collaboration**  
☁️ **DagsHub** + Git + DVC + MLflow =  
A complete cloud-hosted collaborative MLOps workspace.

### ✔ **Research & Team Use**  
Ideal for:  
- ML research workflows  
- Data science teams  
- Reproducible MLOps education  
- Model lifecycle management  

---

## 🛠 Tech Stack

| Icon | Tool | Purpose |
|------|------|---------|
| 🐍 | Python | Core ML logic |
| 📦 | DVC | Dataset & model versioning |
| 📘 | MLflow | Experiment tracking |
| ☁️ | DagsHub | Remote DVC + MLflow hosting |
| 🌲 | RandomForest | Machine learning model |
| 🔢 | Scikit-learn | ML algorithms & evaluation |

---

## 🧩 DVC Pipeline Stage Creation (Reference)

```bash
# Preprocessing Stage
dvc stage add -n preprocess \
    -p preprocess.input,preprocess.output \
    -d src/preprocess.py -d data/raw/data.csv \
    -o data/processed/data.csv \
    python src/preprocess.py

# Training Stage
dvc stage add -n train \
    -p train.data,train.model,train.random_state,train.n_estimators,train.max_depth \
    -d src/train.py -d data/raw/data.csv \
    -o models/model.pkl \
    python src/train.py

# Evaluation Stage
dvc stage add -n evaluate \
    -d src/evaluate.py -d models/model.pkl -d data/raw/data.csv \
    python src/evaluate.py
