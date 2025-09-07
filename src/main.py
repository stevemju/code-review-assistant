import os
import json
from openai import OpenAI
from prompt import SYSTEM_PROMPT
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_code_review(code_snippet: str):
  try:
    response = client.chat.completions.create(
        model="o4-mini", 
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Here is the code snippet:\n\n```python\n{code_snippet}\n```"}
        ]
    )
    return response.choices[0].message.content

  except Exception as e:
    return f"An error occurred: {e}"
