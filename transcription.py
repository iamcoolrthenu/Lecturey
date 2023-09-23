import openai
openai.api_key = "YOUR API-KEY"
openai.api_key = ""
audio_file= open("Recording.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

prompt = "Makes notes of this, format it like notion lecture notes:\n"+transcript

response = openai.Completion.create(
    engine="text-davinci-002",  
    prompt=prompt,
    max_tokens=50,  
)

# Extract and print the generated text
generated_text = response.choices[0].text
print(generated_text)