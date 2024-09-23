"""
Funcoes com parametro
"""


def retorna_quadrado(numero: int):
    return numero ** 2


def multiplica_mensagem(numero1: int, numero2: int, mensagem: str):
    return (numero1+numero2) * mensagem


print(f'Retorno da funcao: {retorna_quadrado(7)}')
print(f'Retorno da funcao: {multiplica_mensagem(3, 5, ' Multiplica! ')}')
