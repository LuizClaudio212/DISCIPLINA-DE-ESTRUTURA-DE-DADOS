"""
Faça uma função eh_bissexto(ano) que recebe um ano como parâmetro e retorna True se o ano for bissexto e
False caso contrário
"""

def eh_bissexto(ano):
    if ano % 4 == 0:
        return True
    else:
        return False

print(eh_bissexto(1932))