import openai
openai.api_key = "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"
audio_file= open("Recording.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)   
