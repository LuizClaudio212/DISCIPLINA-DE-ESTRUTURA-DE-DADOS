"""
6. Faça uma função maior_de_3(num1, num2, num3)que, dados três números, retorna o maior deles.
"""

def input_numeros():
    numeros = []
    for n in range(1, 4):
        numero = int(input(f"Qual e o {n} valor?: "))
        numeros.append(numero)
    return numeros


def maior_de_3(numeros):
    maior = numeros[0]
    for v in numeros:
        if v > maior:
            maior = v
        

    return maior

numeros = input_numeros()

maior = maior_de_3(numeros)
print(maior)