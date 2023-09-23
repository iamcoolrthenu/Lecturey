import openai as oai

oai.api_key = "YOUR_APIKEY"
audio_file= open("testvid.mp4", "rb")
transcript = oai.Audio.transcribe("whisper-1", audio_file) 
print(transcript)

prompt = "Makes notes of this, format it like notion lecture notes:\n"+transcript

response = oai.Completion.create(
    engine="text-davinci-002",  
    prompt=prompt,
    max_tokens=50,  
)

# Extract and print the generated text
generated_text = response.choices[0].text
print(generated_text)
