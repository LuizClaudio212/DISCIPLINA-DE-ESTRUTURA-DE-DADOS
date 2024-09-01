"""
5. Faça uma função maior_de_2(num1, num2) que, dados dois números, retorna o maior deles.

"""

def maior_de_2(num1, num2):
    maior = num1
    if num2 > maior:
        maior = num2
    return maior

print(maior_de_2(5, 6))