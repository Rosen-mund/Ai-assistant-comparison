blocked_keywords = [
    "hack",
    "malware",
    "bomb",
    "ransomware",
    "steal passwords",
    "make virus"
]

def is_safe(prompt):

    prompt = prompt.lower()

    for word in blocked_keywords:
        if word in prompt:
            return False

    return True