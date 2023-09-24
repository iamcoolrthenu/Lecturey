import openai
import config

openai.api_key = config.api_key
vid_aud_file = open("testvid.mp4", "rb")
raw_transcript = openai.Audio.transcribe("whisper-1", vid_aud_file)

# Convert the transcript to a string
uploaded_file = open(vid_aud_file, "rb") #reading the video in binary.
transcript = str(uploaded_file) #converting the video from binary to string
print(transcript)

# Specify the output file name
output_file_name = transcript

# Write the formatted transcription to the output file
with open(output_file_name, "w") as output_file:
    # Split the transcript into words
    words = transcript.split()
    # Iterate through the words and write 10 words per line
    for i in range(0, len(words), 10):
        line = " ".join(words[i:i+10])
        output_file.write(line + "\n")

print(f"Transcription saved to {output_file_name}")
