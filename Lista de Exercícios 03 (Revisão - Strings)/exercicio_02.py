"""
Um dos recursos disponibilizados pelos editores de texto mais modernos é a determinação do número de palavras de um
texto. Escreva um programa que determine o número de palavras de um texto dado.
"""

def input_texto():
    return input("Digite seu texto: ")


def numeros_de_palavras_txt(txt):
    palavras = txt.split()
    return len(palavras)


def menu():
    txt = input_texto()
    num_palavras = numeros_de_palavras_txt(txt)

    print(f"Seu texto tem {num_palavras} palavras.")


if __name__ == "__main__":
    menu()