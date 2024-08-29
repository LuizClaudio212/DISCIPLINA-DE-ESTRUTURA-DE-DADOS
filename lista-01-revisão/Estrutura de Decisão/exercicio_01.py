"""
Exercicio 01: 1. Faça um programa para a leitura de duas notas parciais de um aluno. O programa
deve calcular a média alcançada por aluno e apresentar:
A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
A mensagem “Reprovado”, se a média for menor do que sete;
A mensagem “Aprovado com Distinção”, se a média for igual a dez.
"""
#Essa função recebe e retorna as notas.
def input_notas():
    notas = list()
    for n in range(1, 2+1):
        try:
            nota = float(input(f"Quanto você tirou na {n} nota?: "))
            if nota < 0:
                print("A nota precisa ser maior ou igual a 0.")
            else:
                notas.append(nota)   
        except ValueError:
            print("Erro! Valor invalido.")
    return notas

#Essa função calcula a media das notas.
def calcular_media(notas):
    return sum(notas) / len(notas)


def menu():
    notas = input_notas()
    media = calcular_media(notas)

    if media >= 7 and media <10:
        print("Aprovado!")
    elif media <7:
        print("Reprovado!")
    elif media == 10:
        print("Aprovado com Distinção")


if __name__ == "__main__":
    menu()