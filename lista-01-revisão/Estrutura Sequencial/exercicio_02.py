"""
Exercicio 2: Faça um Programa que converta metros para centímetros.
"""

#Essa função recebe e retorna o valor de metros.
def inputmetros():
    try:
        metros = float(input("Digite a quantidade em metros que vai ser convertida em centimetros(Ex: 1.0): "))
        return metros
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return None
    

#Essa função recebe o valor de metros e retorna o valor convertido em centimetros.
def metros_para_cm(metros):
    return metros * 100


def menu():
    metros = inputmetros()
    if metros is None:
        print("Erro! Não foi possível realizar a conversão.")
    else:
        cm = metros_para_cm(metros)
        print(f"O resultado é {cm:.2f} centimetros.")

if __name__ == "__main__":
    menu()