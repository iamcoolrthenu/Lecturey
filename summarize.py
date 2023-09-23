import os
import openai

openai.api_key = ""
with open('text.txt', 'r') as file:
    user_content = file.read()

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with lecture notes, and your task is to summarize the lecture"
    },
    {
      "role": "user",
      "content": user_content
    }
  ],
  temperature=0,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response['choices'][0]['message']['content'])
