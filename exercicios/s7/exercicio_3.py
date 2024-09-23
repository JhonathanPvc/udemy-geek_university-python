"""
Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor
"""


def retorna_maior_numero(numeros: list[int]) -> int:
    return max(numeros)


lista_numeros: list[int] = [9, 14, 88, 5, 6, 7, 99, 64, 56]

print(f'A lista e: {lista_numeros}')
print(f'O maior numero e: {retorna_maior_numero(lista_numeros)}')
