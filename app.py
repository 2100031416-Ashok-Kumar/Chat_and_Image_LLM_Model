from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="LLM chat model")

st.header("Gemini GPT")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")
new_chat = st.button("New Chat")

if submit and input:
    response = get_gemini_response(input)
    st.session_state.chat_history.append({"question": input, "response": response})

if new_chat:
    st.session_state.chat_history = []

if st.session_state.chat_history:
    with st.expander("Chat History"):
        for chat in st.session_state.chat_history:
            st.write(f"**Q:** {chat['question']}")
            st.write(f"**A:** {chat['response']}")
            st.write("---")

if st.session_state.chat_history:
    st.subheader("Current Chat")
    st.write(f"**Q:** {st.session_state.chat_history[-1]['question']}")
    st.write(f"**A:** {st.session_state.chat_history[-1]['response']}")
    st.write("---")
