"""
3. Escreva uma função que recebe uma string e imprime somente a última palavra da mesma. Exemplo: Se a string digitada
for "José da Silva", deverá ser impresso na tela a substring "Silva".
"""

def saber_ultima_palavra(frase):
    palavra = frase.split()
    return palavra[-1]


def input_frase():
    return input("Digite uma frase: ")


def menu():
    frase = input_frase()
    ultima_palavra = saber_ultima_palavra(frase)
    print(ultima_palavra)


if __name__ == "__main__":
    menu()