"""
11. Faça uma função soma_numeros(numero) que recebe como parâmetro um número N, calcula a soma de 
todos os números de 1 até ele e retorna o valor da soma. Exemplo: soma_numeros(7) = 28 , 
pois 1+2+3+4+5+6+7=28.
"""

def soma_numeros(numero):
    soma_numero = 0
    for i in range(1, numero+1):
        soma_numero += i
    return soma_numero

print(soma_numeros(5))

