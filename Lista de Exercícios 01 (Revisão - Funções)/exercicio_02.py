"""
2. Faça uma função eh_par(numero) que recebe um número inteiro e retorna True (verdadeiro) se o número for par,
 False
(falso) caso contrário.
"""

def eh_par(numero):
    if numero %2 == 0:
        return True
    else:
        return False

bool = eh_par(3)
print(bool)