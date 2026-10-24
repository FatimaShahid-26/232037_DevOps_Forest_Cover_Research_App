# Forest Cover Type Classification — Research Application

A full-stack machine learning application developed as part of a DevOps laboratory project. This project implements an existing research study on forest cover type classification using four machine learning algorithms, without proposing a novel model or methodology.

## Research Paper

**Title:** An Analysis of Machine Learning Techniques for Forest Cover Type Classification

**Authors:** E.B.R. Nagaesvara, M. Aadhithya, and A. Malini

**Publication:** 2023 6th International Conference on Contemporary Computing and Informatics (IC3I), IEEE

**DOI:** https://doi.org/10.1109/IC3I59117.2023.10397823

## Project Objective

The objective is to develop a software application that demonstrates the forest cover type classification workflow reproduced from the research paper.

The application allows users to enter geographical and environmental measurements, select a classification algorithm, and obtain a predicted forest cover type.

The project focuses on software engineering, model integration, automated testing, and CI/CD rather than introducing research novelty.

## Dataset

The project uses the US Forest Cover Type (Covertype) dataset, containing approximately 581,012 observations.

It includes environmental and geographical measurements such as elevation, slope, aspect, hydrology distances, road distances, hillshade, wilderness area, and soil type.

The original dataset contains 54 input features and 7 target classes.

The implemented notebook additionally creates 10 engineered features, resulting in 64 model features.

### Forest Cover Classes

| Class | Forest Cover Type |
|---|---|
| 1 | Spruce/Fir |
| 2 | Lodgepole Pine |
| 3 | Ponderosa Pine |
| 4 | Cottonwood/Willow |
| 5 | Aspen |
| 6 | Douglas-fir |
| 7 | Krummholz |

## Machine Learning Models

The following four classifiers are implemented:

1. Decision Tree
2. Random Forest
3. K-Nearest Neighbors (KNN)
4. XGBoost

The models are trained and evaluated in the Jupyter Notebook. Evaluation includes accuracy, precision, recall, F1-score, and AUC.

The trained models are packaged in `forest_bundle.joblib`, alongside the fitted preprocessing objects and feature schema.

KNN uses a fitted StandardScaler, while XGBoost uses a label encoder for its target classes.

## Technology Stack

| Component | Technology |
|---|---|
| Model development | Python, Jupyter Notebook, Google Colab |
| Machine learning | Scikit-learn, XGBoost |
| Backend API | Flask |
| Frontend | Angular |
| Testing | Pytest |
| Version control | Git and GitHub |
| CI/CD | GitHub Actions |
| Static deployment | GitHub Pages |

## System Architecture

```text
Angular Frontend
       |
       | HTTP POST /api/predict
       v
Flask REST API
       |
       v
Input Validation
       |
       v
Feature Engineering
       |
       v
Selected ML Model
       |
       v
Predicted Forest Cover Type
       |
       v
Angular Result Display
```

## Project Structure

```text
Forest_Cover_Research_App/
├── backend/
│   ├── app.py
│   ├── preprocessing.py
│   ├── requirements.txt
│   ├── test_pipeline.py
│   ├── test_api.py
│   ├── test_payload.json
│   ├── models/
│   │   └── forest_bundle.joblib
│   └── tests/
├── frontend/
│   ├── src/
│   ├── proxy.conf.json
│   ├── package.json
│   └── angular.json
├── notebooks/
├── data/
├── docs/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── pages.yml
├── .gitignore
└── README.md
```

The dataset and trained model bundle may be excluded from Git because of their size. They must be prepared locally before running live predictions.

## Running the Application Locally

### 1. Clone the repository

```bash
git clone https://github.com/FatimaShahid-26/232037_DevOps_Forest_Cover_Research_App.git
cd 232037_DevOps_Forest_Cover_Research_App
```

### 2. Create and activate a Python virtual environment

For Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install backend dependencies

```powershell
python -m pip install -r backend\requirements.txt
```

Use library versions compatible with the environment in which the models were trained.

### 4. Prepare the trained model

Place the trusted, trained `forest_bundle.joblib` file inside:

`backend/models/`

If the file is unavailable, reproduce the training notebook and export the models, scaler, encoder, and feature schema.

### 5. Start the Flask backend

From the project root:

```powershell
python backend\app.py
```

Flask runs locally at:

`http://127.0.0.1:5000`

### 6. Start the Angular frontend

Open a second terminal:

```powershell
cd frontend
npm ci
npx ng serve --proxy-config proxy.conf.json
```

Open:

`http://localhost:4200`

The local Angular application communicates with the Flask API to generate predictions.

## Testing

### Run preprocessing tests

```powershell
python -m pytest -q backend\tests
```

### Test direct machine learning inference

```powershell
python backend\test_pipeline.py
```

### Test the Flask prediction API

Start Flask first, then run:

```powershell
python backend\test_api.py
```

The preprocessing tests can run without the trained model bundle. Model inference and prediction API tests require the exported artifacts.

## Continuous Integration and Deployment

GitHub Actions automates:

- Python dependency installation
- Backend preprocessing tests
- Angular production builds
- GitHub Pages frontend deployment

The CI workflow verifies preprocessing tests and frontend compilation. The fitted model inference tests are performed locally unless model artifacts are also made available to CI.

## GitHub Repository

https://github.com/FatimaShahid-26/232037_DevOps_Forest_Cover_Research_App

## Live Frontend

https://fatimashahid-26.github.io/232037_DevOps_Forest_Cover_Research_App/

**Deployment limitation:** GitHub Pages hosts only the static Angular frontend. It does not execute Flask or Python machine learning models. To perform live predictions, run the application locally with its Flask backend.

## Research Scope and Limitations

This project is a software implementation of an existing forest cover classification study. It does not introduce a new machine learning algorithm, new dataset, or original research contribution.

The implemented notebook follows the classification objective and algorithms of the reference paper, but its experimental configuration and feature engineering may differ from those reported by the authors. Exact numerical reproduction of the published results is not claimed.

The models are trained on US forest cover data. Predictions should not be treated as validated classifications for other geographical regions without appropriate evaluation.

The application is intended for research reproduction, education, and DevOps laboratory demonstration, not operational forestry decisions.

## Academic Attribution

This project is based on:

E.B.R. Nagaesvara, M. Aadhithya, and A. Malini, *An Analysis of Machine Learning Techniques for Forest Cover Type Classification*, IEEE IC3I, 2023.

The research methodology and machine learning algorithms are attributed to the original study.

The full-stack application demonstrates the integration and deployment of the reproduced models using established software engineering practices.