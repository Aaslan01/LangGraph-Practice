# making langgraph chat bot backend
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END, START
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv()



llm = ChatGroq(model="llama-3.1-8b-instant")


class ChatState(TypedDict):
    message: Annotated[list[BaseMessage], add_messages]
    
    
def chatnode(state: ChatState):
    message = state["message"]
    response = llm.invoke(message)
    return {"message": [response]}


# checkpointer
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat", chatnode)
graph.add_edge(START, "chat")
graph.add_edge("chat", END) 

chatbot = graph.compile(checkpointer=checkpointer)
