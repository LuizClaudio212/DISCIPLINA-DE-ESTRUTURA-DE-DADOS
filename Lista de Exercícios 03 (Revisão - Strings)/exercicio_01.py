"""
1. Uma palavra é palíndroma se ela não se altera quando lida da direita para esquerda. Por exemplo, raiar é palíndroma.
Escreva um programa que verifique se uma palavra dada é palíndroma.
"""

def verificar_palavra_palindroma(palavra):
    verificar_palavra = palavra[::-1]
    if verificar_palavra == palavra:
        return True
    return False
    

def input_palavra():
    return input("Digite uma palavra para saber se ela e palindroma: ")


def menu():
    palavra = input_palavra()
    palindroma = verificar_palavra_palindroma(palavra.upper())
    if palindroma is True:
        print(f"A palavra {palavra} é palindroma.")
    else:
        print(f"A palavra {palavra} não é palindroma.")


if __name__ == "__main__":
    menu()