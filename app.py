import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression


st.title("Watch your sugar Mommy")
st.markdown("Predicting risk for gestational diabetes")
    
# @st.cache()
# def accept_user_data():
age = st.slider("Enter your age: ", 15, 43)
ethnicity = st.slider("Ethnicity (0-White, 1-Others)", 0,1)
bp = st.slider('Diastolic Blood Pressure', 50, 100)
Gestational_age= st.slider('Current gestational age: ')
Pregnancies = st.slider('Pregnancy number', 1, 10)
Fasting_Glucose=st.slider('Fasting Glucose', 60, 120)
Pregestational_BMI=st.slider('Pregestational BMI',15, 60)   
user_prediction_data = np.array([age,ethnicity,bp, Gestational_age, Pregnancies, Fasting_Glucose, Pregestational_BMI]).reshape(1,-1)
# return user_prediction_data 
# user_prediction_data =[age,bp, Gestational_age, Pregnancies, Fasting_Glucose, Pregestational_BMI]
# st.write ("Values you have entered:")
# st.write (f"age:{type(age)}")
# st.write (f"ethnicity:{type(ethnicity)}")
# st.write (f"bp:{type(bp)}")
# st.write (f"Gestational_age:{type(Gestational_age)}")
# st.write (f"Pregnancies:{type(Pregnancies)}")
# st.write (f"Fasting_Glucose:{type(Fasting_Glucose)}")
# st.write (f"Pregestational_BMI:{type(Pregestational_BMI)}")
# st.write (f"Combined data is:")

# st.write(user_prediction_data) 
# st.write(f"It is a {type(user_prediction_data)}") 


# # def accept_user_data():
# age = st.number_input("Enter your age: ")
# ethnicity = st.number_input("Ethnicity (0-White, 1-Others)", 0,1)
# bp = st.number_input('Blood Pressure', 50, 100)
# Gestational_age= st.number_input('Current gestational age: ')
# Pregnancies = st.number_input('Pregnancy number', 1, 10)
# Fasting_Glucose=st.number_input('Fasting Glucose', 60, 120)
# Pregestational_BMI=st.number_input('Pregestational BMI',15, 60)   
# user_prediction_data = np.array([age,ethnicity,bp, Gestational_age, Pregnancies, Fasting_Glucose, Pregestational_BMI]).reshape(1,-1)
# # return user_prediction_data 
# st.write(user_prediction_data) 
#     ethnicity = st.slider("Ethnicity (0-White, 1-Others)", 0,1)
#     bp = st.slider('Blood Pressure', 50, 100)
#     Gestational_age= st.slider('Current gestational age: ')
#     Pregnancies = st.slider('Pregnancy number', 1, 10)
#     Fasting_Glucose=st.slider('Fasting Glucose', 60, 120)
#     Pregestational_BMI=st.slider('Pregestational BMI',15, 60)   
#     user_prediction_data = np.array([age,ethnicity,bp, Gestational_age, Pregnancies, Fasting_Glucose, Pregestational_BMI]).reshape(1,-1)
#     return user_prediction_data 
#     st.write(user_prediction_data)   

# accept_user_data()

# def predict_model(bestmodelpath):
#     model = pickle.load(open(bestmodelpath, 'rb'))
#     data = accept_user_data()
#     result=model.predict_proba(data)
#     result_percent=np.round(result[0,1]*100,2)
#     st.title("Predictions")
#     if int(result_percent)>=65:
#             prediction='High Risk for Gestational Diabetes'        
#     elif int(result_percent)>=40:
#             prediction='Moderate Risk for Gestational Diabetes'    
#     else:
#             prediction='Low Risk for Gestational Diabetes'
clicked= st.button("Predict")

if clicked:
    
    # model = model.pkl    
    loaded_model=pickle.load(open('models/model.pkl', 'rb'))
    st.write("Model loaded")
    st.write("Predicting...")
# data = accept_user_data()
    result=loaded_model.predict_proba(user_prediction_data)
    st.write("Predictions done computing result")
    
    result_percent=np.round(result[0,1]*100,2)
    st.title("Predictions")
    if int(result_percent)>=65:
        prediction='High Risk for Gestational Diabetes'        
    elif int(result_percent)>=40:
        prediction='Moderate Risk for Gestational Diabetes'    
    else:
        prediction='You are healthy'
    st.write(prediction)
# model = "model.pkl"           
# def main():
#     if st.button("Predict"):
#         prediction=predict_model(model)
#         st.success(prediction)

# if __name__ == '__main__':
# 	main()

