import pandas as pd
import pickle
import mlflow
import yaml
from sklearn.metrics import accuracy_score
import os

os.environ['MLFLOW_TRACKING_URI'] = "https://dagshub.com/<username>/<repo>.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME'] = "<your-username>"
os.environ['MLFLOW_TRACKING_PASSWORD'] = "<your-token>"

## LOAD PARAMETERS FROM YAML

params = yaml.safe_load(open("params.yaml"))["train"]

def evaluate(data_path,model_path):
    data = pd.read_csv(data_path)

    X=data.drop(columns=["Outcome"])
    y=data["Outcome"]

    mlflow.set_tracking_uri("https://dagshub.com/kirantushar10/MachineLearningPipeline.mlflow")

    ## LOAD THE MODEL FROM THE DISK

    model = pickle.load(open(model_path,'rb'))

    predictions = model.predict(X)
    accuracy = accuracy_score(y,predictions)

    ## LOG THE METRICS
    mlflow.log_metric("Accuracy",accuracy)
    print(f"Model Accuracy:{accuracy}")

if __name__=="__main__":
    evaluate(params["data"],params['model'])


