from dotenv import load_dotenv
import os
import openai

load_dotenv()


openai.api_key = os.getenv("API_SECRET")

question = input("AMA: ")
response = openai.Completion.create(
    model="text-davinci-003", 
    prompt=question,
    max_tokens=300
                                  )
print(response['choices'][0]['text'])