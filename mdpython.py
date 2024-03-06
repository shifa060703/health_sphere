# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:09:59 2024

@author: shifa
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu 


diabetes_model = pickle.load(open('C:/Users/shifa/OneDrive/Desktop/Multiple Disease Prediction System/saved models-HS/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/shifa/OneDrive/Desktop/Multiple Disease Prediction System/saved models-HS/heart_disease_model.sav' ,'rb'))

parkinsons_model = pickle.load(open('C:/Users/shifa/OneDrive/Desktop/Multiple Disease Prediction System/saved models-HS/parkinsons_model.sav', 'rb'))


#trying00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

 
#trying00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
with st.sidebar:
    selected = option_menu('HEALTH SPHERE 🏥🌐A Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons  Prediction'],
                           
                           icons = ['bandaid','heart-pulse','person-check'], 
                           
                           default_index = 0)
    
    
#diabetes prediction page-page number 1
if(selected == 'Diabetes Prediction'):
    st.title("HEALTH SPHERE 🏥🌐-Diabetes Prediction ")
    
    #getting input data -cols for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', key='Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level' , key='Glucose')
    with col3:
        BloodPressure =  st.text_input('BloodPressure value', key='BloodPressure')
    with col1:
        SkinThickness =	 st.text_input('SkinThickness value', key='SkinThickness')
    with col2:
        Insulin	=  st.text_input('Insulin Level', key='Insulin')
    with col3:
        BMI =  st.text_input('BMI value', key='BMI')
    with col1:
        DiabetesPedigreeFunction =  st.text_input(' Diabetes Pedigree Function value', key='DiabetesPedigreeFunction')
    with col2:
        Age =  st.text_input('Age of the patient', key='Age') 
    
    #code for prediction    
    diab_dignosis = '' 
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]) 
        
        if( diab_prediction[0] == 1):
            diab_dignosis = 'The Patient Is Diabetic'
            
        else:
            diab_dignosis = 'The Patient Is Not Diabetic'
            
    
    st.success(diab_dignosis)
           
              
    
    
    
#heart prediction page-page no .2
if(selected == 'Heart Disease Prediction'):
    st.title("HEALTH SPHERE 🏥🌐-Heart Disease Prediction ")
    
    #getting input data -cols for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        years = st.text_input('Age' , key='years')
        
    with col2:
        sex = st.text_input('Sex' ,key='sex')
        
    with col3:
        cp = st.text_input('Chest Pain type', key='cp')
   
    with col1:
        trestbps = st.text_input('Resting BloodPressure', key='trestbps')
     
    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dL', key='chol')
      
    with col3:
        fbs =  st.text_input('Fasting Blood Sugar- mg/dL', key='fbs')
       
    with col1:
        restecg = st.text_input('Resting ECG', key='restecg')
      
    with col2:
        thalach =  st.text_input('Maximum Heart Rate Achieved in bpm', key='thalach')
         
    with col3:
        exang =  st.text_input('Exercise-Induced Angina', key='exang') 
        
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise Relative to Rest value', key= 'oldpeak')
        
    with col2:
        slope =  st.text_input('Peak Exercise ST Segment value', key='slope')
     
    with col3:
        ca =  st.text_input('Number of Major Vessels ', key='ca')
     
    with col1:
        tip=  st.text_input('Thalassemia', key='tip') 
        
    #code for prediction    
    heart_dignosis ='' 
    
    #creating a button for prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[years, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, tip]])
        
        if( heart_prediction[0] == 1):
            heart_dignosis = 'The Patient Has Heart Disease'
            
        else:
            heart_dignosis = 'The Patient Does NOT Have Any Heart Disease'
            
    st.success(heart_dignosis)
        
        
        
       													
#Parkinsons prediction page-PAGE 3
if (selected == 'Parkinsons  Prediction'):
    st.title("HEALTH SPHERE 🏥🌐-Parkinsons Prediction")
    
    #getting input data -cols for input fields
    col1, col2, = st.columns(2)
    
    with col1:
        fo = st.text_input('MDVP Fo(Hz)-Mean Frequency value', key='fo')
    with col2:
        fhi = st.text_input('MDVP Fhi(Hz)-Maximum Frequency' , key='fhi')
    with col1:
        flo =  st.text_input('MDVP Flo(Hz)-Minimum Frequency value', key='flo')
    with col2:
        JitterPercentage = st.text_input('MDVP Jitter_Percentage', key='JitterPercentage')
    with col1:
        Jitterabs	=  st.text_input(' MDVP Jitter(Abs)-Absolute Jitter', key='Jitterabs')
    with col2:
        RAP =  st.text_input('Relative Amplitude Perturbation(RAP)', key='RAP')
    with col1:
        PPQ =  st.text_input('  Perturbation Quotient(PPQ)', key='PPQ')
    with col2:
        DDP =  st.text_input('Jitter (DDP)', key='Jitter:DDP')
    with col1:
        Shimmer =  st.text_input('MDVP Shimmer value', key='Shimmer')
    with col2:
        ShimmerdB =	 st.text_input('MDVP Shimmer(dB) value', key='ShimmerdB')
    with col1:
        APQ3	=  st.text_input('Shimmer APQ3', key='APQ3')
    with col2:
        APQ5 =  st.text_input('Shimmer APQ5', key='APQ5')
    with col1:
        APQ =  st.text_input(' MDVP APQ', key='APQ')
    with col2:
        DDA	=  st.text_input('Shimmer DDA value', key='DDA')
    with col1:
        NHR =  st.text_input('Noise-to-Harmonics Ratio (NHR)', key='NHR')
    with col2:
        HNR =  st.text_input(' Harmonics-to-Noise Ratio (HNR)', key='HNR')
    with col1:
        RPDE =  st.text_input('Recurrence Period Density Entropy', key='RPDE')
    with col2:
        DFA =  st.text_input(' Detrended Fluctuation Analysis', key='DFA')
    with col1:
        spread1 =	 st.text_input('spread1 value', key='spread1')
    with col2:
        spread2	=  st.text_input('spread2 value', key='spread2')
    with col1:
        D2 =  st.text_input('D2 value', key='D2')
    with col2:
        PPE =  st.text_input(' Pitch Period Entropy (PPE)', key='PPE')
        
    
        
    #code for prediction    
    park_dignosis = ''
    
    #creating a button for prediction
    if st.button('Parkinsons Disease Test Result'):
        park_prediction = parkinsons_model.predict([[fo, fhi,flo,JitterPercentage,Jitterabs,RAP, PPQ,DDP,Shimmer, ShimmerdB,APQ3,APQ5,APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2,D2,PPE]])
        
        if( park_prediction[0] == 1):
            park_dignosis = 'The Patient Has Parkinsons Disease'
            
        else:
            park_dignosis = 'The Patient Does NOT Have Any Parkinsons Disease'
    st.success(park_dignosis)
    
    
   
        
        
        																
        



        
       
        
        
        
        
        
        
    
       
        
     
         
    
    
  
        
