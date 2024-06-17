import streamlit as st
import requests
import models.chatbot

st.title("Welcome To Azure Sensei")

def new_query_client(qry: models.chatbot.Query):
    url = 'https://localhost:8000/query'
    x = requests.post(url, json = qry)
    print(x.text)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        for m in st.session_state.messages:
            new_query_client(qry=models.chatbot.Query(role=m["role"], query=m["content"]))

