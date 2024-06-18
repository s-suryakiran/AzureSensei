import streamlit as st
import chatbot as chatbot

st.title("Welcome To Azure Sensei")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])


# if prompt := st.chat_input("Ask your question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):
#         for m in st.session_state.messages:
#             chatbot.query_create(
#                 qry=models.chatbot.Query(role=m["role"], query=m["content"])
#             )


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask anything about Azure Services.."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    if prompt.lower().strip() in ["hi", "hello", "hey"]:
        assistant_response = "Hello there! Feel free to ask me anything about Azure Services."
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    else:
        assistant_response = chatbot.chat_completion(prompt)
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_response}
    )
