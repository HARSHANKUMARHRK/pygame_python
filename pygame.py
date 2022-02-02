import streamlit as st
import pandas as pd


header = st.container()
dataset = st.container()

with header:
    st.title("basic project") 
    st.text("data set on yellow taxi trip records")
   
with dataset:   
    data_taxi = pd.read_csv("yellow_tripdata_2021-01.csv")
    st.table(data_taxi.head())
