"""
12. Faça uma função eh_primo(numero) que recebe como parâmetro um número inteiro e retorna True se ele é 
um número primo e False caso contrário. Um número é primo quando ele é divisível somente por um e por ele 
mesmo.
"""

def eh_primo(numero):
    if numero <= 1:
        return False
    
    if numero == 2:
        return True
    
    if numero % 2 == 0:
        return False
    
    # Verifica divisibilidade apenas até a raiz quadrada do número
    limite = int(numero**0.5) + 1
    for i in range(3, limite, 2):
        if numero % i == 0:
            return False
    return True


print(eh_primo(47))
print(eh_primo(1))
print(eh_primo(2))