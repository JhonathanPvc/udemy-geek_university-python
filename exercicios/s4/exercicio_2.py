"""
Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule 
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o 
número é inválido.
"""

def calcula_numero(numero):
  if numero > 0:
    print(f'O numero {numero} é POSITIVO!')
    print(f'Sua raiz quadrada é: {retorna_quadrado(numero)}')
  else:
    print(f'O numero {numero} é NEGATIVO!')
    
def retorna_quadrado(numero):
  return float(numero ** 0.5)

print('\nOla! Digite um numero e vou dizer se ele é POSITIVO ou NEGATIVO!')
numero: int = int(input())
calcula_numero(numero)