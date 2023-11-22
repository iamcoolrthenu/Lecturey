import streamlit as st
import openai

# Set OpenAI API key from the config file
openai.api_key = st.secrets["api_key"]

def getNotes(transcript):
    """
    Generate notes using OpenAI's Completion API.

    Parameters:
    - transcript (str): The input transcript for generating notes.

    Returns:
    - str: Generated notes based on the input transcript.
    """
    # Create a completion using OpenAI's API
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use the appropriate engine.
        prompt="Write notes on the following: " + transcript,
        max_tokens=500,
        temperature=0.3,
    )

    # Extract and return the generated notes from the API response
    return response['choices'][0]['text']
