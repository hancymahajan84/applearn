import streamlit as st
import pandas as pd
df=pd.read_csv('data.csv')
st.title('learning streamlit programing')
a=st.text_input('enter your name')
mm=st.number_input('enter your ip marks')
if st.button('submit'):
     st.write(f'hello! {a} , your ip marks is {mm}')
     st.dataframe(df)
     
