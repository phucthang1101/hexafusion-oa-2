# import openai
# import os

# openai.api_key = os.getenv("OPENAI_API_KEY")

# def summarize_input(text):
#     prompt = f"Summarize the following message in one sentence:\n\n{text}"

#     try:
#         response = openai.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.5
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         return f"Error: {str(e)}"

import os
from dotenv import load_dotenv

import cohere
load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))


def summarize_input(text):
    prompt = f"""
You are an assistant summarizing incoming customer notes.

Summarize the following message in one sentence:

"{text}"
"""

    try:
        resp = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=50
        )
        return resp.generations[0].text
    except Exception as e:
        return f"Error: {str(e)}"

