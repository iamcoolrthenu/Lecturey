import openai
openai.api_key = "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"
audio_file= open("Recording.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)   