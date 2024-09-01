"""
3. Faça uma função par_ou_impar(numero) que recebe um número inteiro e retorna “par” ou “impar”.
"""
def par_ou_impar(numero):
    if numero %2 == 0:
        return "Par"
    else:
        return "Impar"
    
print(par_ou_impar(2))