"""
Exercicio 01:Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.
"""
#Essa função recebe o valor de nota fazendo a validação da mesma.
def input_nota():
    nota = float(input("Informe uma nota entre zero e dez: "))
    while nota <0 or nota >10:
        print("Valor invalido!")
        nota = float(input("Informe uma nota entre zero e dez: "))
    return nota


def menu():
    nota = input_nota()
    print(nota)


if __name__ == "__main__":
    menu()