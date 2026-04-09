import streamlit as st

st.title("Simple Chat Interface")

# User message block
user_message = st.chat_input("Type your message...")
if user_message:
    st.chat_message("user").write(user_message)

# Assistant message block
st.chat_message("assistant").write("Hello! How can I help you today?")
