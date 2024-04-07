import streamlit as st
user_input = st.text_input("Enter some text")
button = st.button("reverse")
if button: st.write(user_input[::-1])
