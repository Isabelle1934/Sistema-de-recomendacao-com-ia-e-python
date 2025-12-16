print("Projeto rodando corretamente!")
from src.agent import real_estate_agent

print("=== Sistema de Recomendação de Apartamentos ===")

user = input("Descreva o imóvel que você procura:\n> ")

resultado = real_estate_agent(user)

print("\nRecomendações:\n")
print(resultado)
