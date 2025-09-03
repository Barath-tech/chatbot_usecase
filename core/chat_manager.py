import streamlit as st

def new_chat():
    chat_id = f"chat_{len(st.session_state.chats)+1}"
    st.session_state.chats[chat_id] = []
    st.session_state.current_chat = chat_id

def add_message(chat_id, role, content):
    st.session_state.chats[chat_id].append({"role": role, "content": content})
