import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid



# -------- utlity functions --------
def generate_thread_id():
    return uuid.uuid4()

def reset_thread():
    st.session_state['thread_id'] = generate_thread_id()
    st.session_state['message_history'] = []
    add_thread_to_history(st.session_state['thread_id'])
    st.rerun()

def add_thread_to_history(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)


st.title("Simple Chat Interface")

# ============= Session State Management for Chat History =============
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []
    
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []  # [thread_id]

add_thread_to_history(st.session_state['thread_id'])
# =============


#------- Chat history management Side bar -------
st.sidebar.markdown("## LangGraph Chatbot")
if st.sidebar.button("New Chat"):
    reset_thread()

st.sidebar.caption("Keep it simple. Start a fresh thread anytime.")
st.sidebar.markdown("### My Conversations")
for thread_id in st.session_state['chat_threads']:
    st.sidebar.button(str(thread_id))
# =============

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']): 
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input('Type here')

# st.session_state -> dict -> 
CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # first add the message to message_history
    # # Display assistant message
    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'message': [HumanMessage(content=user_input)]},
                config= CONFIG,
                stream_mode= 'messages'
            )
        )
        
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})