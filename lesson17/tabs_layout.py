import streamlit as st

tab1, tab2, tab3 = st.tabs(['tab 1', 'tab 2', 'tab 3'])

with tab1:
    st.header("Content for tab 1")
    st.write("this is the first content for tab 1")

with tab2:
    st.header("Content for tab 2")
    st.write("this is the 2nd content for tab 1")

with tab3:
    st.header("Content for tab 3")
    st.write("this is the third content for tab 1")