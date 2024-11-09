
# Voice Assistant Project

This is a Python-based voice assistant project that integrates various functionalities such as web search, email sending, playing YouTube videos, fetching weather reports, and more. The project can be run locally, inside a Docker container, or through a **Streamlit** web app for an interactive UI experience.

## Features

- **Speech Recognition**: Listens to voice commands and responds with relevant actions.
- **Web Integration**:
  - Google Search
  - YouTube playback
  - Wikipedia search
- **Utility Commands**:
  - Open Notepad, Command Prompt, and Camera
  - Fetch IP Address
  - Send emails
  - Get weather updates
  - News reading
  - IMDb movie information
  - Basic calculations using WolframAlpha API
- **Streamlit Web Interface**:
  - Home, Listening, and About sections
  - UI buttons to start and stop listening to voice commands
  - Visual feedback of the assistant’s status
- **Custom Hotkeys**:
  - Start listening: `Ctrl + Alt + K`
  - Stop listening: `Ctrl + Alt + P`

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `pyttsx3`: Text-to-speech conversion
  - `SpeechRecognition`: Recognize speech input
  - `Streamlit`: Web interface for the assistant
  - `keyboard`: Detect key presses for hotkeys
  - `requests`: HTTP requests
  - `pyautogui`: Automating the mouse and keyboard
  - `wolframalpha`: WolframAlpha API for calculations
  - `imdbpy`: Fetching IMDb movie data
  - `webbrowser`: Opening browser for web-based actions
- **Docker**: Containerization for easy deployment and environment consistency

## Getting Started

### Prerequisites

1. **Python**: Ensure Python 3.x is installed.
2. **Dependencies**: Install the required Python libraries. Run the following command:
   ```bash
   pip install -r requirements.txt
   ```
3. **VS Code (Optional)**: If you're using VS Code, install the Docker extension for easy Docker management.

### Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/voice-assistant
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the project:
   ```bash
   python main.py
   ```

### Running with Streamlit

To use the Streamlit-based UI, follow these steps:

1.Go to the specified directory where you have the porject
2. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```
3. Open the provided local URL to access the Streamlit web interface.

In the Streamlit app, you can:
- Navigate through **Home**, **Listening**, and **About** sections.
- Start and stop listening using UI buttons.
- Receive visual feedback on the assistant’s listening status.

### Running with Docker

1. Install Docker (if not installed already). You can use **Docker Desktop** for Windows and macOS or follow the instructions for Linux.
2. Build the Docker image:
   ```bash
   docker build -t voice-assistant .
   ```
3. Run the Docker container:
   ```bash
   docker run -it voice-assistant
   ```

### VS Code Docker Extension

If you prefer using VS Code's Docker extension:

1. Install the **Docker Extension** in VS Code.
2. Open the project folder in VS Code.
3. Build and run the Docker image using the Docker extension UI.

## Project Structure

```
├── app.py                # Streamlit app entry point
├── main.py               # Main entry point for the voice assistant
├── const.py              # Contains constants and utility text
├── requirements.txt      # Python dependencies
├── Dockerfile            # Dockerfile for containerizing the project
└── README.md             # Project documentation
```

## Usage

- **Start the Assistant**: The voice assistant will greet you and ask for commands.
- **Stop Listening**: Use the hotkey `Ctrl + Alt + P` or the Stop button in the Streamlit app.
- **Supported Commands**:
  - "Open Google"
  - "Open YouTube"
  - "What's the weather?"
  - "Send an email"
  - "Play music on YouTube"
  - "What's my IP address?"
  - And more...

## Docker Image

You can build and run the Docker image of the project for a portable and consistent environment. The Dockerfile ensures the required dependencies are installed and the project runs as intended inside a container.

## Contribution

If you'd like to contribute, feel free to create a pull request or raise issues. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
