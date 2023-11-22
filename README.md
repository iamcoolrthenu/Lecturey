# Lecturey
Lecturey Website is accessible at [https://lecturey.streamlit.app/](https://lecturey.streamlit.app/).

## Overview

Lecturey is a versatile Python program designed for generating notes and images from transcribed text sourced from video and audio files. It leverages various technologies such as Streamlit for the website interface, Beautiful Soup for web scraping to extract images, OpenAI's Whisper for transcribing text, and OpenAI's ChatGPT for note-taking.

## How to Use

### 1. Download Repository
   - Clone or download the GitHub repository.

### 2. Configure API Key
   - Create a file named `config.py`.
   - Add a variable called `api_key` and set it equal to your OpenAI API key.

### 3. Install Dependencies
   - Open a command/terminal window.
   - Run the command:
     ```bash
     pip install -r requirements.txt
     ```

### 4. Run the Application
   - Navigate to the directory containing `streamlit_app.py`.
   - In a terminal window, run the command:
     ```bash
     python3 -m streamlit run streamlit_app.py
     ```

## Dependencies

Ensure you have the following dependencies installed:

- streamlit
- selenium
- beautifulsoup4
- googlesearch-python
- openai
  
