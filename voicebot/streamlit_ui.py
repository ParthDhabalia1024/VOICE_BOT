import streamlit as st
from main import greet_me, take_command, speak

# Function to start listening for commands
def listen_for_commands():
    st.write("Listening...")
    query = take_command().lower()  # Call your existing function
    return query

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Choose an option:", ["Home", "Listening", "About"])

if options == "Home":
    st.title("Welcome to the Voice Assistant Control App!")
    st.write("""
    This app allows you to control various tasks using voice commands.
    Feel free to explore the different sections to learn more about the capabilities of your voice assistant.
    """)

    # Adding an image to the Home section
    st.image("voicebot\images.png", caption="Voice Assistant Home", use_column_width=400)

elif options == "Listening":
    # UI Layout for Listening
    st.title("Voice Assistant Control")
    
    start_button = st.button("🎤 Start Listening")
    stop_button = st.button("🛑 Stop Listening")

    # State to control listening process
    if 'listening' not in st.session_state:
        st.session_state.listening = False

    # Status Indicator
    if st.session_state.listening:
        st.success("Voice Assistant is Listening...")
    else:
        st.warning("Voice Assistant is Not Listening.")

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

elif options == "About":
    st.title("About This Project")
    st.write("""
    This application serves as a voice assistant for various tasks, 
    leveraging speech recognition technology to execute user commands.
    
    ### Features:
    - Voice Recognition
    - Task Automation
    - Customizable Commands

    ### Why Use Our Voice Assistant?
    Our voice assistant is designed to simplify your daily tasks 
    and enhance your productivity by allowing you to interact with your devices using voice commands.
    """)

    # Adding an image to the About section
    st.image("voicebot\images.jpeg", caption="About Voice Assistant", use_column_width=500)

if __name__ == "__main__":
    st.write("Please select an option from the sidebar.")
