import streamlit as st
import openai
import config
# Set your OpenAI API key here
openai.api_key = config.api_key

def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript

    except Exception as e:
        return f"Error: {str(e)}"

# Set the title and description of your app
st.title("Lecturey")

# Create a file uploader widget that accepts both audio and video file types
uploaded_file = st.file_uploader("Upload a video or audio file to transcribe.", type=["mp3", "wav", "ogg", "mp4", "avi", "mov"])

# Check if a file was uploaded
if uploaded_file is not None:
    # Determine if the uploaded file is an audio or video based on the file extension
    file_extension = uploaded_file.type.split("/")[-1]

    if file_extension in ["mp3", "wav", "ogg", "mp4", "avi", "mov"]:
        # Display the file type
        st.write(f"Uploaded {file_extension} file")

        # Provide an option to upload a text file for transcription
        txt_file = st.file_uploader("Upload a text file to get transcription", type=["txt"])
        if txt_file is not None:
            # Perform audio to text transcription using OpenAI convertion 
            transcription = convert_audio_to_text(uploaded_file)
            transcription = str(transcription)
            with open("text.txt", "w") as text_file:
                text_file.write(transcription)
            st.write("Transcription:")
            st.write(transcription)
            

    else:
        st.write("Unsupported file format. Please upload an audio or video file.")
else:
    st.write("Please upload a file.")
