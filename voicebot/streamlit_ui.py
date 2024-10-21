import streamlit as st
from main import greet_me, take_command, speak

# Function to start listening for commands
def listen_for_commands():
    st.write("Listening...")
    query = take_command().lower()  # Call your existing function
    return query

# UI Layout
st.set_page_config(page_title="Voice Assistant Control", page_icon="🎤", layout="wide")

# Sidebar for options
st.sidebar.header("Voice Assistant Options")
st.sidebar.markdown("### Control the voice assistant:")
st.sidebar.write("Use the buttons below to start or stop the voice assistant.")

# Button to trigger listening
start_button = st.sidebar.button("Start Listening")
stop_button = st.sidebar.button("Stop Listening")

# State to control listening process
if 'listening' not in st.session_state:
    st.session_state.listening = False

# Main content area
st.title("Voice Assistant Control")
st.image("voicebot\images.jpeg", width=400)  # Replace with a relevant image URL

# Check if "Start Listening" button is clicked
if start_button:
    st.session_state.listening = True
    st.success("Voice Assistant is now listening...")
    while st.session_state.listening:
        query = listen_for_commands()
        if query:
            st.write(f"Command recognized: **{query}**")
            # Optional: Add response for recognized commands
            if "how are you" in query:
                speak("I am absolutely fine. What about you?")
                st.write("Response: I am absolutely fine. What about you?")
            # Add more command responses here as needed

# Check if "Stop Listening" button is clicked
if stop_button:
    st.session_state.listening = False
    st.success("Voice Assistant has stopped listening.")

# Footer
st.markdown("---")
st.write("Developed by Parth Dhabalia | Voice Assistant Project")
