
# SweetExpectations
### Predicting gestational dibetes for timely intervention: 
Application link: [SweetExpectations](https://sweet-expectations.herokuapp.com/) 

## Summary:
The aim of this project is to build a web application that expectant women can use to predict/monitor the risk for gestational diabetes much before their Oral Glucose Tolerance Test is due(around week 26-28).Early prediction would enable early lifestyle interventions which essentially translates to an estimated saving of $5800 per pregnancy as per an estimate of American Diabetes Association in 2017.

## Data Extraction, Transformation and Loading

**Data Source:** 
Electronic Health Records of expecting women was obtained from [Physionet](https://www.physionet.org/content/maternal-visceral-adipose/1.0.0/).The database is from a cohort study of pregnant women up to 20 weeks of pregnancy and followed until delivery. Of the 154 women selected initially, 21 (13%) were lost to follow-up, resulting in a final sample of 133 women. The inclusion criteria were singleton pregnancy and gestational age ≤20 weeks. The exclusion criteria was pre-existing type 1 or 2 diabetes mellitus.

**Exploratory Data Analysis:**
Data was cleaned in pandas, and explored using matplotlib, seaborn visualization libraries. The data has 13 features and 1 target (gestational diabetes mellitus (gdm)), with imbalanced class (14% positive and 86% negative). 

## Feature Selection:
Features that did not meet inclusion criteria (type of delivery, gestational age at delivery, child birth weight at delivery) and had no signal (previous diabetes) were dropped. Recursive feature elimination with cross-validation suggested 8 features for optimum accuracy. 'Ethnicity' had the least feature importance. Furthermore, redundancy was eliminated by exclusion of highly correlated features (mean diastolic bp, mean systolic bp, armenalli fat) without impacting the overall model performance. Final feature vector was composed of 5 features (Fasting blood glucose (mg/dl), BMI Pregestational, Age, Pregnancies (number), Gestational age).

## Data Splitting:

## Resampling minority class:

## Training the model:

## Tuning hyperparameters

## Model validation

## Installations
pip install -r requirements.txt

## To run locally
1. Clone the repository 
2. setup the environment variables (or comment out the DB parameters).
3. python app.py

