import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from PIL import Image
import webbrowser
image = Image.open('logo.png')

st.image(image,use_column_width=True)

total=100


if st.sidebar.button('Open browser', key='url_sub'):
                url = 'https://www.reddit.com/r/GestationalDiabetes/'
                webbrowser.open_new_tab(url)

# webbrowser.open(') 



def donut_plot(prediction, total):
    delta=total-prediction
    values = [prediction, delta]
    if prediction >=65:
        color=["brown", "grey"]
        label= ["High Risk", ""]
    elif prediction >=45:
        color=["orange", "grey"]
        label= ["Moderate Risk", ""]
    else:
        color=["green", "grey"]
        label= ["  Healthy", ""]
    #Convert the pie plot to donut plot
    values = [prediction, delta]
    plt.pie(values, labels=label, labeldistance=1.1, colors=color)
    centre_circle = plt.Circle((0,0),0.65,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

def bmi_calc(bmi):
    if bmi < 18.5:
        bmi_text="under weight"
    elif bmi >= 18.5 and bmi <= 24.9:
        bmi_text="normal weight"
    elif bmi >= 25 and bmi <= 29.9:
        bmi_text="Over weight"
    else: 
        bmi_text="Obese"
    return bmi_text

def sugar_calc(Fasting_Glucose):
    if Fasting_Glucose < 92:
        Fasting_Glucose_text="normal"
    elif Fasting_Glucose >= 92 and Fasting_Glucose <= 126:
        Fasting_Glucose_text="high"
    else:
        Fasting_Glucose_text="overt diabetic"
    return Fasting_Glucose_text

st.title("Towards a safer pregnancy")
# st.header("Predicting risk for gestational diabetes")
st.header('Enter your gestational age: ') 
Gestational_age= st.slider(" ", 1, 40)
if Gestational_age ==1:
    st.write("")
elif Gestational_age > 25:
    st.title("Visit your doctor for glucose tolerance test!!")
else:
    st.title("You are good to go.")
    st.write("Fill in your details below")

    # button= st.button("Go!")

# if button:
# @st.cache()
# def accept_user_data():
    age = st.number_input("Enter your age: ", 15, 50)
    height = st.number_input("Enter your height (ft): ", 3,7)
    weight = st.slider("Enter your weight (kg): ", 20,200)
    height_m = height * 0.304
    bmi=weight/(height_m)
    Pregnancies = st.slider('Pregnancy number', 1, 10)
    Fasting_Glucose=st.slider('Fasting Glucose', 60, 130)
    # Pregestational_BMI=st.slider('Pregestational BMI',15, 60)   
    user_prediction_data = np.array([age, Gestational_age, Pregnancies, Fasting_Glucose, bmi]).reshape(1,-1)
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



    clicked= st.button("Predict")

    if clicked:
    
    # model = model.pkl    
        loaded_model=pickle.load(open('models/model_tree.pkl', 'rb'))
        # st.write("Model loaded")
        # st.write("Predicting...")
# data = accept_user_data()
        result=loaded_model.predict_proba(user_prediction_data)
        # st.write("Predictions done computing result")
    
        result_percent=np.round(result[0,1]*100,2)
        st.title("Predictions")
        if int(result_percent)>=65:
            prediction='High Risk for Gestational Diabetes'        
        elif int(result_percent)>=45:
            prediction='Moderate Risk for Gestational Diabetes'    
        else:
            prediction='You are healthy'
        st.pyplot(donut_plot(result_percent, total))
        st.title(prediction)
        x=bmi_calc(bmi)
        y=sugar_calc(Fasting_Glucose)
        if y=='high':
        # st.write(f"You are {x}")
            st.write(f"Your blood sugar level is {y}")
            st.write("Start healthy practices: monitor glucose level everyday, eat healthy and exercise")
            st.write("Learn more from others' experiences click on the button on the side bar")
            
            # if st.button('Open browser', key='url_submit'):
            #     url = 'https://www.reddit.com/r/GestationalDiabetes/'
            #     webbrowser.open_new_tab(url)
        elif y=='overt diabetic':
            st.write(f"You are  overly diabetic")
            st.write("Start healthy practices: monitor glucose level everyday, eat healthy and exercise")
            st.write("Learn more from others' experiences click on the button on the side bar")
            # if st.button('Open browser', key='url_sub'):
            #     url = 'https://www.reddit.com/r/GestationalDiabetes/'
            #     webbrowser.open_new_tab(url)
            # [Comments](https://www.reddit.com/r/GestationalDiabetes/)

# model = "model.pkl"           
# def main():
#     if st.button("Predict"):
#         prediction=predict_model(model)
#         st.success(prediction)

# if __name__ == '__main__':
# 	main()

