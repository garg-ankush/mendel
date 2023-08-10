import openai
import os
from dotenv import load_dotenv

load_dotenv()

class LLM:
    def __init__(self):
        self.model_name: str = "gpt-3.5-turbo"
        self.openai = openai
        self.openai.api_key = os.getenv("OPENAI_API_KEY")

    def call(self, instruction: str, prompt: str, suffix=""):
        return self.completion(str(instruction) + str(prompt) + suffix)

    def completion(self, instructions):
        params = {
            "messages": [
                {
                    "role": "system",
                    "content": instructions,
                }
            ],
            "temperature": 0,
            "max_tokens": 512,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0.6,
        }

        response = self.openai.ChatCompletion.create(model=self.model_name, **params)
        return response["choices"][0]["message"]["content"]