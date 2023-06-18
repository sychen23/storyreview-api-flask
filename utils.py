import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_completion(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
    )
    return response.choices[0].text
