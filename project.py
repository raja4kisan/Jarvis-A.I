import openai
import os
from config import apikey
# Load the API key from an environment variable
openai.api_key = apikey

try:
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Replace with the appropriate model name
        prompt="Dear Hiring Manager,\nI am writing to express my interest in the [position] position at [company].",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

    print(response)
except Exception as e:
    print(f"Invalid Request! Error: {e}")


'''
{
  "id": "chatcmpl-8zKczwq7ZTwkGozygrjS6R3Hf1aX5",
  "object": "chat.completion",
  "created": 1709627993,
  "model": "gpt-3.5-turbo-0125",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "there was a young girl named Lily who lived in a small village nestled in the rolling hills of the countryside. Lily was known for her kindness and curiosity, always eager to help others and explore the world around her."
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 22,
    "completion_tokens": 43,
    "total_tokens": 65
  },
  "system_fingerprint": "fp_2b778c6b35"
}
'''
