"""
  if, else, elif
"""

print('Ola! \nDigite sua idade:')
idade = int(input())

if idade < 18:
    print('Menor de idade!')
elif idade == 18:
    print('Tem 18 anos!')
else :
    print('Maior de idade!')