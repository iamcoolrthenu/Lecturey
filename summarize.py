import openai

text = "Your text goes here..."
api_key = "your_api_key_here"

openai.api_key = api_key

response = openai.Completion.create(
    engine="davinci",
    prompt=f"Summarize the following text:\n{text}",
    max_tokens=50  # Adjust the number of tokens as needed for your desired summary length
)

summary = response.choices[0].text
print(summary)
