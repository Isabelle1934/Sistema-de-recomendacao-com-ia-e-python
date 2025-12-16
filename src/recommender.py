import pandas as pd

def filter_properties(intent):
    # Carrega os dados
    df = pd.read_csv("data/properties.csv")

    # Começa com TODOS os imóveis
    filtered = df

    # Filtro por quartos
    if intent.get("quartos"):
        filtered = filtered[filtered["quartos"] == intent["quartos"]]

    # Filtro por preço
    if intent.get("preco_max"):
        filtered = filtered[filtered["preco"] <= intent["preco_max"]]

    # Filtro por metrô
    if intent.get("perto_do_metro"):
        filtered = filtered[filtered["perto_do_metro"] == True]

    return filtered
