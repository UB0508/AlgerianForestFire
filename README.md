README
Project: Flask app for model inference and example datasets/notebooks.

Overview
This repository hosts a small Flask application (application.py) that loads pre-trained models from the models folder and serves a web UI from templates. Example datasets are in dataset and exploratory notebooks are in notebooks.

Key symbols in the app:

application.app — the Flask application instance (application.py)
application.ridge_model — loaded Ridge model (application.py)
application.standard_scaler — loaded scaler used for preprocessing (application.py)
application.index — index route that renders index.html (application.py)
application.predict — prediction route that handles POST/GET for inference (application.py)
Files
.DS_Store
application.py
requirements.txt
dataset/

Algerian_forest_fires_dataset_UPDATE_cleaned.csv
Algerian_forest_fires_dataset_UPDATE.csv
height-weight.csv
models/

elastic_net_cv_model.pkl
lasso_cv_model.pkl
model.pkl
ridge_cv_model.pkl
scaler_algerian_forest.pkl
scaler.pkl
notebooks/

.DS_Store
feature-engineering.ipynb
model_training.ipynb
[notebooks/mulit-linear regression.ipynb](notebooks/mulit-linear regression.ipynb)
[notebooks/simple-linear regression.ipynb](notebooks/simple-linear regression.ipynb)
templates/

home.html
index.html
Setup
Install dependencies:

pip install -r requirements.txt

Run (development)
Set the Flask app and start the dev server:

export FLASK_APP=application.py
export FLASK_ENV=development
flask run

Or on Windows (PowerShell):
$env:FLASK_APP = 'application.py'
$env:FLASK_ENV = 'development'
flask run

Open http://127.0.0.1:5000/ to access the UI served by application.index which renders index.html.

Usage
Visit the web UI at / to use the form (front-end in templates/index.html).
The inference endpoint is application.predict at /predict. The endpoint uses application.standard_scaler and models like application.ridge_model loaded from models.
Notes
Models and scalers are stored as pickle files under models. Ensure these files are present and compatible with the versions of scikit-learn listed in requirements.txt.
Example datasets and notebooks are provided for exploration and retraining.
