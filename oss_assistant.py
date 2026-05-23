from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct",
    temperature=0.3,
    do_sample=True
)

SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer clearly and concisely.
"""

def generate_oss_response(messages):

    formatted_messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    for msg in messages:
        formatted_messages.append(msg)

    result = pipe(
        formatted_messages,
        max_new_tokens=150
    )

    return result[0]["generated_text"][-1]["content"]