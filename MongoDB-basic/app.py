import streamlit as st
import requests
import pandas as pd

st.title("Customer Feedback System")

# Get Feedback Data
response = requests.get("http://127.0.0.1:5000/feedbacks")
data = response.json()
df = pd.DataFrame(data)

st.write("### Customer Feedbacks")
st.dataframe(df)

# Add New Feedback
st.write("### Add Feedback")
name = st.text_input("Customer Name")
rating = st.slider("Rating", 1, 5, 3)
feedback = st.text_area("Feedback")
date = st.date_input("Date")

if st.button("Submit"):
    feedback_data = {"customer_name": name, "rating": rating, "feedback": feedback, "date": str(date)}
    requests.post("http://127.0.0.1:5000/feedbacks", json=feedback_data)
    st.success("Feedback Submitted!")