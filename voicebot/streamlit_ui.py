import streamlit as st
from main import greet_me, take_command, speak

# Function to start listening for commands
def listen_for_commands():
    st.write("Listening...")
    query = take_command().lower()  # Call your existing function
    return query

# UI Layout
st.title("Voice Assistant Control")

# Button to trigger listening
start_button = st.button("Start Listening")
stop_button = st.button("Stop Listening")

# State to control listening process
if 'listening' not in st.session_state:
    st.session_state.listening = False

# Check if "Start Listening" button is clicked
if start_button:
    st.session_state.listening = True
    st.write("Voice Assistant is listening...")
    while st.session_state.listening:
        query = listen_for_commands()
        if query:
            st.write(f"Command recognized: {query}")

# Check if "Stop Listening" button is clicked
if stop_button:
    st.session_state.listening = False
    st.write("Voice Assistant has stopped listening.")
