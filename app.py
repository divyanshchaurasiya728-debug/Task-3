import numpy as np
import pandas as pd
import streamlit as st
import joblib
model = joblib.load("XGBoost.pkl")

st.title("Income predictor for U.S. people of year 1994-95")
st.write("Enter the required details to predict the income.")

industry_code = st.selectbox("Select the major industry code",['Not in universe or children','Construction','Entertainment','Finance insurance and real estate','Education',
'Business and repair services','Manufacturing-nondurable goods','Personal services except private HH','Manufacturing-durable goods','Other professional services',
'Mining','Transportation','Wholesale trade','Public administration','Retail trade',
'Social services','Private household services','Utilities and sanitary services','Communications','Hospital services',
'Medical except hospital','Agriculture','Forestry and fisheries','Armed Forces'])
num_of_weeks_worked_in_a_year = st.text_input("Enter the number of weeks worked in a year")
tax_filer = st.selectbox("Select the Tax filer status",["Nonfiler",'Head of household','Joint both under 65','Single','Joint both 65+','Joint one under 65 & one 65+'])
num_workers_worked_for_employer = st.selectbox("Select the number of workers worked for employer:",[0, 1, 6, 4, 5, 3, 2])
major_occupation_code = st.selectbox("Select the major occupation",['Not in universe','Precision production craft & repair','Professional specialty','Executive admin and managerial','Handlers equip cleaners etc',
'Adm support including clerical', 'Machine operators assmblrs & inspctrs','Other service','Sales','Private household services','Technicians and related support','Transportation and material moving',
'Farming forestry and fishing','Protective services','Armed Forces'])
sex = st.selectbox("Selecte the Gender",['Male','Female','Other'])
education = st.selectbox("Select the education level",['High school graduate', 'Some college but no degree','10th grade','Children','Bachelors degree(BA AB BS)',
'Masters degree(MA MS MEng MEd MSW MBA)','Less than 1st grade','Associates degree-academic program','7th and 8th grade','12th grade no diploma',
'Associates degree-occup /vocational','Prof school degree (MD DDS DVM LLB JD)','5th or 6th grade','11th grade',
'Doctorate degree(PhD EdD)','9th grade','1st 2nd 3rd or 4th grade'])

input_data = pd.DataFrame([[industry_code, num_of_weeks_worked_in_a_year , tax_filer, num_workers_worked_for_employer,major_occupation_code,sex,education]],
columns =['Industry code','Number of weeks worked in a year','Tax filer status','Number of workers worked for Employer','Major occupation code','Sex','Education'])

input_data = pd.get_dummies(input_data)

if st.button("Predict Income"):
    prediction = model.predict(input_data)[0]
    st.success(f"📌 Predicted Income: {round(prediction, 2)} USD")