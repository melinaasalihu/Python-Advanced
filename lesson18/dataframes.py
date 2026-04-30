import pandas as pd
import streamlit as st

st.header("Displaying dataframes")

data = pd.DataFrame({
    'Name' : ['Melina','Egzon','Dion','Sara','Liron','Reina'],
    'Age'  : [17,17,18,18,16,15],
    'City' : ['Fush Kosove', 'Prishtine', 'Presheve','Obiliq','Prishtine','Prishtine']

})
st.dataframe(data)