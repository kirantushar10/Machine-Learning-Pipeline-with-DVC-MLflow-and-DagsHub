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

<!-- ============================================== -->
<!--                PROJECT SUMMARY                 -->
<!-- ============================================== -->

<h2 align="center">📝 Project Summary</h2>

<p align="center">
This project delivers a complete <b>MLOps-driven Machine Learning Pipeline</b> using
<b>📦 DVC</b>, <b>📘 MLflow</b>, <b>☁️ DagsHub</b>, and <b>🐍 Python</b>.
It trains a <b>🌲 Random Forest Classifier</b> on the
<b>🩺 Pima Indians Diabetes Dataset</b> with reproducible, version-controlled stages.
</p>

---

<h2 align="center">🔹 🧹 Preprocessing Stage 🔹</h2>

📄 **Script:** `src/preprocess.py`  
📦 **Versioned Using:** DVC  
💾 **Output:** `data/processed/data.csv`

### ✨ What This Stage Does:
- Loads raw CSV from `data/raw/`
- Cleans, formats & structures data
- Produces fully reproducible processed data

---

<h2 align="center">🔹 🤖 Training Stage 🔹</h2>

📄 **Script:** `src/train.py`  
📘 **Tracked using:** MLflow  
📦 **Model Versioning:** DVC  
🧠 **Algorithm:** Random Forest Classifier  

### ✨ What This Stage Does:
- Trains Random Forest model  
- Performs Grid Search hyperparameter tuning  
- Logs everything to MLflow:
  - 📈 Accuracy  
  - ⚙️ Hyperparameters  
  - 📊 Confusion Matrix  
  - 🧾 Classification Report  
  - 📦 Trained Model Artifact  

---

<h2 align="center">🔹 📊 Evaluation Stage 🔹</h2>

📄 **Script:** `src/evaluate.py`  
📘 **Tracked using:** MLflow  

### ✨ What This Stage Does:
- Loads trained model  
- Computes predictions  
- Logs evaluation metrics  
- Creates evaluation artifacts for comparison  

> 🟣 **Colorized Callout:**  
> Keeps the evaluation transparent, repeatable, and fully trackable across model versions.

---

<!-- ============================================== -->
<!--                  WHY THIS PIPELINE             -->
<!-- ============================================== -->

<h2 align="center">🎯 Why This Pipeline?</h2>

### ✔ 🔁 **Reproducibility**  
DVC guarantees identical results across environments by version-controlling:
- Data  
- Models  
- Parameters  
- Pipeline stages  

### ✔ 📈 **Experimentation**  
MLflow tracks:
- Metrics  
- Hyperparameters  
- Artifacts  
- Models  

➡️ Makes it easy to compare hundreds of experiments.

### ✔ 🤝 **Collaboration**  
DVC + MLflow + Git + DagsHub create a full cloud-ready MLOps stack.

### ✔ 🎓 **Research & Team Use**
Ideal for:
- Research workflows  
- Academic ML projects  
- DS team collaboration  
- MLOps learning & demos  

---

<!-- ============================================== -->
<!--                  TECH STACK                    -->
<!-- ============================================== -->

<h2 align="center">🛠 Tech Stack</h2>

| Icon | Technology | Purpose |
|------|------------|---------|
| 🐍 | Python | Main programming language |
| 🔢 | Scikit-learn | Model training & evaluation |
| 📦 | DVC | Data & model versioning |
| 📘 | MLflow | Experiment tracking |
| ☁️ | DagsHub | Remote storage + MLflow UI |
| 🐙 | Git | Code versioning |

---

<!-- ============================================== -->
<!--            DVC PIPELINE STAGE CREATION         -->
<!-- ============================================== -->

<h2 align="center">🧩 DVC Pipeline Stage Creation (Reference)</h2>

```bash
# 🧹 Preprocessing Stage
dvc stage add -n preprocess \
    -p preprocess.input,preprocess.output \
    -d src/preprocess.py -d data/raw/data.csv \
    -o data/processed/data.csv \
    python src/preprocess.py

# 🤖 Training Stage
dvc stage add -n train \
    -p train.data,train.model,train.random_state,train.n_estimators,train.max_depth \
    -d src/train.py -d data/raw/data.csv \
    -o models/model.pkl \
    python src/train.py

# 📊 Evaluation Stage
dvc stage add -n evaluate \
    -d src/evaluate.py -d models/model.pkl -d data/raw/data.csv \
    python src/evaluate.py
```

<!-- ====================== ⚙️ MLflow Configuration ====================== -->

## ⚙️ Configure MLflow (DagsHub Integration)

MLflow is configured to log metrics, models, and artifacts directly to **DagsHub’s hosted MLflow server**.

Add the following code snippet at the **top** of both:  
`src/train.py` and `src/evaluate.py`

```python
import os

# ====================================================
# 🔧 MLFLOW + DAGSHUB CONFIGURATION
# ====================================================
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/<your-username>/<your-repo>.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "<your-username>"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "<your-access-token>"
# ====================================================
