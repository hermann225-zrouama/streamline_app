import streamlit as st
from PIL import Image
import pandas as pd

st.title("Hello World")
st.write("This is my first Streamlit app!")

data = pd.read_csv("api_data.csv")

column = st.multiselect("Choose a column", data.columns)

# head de la data
st.dataframe(data[column].head())

# histograme userId
st.bar_chart(data['userId'])