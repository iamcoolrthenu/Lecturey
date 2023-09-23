import openai
openai.api_key = "YOUR API-KEY"
audio_file= open("Recording.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)   
