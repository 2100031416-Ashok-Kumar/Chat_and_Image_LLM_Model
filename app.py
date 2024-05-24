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

form = st.form(key='chat_form')
input_message = form.text_input(label='You:', key='input')

if form.form_submit_button(label='Send') and input_message:
    response = get_gemini_response(input_message)
    st.session_state.chat_history.append({"question": input_message, "response": response})

if st.session_state.chat_history:
    with st.expander("Chat History"):
        for chat in st.session_state.chat_history:
            st.write(f"**You:** {chat['question']}")
            st.write(f"**Gemini GPT:** {chat['response']}")
            st.write("---")

if st.session_state.chat_history:
    st.subheader("Current Chat")
    st.write(f"**You:** {st.session_state.chat_history[-1]['question']}")
    st.write(f"**Gemini GPT:** {st.session_state.chat_history[-1]['response']}")
    st.write("---")
