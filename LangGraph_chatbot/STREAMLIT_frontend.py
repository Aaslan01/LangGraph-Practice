import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

st.title("Simple Chat Interface")

if 'memory_history' not in st.session_state:
    st.session_state['memory_history'] = []




if st.session_state['memory_history']:
    for message in st.session_state['memory_history']:
        with st.chat_message(message["role"]):
            st.text(message["content"])

# Assistant message block
# show input text box at the bottom of the page
user_input = st.chat_input("Enter your message:")

CONFIG =  {'configurable': {'thread_id': 'thread_1'}} 
if user_input:
    
    # Append user message to memory history
    st.session_state['memory_history'].append({"role": "user", "content": user_input})
    # Display user message
    with st.chat_message("user"):
        st.text(user_input)
    
    # Get assistant response from chatbot
    response = chatbot.invoke({"message": [HumanMessage(content=user_input)]}, config = CONFIG )   
    ai_message = response["message"][-1].content
    #append assistant message to memory history
    st.session_state['memory_history'].append({"role": "assistant", "content": ai_message})
     # Display assistant message
    with st.chat_message("assistant"):
        st.text(ai_message)