"""
  Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""


def retorna_numero_maior(numero1, numero2):
    numero_maior: int = 0
    numero_menor: int = 0

    if numero1 > numero2:
        numero_maior = numero1
        numero_menor = numero2
    elif numero1 == numero2:
        return print('Os numeros são IGUAIS!')
    else:
        numero_maior = numero2
        numero_menor = numero1

    return print(f'O numero {numero_maior} é maior que {numero_menor}')


print('\nOla! Digite 2 numeros e eu vou dizer qual é o maior')
print('Digite o primeiro numero:')
numero1: int = int(input())
print('Digite o segundo numero:')
numero2: int = int(input())

retorna_numero_maior(numero1, numero2)
