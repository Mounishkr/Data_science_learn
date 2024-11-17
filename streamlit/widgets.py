import streamlit as st 
import pandas as pd


st.title("Streamlit Text input")

name=st.text_input("Enter your name", "Type here...")

age=st.slider("Select your age", 18, 100)

st.write("Your age is, {age}.")

options = ['Green', 'Yellow', 'Red', 'Blue']
color = st.selectbox('What is your favorite color?', options)
st.write(f"Your favorite color is {color}.")

if name:
    st.write(f"hello, {name}")
    
data = {"Name": ["John", "Jane", "Bob"], "Age": [25, 30, 35], "City": ["New York", "London", "Paris"]}
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)
    
    
uploaded_file = st.file_uploader("Choose a file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
    

