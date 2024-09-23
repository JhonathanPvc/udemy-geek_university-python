"""
Kwargs 

O kwargs exige que os parametros sejam nomeados, assim transformando o retorno em um dicionario
"""

# Exemplo 1


def cores_favoritas(**kwargs):
    print(kwargs)


cores_favoritas(jhon='Azul', isis='Amarelo', daiane='Rosa')
