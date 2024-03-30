# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

for num in range(0, 11):
    print(num ** 2)

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
    
lista = ['Python', 'Java', 'C++', 'Javascript']

lista.remove('C++')
lista.append('Ruby')

print(lista)

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, 
# autor e ano de publicação. Imprima cada informação.

livro = {
    'titulo': 'Hábitos Atomicos',
    'autor': 'Autor1',
    'ano_publicacao': 2009
}

for chave, valor in livro.items():
    print(f'{chave}: {valor}')

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.



# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.