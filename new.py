import streamlit as st
import pickle



with open("knn.pkl", "rb") as f:
    model = pickle.load(f)

st.title("My KNN Model")
age = st.number_input("Enter age")
salary = st.number_input("Enter salary")
exp = st.number_input("Enter years")
dept = st.number_input("Enter department: (0-HR, 1-IT, 2-Sales)")
pred = model.predict([[age,salary,exp,dept]])
if st.button("Analyze"):
    if pred == 1:
        st.success("You are going good")
    else:
        st.warning("Chances of layoffs")