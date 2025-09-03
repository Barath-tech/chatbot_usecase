
import streamlit as st
from core import chat_manager, llm_api, storage
from ui import layout
from config.settings import MODEL_NAME

st.set_page_config(page_title="LLM Chatbot", page_icon="🤖", layout="wide")

# --- Session State Init ---
if "chats" not in st.session_state:
    st.session_state.chats = storage.load_chats()
if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

# --- Sidebar ---
layout.sidebar(st.session_state)

# --- Main Area ---
if st.session_state.current_chat:
    chat_history = st.session_state.chats[st.session_state.current_chat]

    layout.display_chat(chat_history)

    user_input = st.chat_input("Type your message...")
    if user_input:
        chat_manager.add_message(st.session_state.current_chat, "user", user_input)

        response = llm_api.send_to_llm(chat_history, model=MODEL_NAME)
        chat_manager.add_message(st.session_state.current_chat, "assistant", response)

        storage.save_chats(st.session_state.chats)
        st.rerun()
else:
    st.info("Click **New Chat** in sidebar to start a conversation.")
