import streamlit as st
import pandas as pd
import pickle
from sklearn import preprocessing

# Load the model
model = pickle.load(open("forest_model.pkl", "rb"))

st.title("Bankruptcy Prevention")

risk_mapping = {
    'Low': 0,
    'Medium': 0.5,
    'High': 1
}

# Input selection
Industrial_risk = st.selectbox('Industrial risk', ('Low','Medium','High'))
Management_risk = st.selectbox('Management risk', ('Low','Medium','High'))
Financial_flexibility = st.selectbox('Financial flexibility',('Low','Medium','High'))
Credibility = st.selectbox('Credibility',('Low','Medium','High'))
Competitiveness = st.selectbox('Competitiveness',('Low','Medium','High'))
Operating_risk = st.selectbox('Operating risk', ('Low','Medium','High'))

# Convert categorical inputs to numerical using risk_mapping
industrial_risk = risk_mapping[Industrial_risk]
management_risk = risk_mapping[Management_risk]
financial_flexibility = risk_mapping[Financial_flexibility]
credibility = risk_mapping[Credibility]
competitiveness = risk_mapping[Competitiveness]
operating_risk = risk_mapping[Operating_risk]

# Prepare input for prediction
input_data = pd.DataFrame({
    'industrial_risk': [industrial_risk],
    'management_risk': [management_risk],
    'financial_flexibility': [financial_flexibility],
    'credibility': [credibility],
    'competitiveness': [competitiveness],
    'operating_risk': [operating_risk]
})

# Making the prediction
prediction = model.predict(input_data)

# Displaying the result
if prediction == 1:
    st.write('The company is at risk of bankruptcy')
else:
    st.write('The company is not at risk of bankruptcy')
