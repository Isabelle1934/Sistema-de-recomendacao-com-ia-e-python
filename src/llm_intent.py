import ollama
import json

def extract_intent(user_message):
    prompt = f"""
Extraia as informações do texto abaixo e retorne APENAS um JSON.

Campos:
- quartos (int ou null)
- preco_max (int ou null)
- perto_do_metro (true ou false)

Texto:
"{user_message}"
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {
    "quartos": None,
    "preco_max": None,
    "perto_do_metro": False
}

