"""
Args
"""


def soma_numeros(numero1: int, numero2: int, numero3: int):
    return numero1 + numero2 + numero3


def soma_numeros_args(*args, ):
    print(args)


def soma_todos(*args):
    return sum(args)


print(f'Soma dos numeros: {soma_numeros(10, 1, 1)}')

# Args organiza os parametros em tuplas
soma_numeros_args(3, 4, 5, 68)
soma_numeros_args(0, 3, 1, 45, 56)

print(f'O resultado da soma e: {soma_todos(10, 10, 20)}')
