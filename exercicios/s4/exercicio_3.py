"""
Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar
"""

def verifica_numero_par_impar(numero):
  if numero % 2 == 0:
    return print(f'O numero {numero} é PAR')
  else:
    return print(f'O numero {numero} é IMPAR')	

print('Ola! Digite um numero e eu vou dizer se ele é PAR ou IMPAR!')
numeroDigitado = int(input())
verifica_numero_par_impar(numeroDigitado)