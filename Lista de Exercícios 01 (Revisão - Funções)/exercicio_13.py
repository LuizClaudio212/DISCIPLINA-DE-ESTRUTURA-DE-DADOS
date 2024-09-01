"""
13. A sequência de Fibonacci é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual, cada termo
subsequente corresponde a soma dos dois anteriores. Faça uma função Fibonacci(termo) que dado um número N
representando o n-ésimo termo da sequencia de Fibonacci, retorna a soma desses termos. 
Exemplo: Fibonacci(7) = 20 ,pois os 7 primeiros termos da sequencia de Fibonacci são “0,1, 1, 2, 3, 5, 8” 
e sua soma é 20.
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def soma(i):
    sum = 0

    for v in range(i):
        sum += fibonacci(v)

    return sum

print(soma(7))