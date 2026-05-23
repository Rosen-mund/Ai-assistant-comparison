import google.generativeai as genai
import os

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_frontier_response(messages):

    conversation = ""

    for msg in messages:

        role = msg["role"]
        content = msg["content"]

        conversation += f"{role}: {content}\n"

    response = model.generate_content(
        conversation
    )

    return response.text