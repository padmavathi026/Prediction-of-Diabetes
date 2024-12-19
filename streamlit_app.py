import json
import streamlit as st
import requests

user_options = {}

st.title("PREDICTION OF DIABETES")
streamlit_options = json.load(open("streamlit_options-3.json"))
for field_names,range in streamlit_options["slider_fields"].items():
    min_val, max_val = range
    current_value = round((min_val + max_val)/2)
    user_options [field_names] = st.sidebar.slider(field_names, min_val, max_val, value=current_value)



for field_names,values in streamlit_options["single_select_fields"].items():
    user_options[field_names] = st.sidebar.selectbox(field_names, values)

if "Diabetes_012" in user_options:
    del user_options["Diabetes_012"]

st.write("User Input:", user_options)

user_options

if st.button('Predict'):
    data = json.dumps(user_options, indent = 2)
    print(data)
    r = requests.post('http://127.0.0.1:8000/predict', data = data)
    st.write(r.json())