"""
Exercicio 02: Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
#Essa função recebe e retorna os três números
def input_numeros():
    numeros = []
    for n in range (1, 3+1):
        numero = int(input(f"Digite o {n} número: "))
        numeros.append(numero)
    return numeros

#Essa função retorna o maior e o menor número entre os números
def maior_e_menor_numero(numeros):
    maior = numeros[0]
    menor = numeros[0]
    for v in numeros:
        if v > maior:
            maior = v
        elif v < menor:
            menor = v
    return maior, menor


def menu():
    numeros = input_numeros()
    maior, menor = maior_e_menor_numero(numeros)

    print(f"O maior número entre os valores é: {maior}")
    print(f"O menor número entre os valores é: {menor}")


if __name__ == "__main__":
    menu()