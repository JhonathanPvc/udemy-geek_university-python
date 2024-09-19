"""
Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo 
seu valor na tela, até que seu valor seja 100000 (cem mil)
"""

print('De 1000 em 1000 até 100.000!\n')

contador: int = 0

while contador <= 100000:
    print(f'O contador esta em {contador}')
    contador = contador + 1000

print('\nFIM')
