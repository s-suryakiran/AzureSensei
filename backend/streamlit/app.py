import streamlit as st
import chatbot
import models.chatbot

st.title("Welcome To Azure Sensei")

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
            chatbot.query_create(
                qry=models.chatbot.Query(role=m["role"], query=m["content"])
            )
