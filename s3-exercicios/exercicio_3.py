"""
  Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos
"""

soma = 0
def soma_valor(valor):
  retorno = soma+(valor ** 2)
  return retorno

print('Ola! \n Vou pedir para vc digitar 3 valores.')
print('\n')
for x in range(3):
  print(f'Digite o valor {x+1}: ')
  numeroDigitado = int(input())
  soma = soma_valor(numeroDigitado)

print(f'A soma dos quadrados digitados foi de: {soma}')