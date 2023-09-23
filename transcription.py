import openai
openai.api_key = "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"
audio_file= open("Recording.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)