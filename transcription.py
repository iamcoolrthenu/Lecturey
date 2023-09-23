import openai
openai.api_key = "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"
audio_file= open("Recording.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)   
