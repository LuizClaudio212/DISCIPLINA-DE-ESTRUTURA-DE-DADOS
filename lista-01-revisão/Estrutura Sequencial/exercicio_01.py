"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
"""
Essa função recebe as medias bimestrais e vai somando os valores em soma_das_notas depois retorna a media bimestral
"""
def inputnotas():
    soma_das_notas = 0
    for n in range (1, 4+1):
        try:
            nota = float(input(f"Qual sua nota do {n} bimestre?: "))
            soma_das_notas += nota
        except ValueError:
            print(f"Erro! Nota do {n} bimestre não registrada com exito!")

    return soma_das_notas / 4

def menu():
    media = inputnotas()
    print(f"Sua média bimestral é: {media}")

if __name__ == "__main__":
    menu()