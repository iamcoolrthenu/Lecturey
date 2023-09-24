import os
import openai
import config
openai.api_key = config.api_key

def getNotes(transcript):
  response = openai.Completion.create(
      engine="text-davinci-002",  # Use the appropriate engine.
      prompt="Write notes on the following: " + transcript,
      max_tokens=500,
      temperature=0.3,
  )
  return response['choices'][0]['text']