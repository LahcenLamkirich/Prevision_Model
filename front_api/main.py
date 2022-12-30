import streamlit as st
import pandas as pd
import numpy as np
import pickle 
import streamlit.components.v1 as components


st.write("Front de l'application de la prediction de l'accord d'un credit")

#Collecter le profil d'entrée
st.sidebar.header("Les caracteristiques du client")

def client_caract_entree():
    Gender=st.sidebar.selectbox('Sexe',('Male','Female'))
    Married=st.sidebar.selectbox('Marié',('Yes','No'))
    Dependents=st.sidebar.selectbox('Enfants',('0','1','2','3+'))
    Education=st.sidebar.selectbox('Education',('Graduate','Not Graduate'))
    Self_Employed=st.sidebar.selectbox('Salarié',('Yes','No'))
    ApplicantIncome=st.sidebar.slider('Salaire du client',150,4000,200)
    CoapplicantIncome=st.sidebar.slider('Salaire du conjoint',0,40000,2000)
    LoanAmount=st.sidebar.slider('Montant du crédit en Kdollar',9.0,700.0,200.0)
    Loan_Amount_Term=st.sidebar.selectbox('Durée du crédit',(360.0,120.0,240.0,180.0,60.0,300.0,36.0,84.0,12.0))
    Credit_History=st.sidebar.selectbox('Credit_History',(1.0,0.0))
    Property_Area=st.sidebar.selectbox('Property_Area',('Urban','Rural','Semiurban'))


    # #  Prepare data transform
    Gender = 1 if Gender == 'Male' else 0
    Education = 1 if Education == 'Graduate' else 0
    Property_Area = 0 if Property_Area == 'Urban' else 1 if Property_Area == 'Rural' else 2
    Self_Employed = 1 if Self_Employed == 'Yes' else 0
    Married = 1 if Married == 'Yes' else 0
    Dependents = 3 if Dependents == '3+' else Dependents

    # Features :
    data={
    'Gender':Gender,
    'Married':Married,
    'Dependents':Dependents,
    'Education':Education,
    'Self_Employed':Self_Employed,
    'Property_Area':Property_Area,
    'ApplicantIncome':ApplicantIncome,
    'CoapplicantIncome':CoapplicantIncome,
    'LoanAmount':LoanAmount,
    'Loan_Amount_Term':Loan_Amount_Term,
    'Credit_History':Credit_History,
    }

    profil_client=pd.DataFrame(data,index=[0])
    return profil_client

input_df=client_caract_entree()

st.write(input_df)

#importer le modèle
load_model=pickle.load(open('C:/Users/Lahcen Lamkirich/Desktop/Ai_proj/new/model.pkl','rb'))


#appliquer le modèle sur le profil d'entrée
prevision=load_model.predict(input_df)

st.subheader('Résultat de la prévision')
st.write(prevision)
