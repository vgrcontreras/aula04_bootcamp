"""
6. Eliminação de Duplicatas
Objetivo: Dada uma lista de emails, remover todos os duplicados.
"""

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]



"""7. Filtragem de Dados
Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18."""

# idades = [22, 15, 30, 17, 18]

# idades_validas = []

# for idade in idades:
#     if idade > 18:
#         idades_validas.append(idade)

# ## Mesma solução utilizando List Comprehension
# # idades_validas = [idade for idade in idades if idade > 18]

# print(idades_validas)

"""8. Ordenação Personalizada
Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome."""

# pessoas = [
#     {"nome": "Victor", "idade": 30},
#     {"nome": "Juliana", "idade": 25},
#     {"nome": "Alice", "idade": 20}
# ]

# pessoas.sort(key=lambda pessoa: pessoa["nome"])

# print(pessoas)

"""9. Agregação de Dados
Objetivo: Dado um conjunto de números, calcular a média."""

# minha resolução
# numeros = [10, 20, 30, 40, 50]

# num_sum = 0

# for num in numeros:
#     num_sum += num

# resultado = num_sum / len(numeros)
# print(resultado)

# #resolução bootcamp
# numeros = [10, 20, 30, 40, 50]
# media = sum(numeros) / len(numeros)

# print("Média:", media)

"""10. Divisão de Dados em Grupos
Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares."""

# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# valores_pares = [valor for valor in valores if valor % 2 == 0]
# valores_impares = [valor for valor in valores if valor % 2 != 0]

# print("Pares:", valores_pares)
# print("Ímpares:", valores_impares)

"""11. Atualização de Dados
Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
"""

# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# # Atualizar o preço do produto com id 2 para 90

# produtos[1].update({'preço': 90})

# print(produtos)

"""12. Fusão de Dicionários
Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
"""

# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# merged_dict = dicionario1 | dicionario2

# print(merged_dict)

""""13. Filtragem de Dados em Dicionário
Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0."""

"""14. Extração de Chaves e Valores
Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
"""

"""15. Contagem de Frequência de Itens
Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário."""