# Proposed Research Novelty and Project Extension

## 1. Project Overview

The current project focuses on reproducing a forest cover type classification study using machine learning techniques. The initial implementation evaluates classification models and integrates the prediction functionality in a web application using a Flask backend and an Angular frontend. GitHub Actions and GitHub Pages are used to support automated project workflows and frontend deployment.

In the next phase, I will extend this research towards a Pakistan-focused forest classification framework, with particular attention to the country's diverse forest ecosystems and environmental conditions.

## 2. Identified Research Gap

Existing forest cover classification studies provide useful approaches for predicting forest cover categories from environmental and geographical features. However, models developed using datasets from other geographical regions may not perform equally well in Pakistan because of differences in climate, elevation, terrain, vegetation, and forest composition.

A further challenge is the availability of a consistent, regionally relevant dataset containing environmental features and forest-related labels suitable for supervised machine learning.

This project will investigate how a machine learning classification framework can be adapted to Pakistan using locally relevant geographical and environmental data.

## 3. Proposed Research Novelty

The proposed novelty is the development and evaluation of a Pakistan-focused forest classification framework using environmental and geospatial features derived from relevant satellite and geographical datasets.

The research will explore the following contributions:

### 3.1 Pakistan-Specific Environmental Dataset

A regionally relevant dataset might be constructed by integrating suitable environmental and geospatial information. Candidate features including elevation, slope, aspect, mean temperature, and total precipitation. I will try to obtain Forest-related labels from appropriate reference datasets.

The initial geographical focus may be Swat, Khyber Pakhtunkhwa, with the possibility of extending the study to additional regions depending on data availability and validation requirements.

### 3.2 Adaptation of Existing Classification Methods

The baseline classification workflow will be adapted to the selected Pakistani study area. Multiple machine learning algorithms will be evaluated using consistent preprocessing, data splitting, and evaluation procedures.

This will help determine whether the existing methodology can be applied effectively to the selected region and identify the adjustments required for local environmental conditions.

### 3.3 Comparative Model Evaluation

The study will compare candidate classification models using metrics such as accuracy, precision, recall, F1-score, and confusion matrices. Where appropriate, class-wise performance and macro-averaged metrics will be emphasized to investigate performance differences across forest categories.

The evaluation will also examine potential class imbalance, spatial dependence, and the limitations of the available reference labels.

### 3.4 Geospatial Feature Contribution Analysis

The study will investigate the contribution of environmental variables to classification performance. Feature importance or other suitable interpretation techniques will be used to identify which variables contribute most to the predictions.

This analysis may help explain how topographic and climatic conditions relate to the classification results within the selected study area. Feature importance will be interpreted as model-specific evidence rather than proof of causal relationships.

### 3.5 Integration into a Reproducible Application

The research workflow will be connected to the existing web application so that users can submit environmental feature values and view the model's predicted category and associated confidence or probability estimates, where supported.

The project will also maintain reproducible training and evaluation procedures and document the dataset sources, preprocessing decisions, model configurations, and limitations.

## 4. Research Questions

The proposed extension will investigate the following questions:

1. How effectively can machine learning models classify forest-related categories using environmental and geospatial features from a selected region of Pakistan?
2. Which evaluated model provides the strongest classification performance under a consistent evaluation protocol?
3. Which environmental and topographic variables contribute most to the model's classification decisions?
4. How do data quality, class imbalance, and spatial characteristics affect the reliability and generalizability of the predictions?

## 5. Proposed Methodology

The planned research will follow these stages:

1. **Study-area selection:** Define the geographical extent and classification objective for the Pakistani study area.
2. **Data collection:** Obtain suitable satellite-derived, climatic, topographic, and reference-label datasets.
3. **Dataset preparation:** Align spatial resolution and coordinate systems where necessary, handle missing values, define features, and validate class labels.
4. **Baseline reproduction:** Document and reproduce the reference methodology as closely as the available data and implementation details permit.
5. **Model training:** Train and compare selected machine learning algorithms using consistent experimental settings.
6. **Model evaluation:** Report overall and class-wise metrics, confusion matrices, and appropriate validation results.
7. **Feature analysis:** Investigate feature contributions and assess their consistency with the observed classification patterns.
8. **Application integration:** Connect the selected model to the Flask API and Angular interface.
9. **Documentation:** Record the experimental setup, data provenance, limitations, and findings in the repository.

Where spatially structured data are available, spatially separated validation will be considered to reduce the risk of overly optimistic results caused by nearby or overlapping samples appearing in both training and testing sets.

## 6. Expected Contributions

The expected outcomes are:

- A documented, Pakistan-focused dataset preparation and classification workflow.
- An empirical evaluation of selected machine learning algorithms on the chosen study area.
- An analysis of the contribution of environmental and topographic features.
- A reproducible implementation connecting model inference to a web-based interface.
- Evidence regarding the strengths and limitations of applying the selected classification methodology to the Pakistani context.

These contributions will be assessed through experiments rather than assumed in advance.

## 7. Scope and Limitations

The project will initially focus on the selected study area and the categories supported by the available reference data. The quality of the results will depend on the reliability, spatial resolution, temporal consistency, and representativeness of the input datasets.

A classification model trained on a limited geographical area will not automatically be considered valid for all forests in Pakistan. Broader generalization will require additional geographical coverage and independent validation.

Furthermore, environmental features alone may not distinguish all forest types reliably. The classification objective and reference labels must therefore be defined clearly before model performance is interpreted.

## 8. Novelty Status

The current implementation establishes the initial machine learning and application baseline. The Pakistan-specific dataset integration, regional evaluation, and feature contribution analysis constitute the proposed research extension and will be implemented and evaluated in subsequent stages.

The novelty claim will be refined after reviewing related literature and determining which aspects of the proposed approach have already been investigated in previous studies. The project will not claim to be the first of its kind without sufficient evidence from that review.

## 9. Conclusion

This proposed extension aims to move the project beyond a straightforward reproduction of an existing forest classification study by investigating the adaptation of machine learning methods to a geographically distinct and locally relevant setting in Pakistan.

The main research contribution will be established through the construction and documentation of an appropriate dataset, a rigorous comparative evaluation, analysis of environmental feature contributions, and transparent reporting of the resulting findings and limitations.