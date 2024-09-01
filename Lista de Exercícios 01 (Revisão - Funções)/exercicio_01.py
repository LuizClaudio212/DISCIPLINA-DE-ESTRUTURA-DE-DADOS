"""
Exercicio 01. Faça uma função fatorial(n) que, dado um número N, calcule e retorne o fatorial de N. 
O fatorial de um número natural n,
representado por n!, é o produto de todos os inteiros positivos menores ou iguais a n. 
Exemplos: 5! = 1 x 2 x 3 x 4 x 5 = 120
0! = 1
"""
def fatorial(n):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    return fatorial

print(fatorial(3))

