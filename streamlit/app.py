import streamlit as st 
import pandas as pd
import numpy as np

#title
st.title("Helloe bro")

#simple text 
st.write("Simple word")

#create a simple data frame

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

## display the dataframe
st.write("Here's our first attempt at using data to create a table:")
st.write(df)

#create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.line_chart(chart_data)