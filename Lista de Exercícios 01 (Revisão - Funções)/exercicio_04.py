"""
4. Escreva uma função compare(a, b) que recebe dois números a e b como parâmetro e retorna 1 se a > b, 
0 se a == b, e -1 se a < b.
"""

def compare(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

print(compare(1,4))