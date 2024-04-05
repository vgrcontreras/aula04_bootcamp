# 1) Escreva uma função que receba uma lista de números e retorne a soma de todos os números.


"""def soma_numeros_lista(lista: list):
    return sum(lista)

lista_numeros = [1, 3, 10 , 50, 33, 2.2, 4]

resultado = soma_numeros_lista(lista_numeros)
print(resultado)"""

# 2) Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

"""def check_prime_number(num: int) -> bool:
    if num > 1:
        # Iterate from 2 to n // 2
        for i in range(2, (num//2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
            
        else:
            return True
    else:
        return False

resultado = check_prime_number(7)
print(resultado)"""

# 3) Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

"""def invert_string(string: str) -> str:
    inverted_string = string[::-1]

    return inverted_string

resultado = invert_string('Hello World')
print(resultado)
"""
# 4) Implemente uma função que receba dois argumentos: uma lista de números e um número. 
#A função deve retornar todas as combinações de pares na lista que somem ao número dado.



# 5) Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

# def get_keys_of_dicitionary(dictionary: dict) -> list:

"""thisdict = {
"zeta": "Ford",
"arroz": "Mustang",
"victor": 1964
}

def get_sorted_keys_in_dict(dictionary: dict) -> list:
    key_list = [key for key, value in dictionary.items()]

    key_list.sort()

    return key_list

resultado = get_sorted_keys_in_dict(thisdict)
print(resultado)"""