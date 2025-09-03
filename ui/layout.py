import streamlit as st
from core import chat_manager, storage

def sidebar(state):
    st.sidebar.title("💬 Chats")

    if st.sidebar.button("➕ New Chat"):
        chat_manager.new_chat()
        storage.save_chats(state.chats)

    for chat_id in state.chats:
        if st.sidebar.button(chat_id):
            state.current_chat = chat_id

def display_chat(chat_history):
    for msg in chat_history:
        if msg["role"] == "user":
            st.markdown(f"**🧑 You:** {msg['content']}")
        else:
            st.markdown(f"**🤖 Bot:** {msg['content']}")
