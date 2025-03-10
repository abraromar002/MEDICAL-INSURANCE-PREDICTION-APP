import  numpy as np 
import pandas as pd 
import pickle as pkl 
import streamlit as st

model = pkl.load(open('MIPML.pkl', 'rb'))

st.header(' MEDICAL INSURANCE PREDICTION')

gender=st.selectbox('Enter Gender',['Female', 'Male'])
smoker = st.selectbox('Are u Smoker', ['NO', 'YES'])
region = st.selectbox("Geographical Region", ['Southeast', 'Southwest', 'Northeast', 'Northwest'])
age = st.slider('Enter Your Age',5 , 80)
bmi = st.slider('Enter Bmi',5 , 100)
children =st.number_input("Number of Children", min_value=0, max_value=10, value=0, step=1)


if gender == 'Female':
    gender=0
else:
    gender=1


if smoker == 'NO':
    smoker=0
else:
   smoker=1

if region== 'Southeast':
    region=0

if region== 'Southwest':
    region=1

if region== 'Northeast':
    region=2
else:
    region = 3

input_data=(age,gender,bmi,children,smoker,region)
input_data= np.asarray(input_data)
input_data=input_data.reshape(1,-1)

if st.button('predict'):
  predicted_prem = model.predict(input_data)

  display_string = 'Insurance premium will be ' + str(round(predicted_prem[0] ,2)) +'USD $'

  st.markdown(display_string)
  


       
