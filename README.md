
# SafePregnancy : 
A streamlit web application for early prediction of gestational diabetes in expectant women.
Application link: [SafePregnancy](https://watch-sugar-mommy.herokuapp.com/) 

## Summary:
The aim of this project is to build a web application that expectant women can use to predict/monitor the risk for gestational diabetes much before their Oral Glucose Tolerance Test is due(around week 26-28).Early prediction would enable early lifestyle interventions which essentially translates to an estimated saving of $3800 per pregnancy.
## Data Extraction, Transformation and Loading
**Data Source:** 
Electronic Health Records of expecting women was obtained from [Physionet](https://www.physionet.org/content/maternal-visceral-adipose/1.0.0/).The database is from a cohort study of pregnant women up to 20 weeks of pregnancy and followed until delivery. Of the 154 women selected initially, 21 (13%) were lost to follow-up, resulting in a final sample of 133 women. The inclusion criteria were singleton pregnancy and gestational age ≤20 weeks. The exclusion criteria was pre-existing type 1 or 2 diabetes mellitus.The data had 13 features and 1 target, with imbalanced positive class.


## Installations
pip install -r requirements.txt

## To run locally
1. Clone the repository 
2. setup the environment variables (or comment out the DB parameters).
3. streamlit run app.py

