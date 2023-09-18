# Description of the GitHub Project

## Project Name: Jarvis - Voice Assistant

### Overview
This GitHub project, named "Jarvis - Voice Assistant," is a Python-based voice assistant that allows users to interact with their computer using voice commands. The voice assistant is designed to perform various tasks, including web browsing, providing weather information, opening applications, playing music, searching the web, and more.

### Features
1. **Voice Recognition**: The project uses the `speech_recognition` library to recognize and convert voice commands into text.

2. **Voice Output**: It utilizes the Windows Speech API (`win32com.client`) to enable the assistant to speak and provide responses audibly.

3. **OpenAI Integration**: The assistant can provide information and responses by interfacing with the OpenAI GPT-3 model using the OpenAI API.

4. **Web Browsing**: Users can instruct the assistant to open various websites like YouTube, Google, Facebook, and others.

5. **Music Playback**: The assistant can play random music tracks from a specified directory on the computer.

6. **Notepad and File Explorer**: Users can open Notepad and File Explorer with voice commands.

7. **Code Editor**: It can also open Visual Studio Code and Python IDLE for coding purposes.

8. **Wikipedia Search**: The assistant can search and provide summaries from Wikipedia.

9. **Weather Information**: Users can inquire about the weather conditions for a specific location using data from OpenWeatherMap.

10. **Time Information**: The assistant can tell the current time.

11. **AI Information Retrieval**: It can search for information using AI-powered responses through the OpenAI GPT-3 model.

12. **Exit Command**: The assistant can be terminated with the voice command "jarvis quit."

### Prerequisites
- Python (with required libraries: `speech_recognition`, `win32com.client`, `requests`, `wikipedia`, `openai`)
- OpenAI API Key and OpenWeatherMap API Key (configured in the `config.py` file)
- A microphone for voice input

### Usage
1. After running the script, the assistant greets the user and waits for voice commands.
2. Users can give voice commands to perform tasks like opening websites, searching the web, playing music, and more.
3. The assistant responds audibly to voice commands and performs the requested actions.

### Note
- This project assumes that Windows is the operating system and uses Windows-specific libraries.
- You need to configure the `config.py` file with your OpenAI API key and OpenWeatherMap API key.
- Some actions, like opening specific applications, may require adjustments to the file paths based on your system configuration.

### Disclaimer
This project is for educational and personal use only. It may require additional customization to work seamlessly on different systems and environments. Use it responsibly and respect privacy and security concerns while using voice recognition technology.

### Author
Aman Bisht

### Contributions
Contributions to this project are welcome. Feel free to fork the repository and create pull requests to enhance its functionality or fix issues. Please adhere to the project's coding and contribution guidelines.
