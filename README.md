
# SweetExpectations
### Predicting gestational dibetes for timely intervention: 
Application link: [SweetExpectations](https://sweet-expectations.herokuapp.com/) 

## Content
[Summary](#Summary)
[Data](#Data)
[EDA](#EDA)
[Features](#Features)
[Training](#Training)
[Validation](#Validation)
[App](#App)
[Challenges](#Challenges)
[Installations](#Installations)
[How-to-run](#How-to-run)

## Summary:
The aim of this project is to build a web application that can be used to predict/monitor the risk for gestational diabetes in expectant women much before their Oral Glucose Tolerance Test is due(around week 26-28).Early prediction promote early lifestyle interventions which essentially translates to an estimated saving of $5800 per pregnancy per an estimate by The American Diabetes Association in 2017.

## Data:
Electronic Health Records of expecting women was pulled in from [Physionet](https://www.physionet.org/content/maternal-visceral-adipose/1.0.0/).The database is from a cohort study of pregnant women up to 20 weeks of pregnancy and followed until delivery.Total records is 133. Inclusion criteria were singleton pregnancy and gestational age ≤20 weeks.
        ![Pipeline](https://github.com/Harmeet2504/Insight_Health/blob/master/reports/figures/pipeline.jpg)
## EDA:
Data was cleaned using pandas, and explored using matplotlib, seaborn visualization libraries. The data is non-linear and has 13 features and 1 target (gestational diabetes mellitus (gdm)), with imbalanced class (14% positive and 86% negative). Positive classes tend to be obese with high first fasting glucose. 

## Features:
Features that did not meet inclusion criteria (type of delivery, gestational age at delivery, child birth weight at delivery) and had no signal (previous diabetes) were eliminated from the study. Recursive feature elimination with cross-validation suggested 8 features for optimum accuracy. 'Ethnicity' had the least feature importance. Furthermore, redundancy was eliminated by exclusion of highly correlated features (mean diastolic bp, mean systolic bp, armenalli fat) without impacting the overall model performance. Final feature vector was composed of 5 features (Fasting blood glucose (mg/dl), BMI Pregestational, Age, Pregnancies (number), Gestational age).

## Training:
Data was stratified before splitting to training(80%) and test(20%) set using sklearn. Resampling was implemented on the training set to match the minority with majority class. Random forest classifier was formulated and tuned for its hyperparameters using 3-fold cross-validation by leveraging randomized search algorithm.

## Validation:
Model was optimized to eliminate both false positive and false negative outcomes because in either case any interventions would affect the life of both mother and the child. Hence, evaluation criteria was a trade-off of sensitivity and specificity. Model had an F1-score of 95%, Recall of 100%, Precision of 93% and AUC-score of 99.8%. All the parameters were better than the baseline model by 50%.
                ![Validation](https://github.com/Harmeet2504/Insight_Health/blob/master/reports/figures/evaluation_comparison.png)

## App:
The app was built using Flask api, designed with HTML, CSS and Bootstrap and deployed on Heroku. 

## Challenges
1. Small sample size: Feature space was reduced to build a generalizable model.Random Forest Classifier is a robust algorithm that works on the principle of bagging and eliminates overfitting by lowering variance.
2. Imbalanced classes: The best way around was to oversample the minority class to match majority class in the training set.

## Installations
pip install -r requirements.txt

## How-to-run 
1. Clone the repository 
2. Set up the environment variables
3. In the terminal run 'python app.py' from root directory

