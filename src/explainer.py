import ollama

def explain_recommendations(apartments):
    prompt = f"""
Explique os apartamentos abaixo de forma clara e objetiva para um cliente:

{apartments}
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
