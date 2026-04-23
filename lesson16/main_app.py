import streamlit as st

if st.button("click me"):
    st.write("button clicked")

if st.checkbox("check me to show some text"):
    st.write("youre seeing this text because you checked the checkbox")

user_input = st.text_input("enter text", "sample text")
st.write("You entered:", user_input)

age = st.number_input("enter your age", min_value=0, max_value=100)
st.write(f"your age is: {age}")

message = st.text_area("enter message")
st.write(f"your message: {message}")

choice = st.radio("pick one", ["Choice 1", "choice 2", "choice 3"])
st.write(f"you chose: {choice}")

if st.button("succes"):
    st.success("operaton was succesful")

try:
    1/0
except Exception as e:
    st.exception(e)