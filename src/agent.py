from src.llm_intent import extract_intent
from src.recommender import filter_properties
from src.explainer import explain_recommendations

def real_estate_agent(user_message):

    # O LLM entende a intenção
    intent = extract_intent(user_message)

    # O python está filtrando os imóveis
    properties = filter_properties(intent)

    if properties.empty:
        return "Nenhum imóvel encontrado com esses critérios."

    # O LLM explica o resultado
    explanation = explain_recommendations(intent, properties)
    return explanation
