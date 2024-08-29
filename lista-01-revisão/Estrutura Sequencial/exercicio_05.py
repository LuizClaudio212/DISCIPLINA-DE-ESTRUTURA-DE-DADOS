"""
Exercicio 05: Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
#Essa função recebe e retorna a altura.
def input_altura():
    try:
        altura = float(input("Qual é a sua altura? [Ex 1.80]: "))
        return altura
    except ValueError:
        print("Valor invalido!")
        return None

#Essa função recebe e retorna o sexo.
def input_sexo():
    sexo = input("Qual seu sexo?[Ex M/F]: ").upper().strip()
    if sexo in ["M", "F"]:
        return sexo
    else:
        print("Entrada inválida. Por favor, insira 'M' ou 'F'.")
        return None

#Essa função realiza o calculo do peso ideal.
def conversao_peso_ideal(altura, sexo):
    if sexo == "M":
        return (72.7*altura) - 58
    else:
        return (62.1*altura) - 44.7


def menu():
    altura = input_altura()
    sexo = input_sexo()
    if altura is None or sexo is None:
        print("Não foi possivel realizar a conversão!")
    else:
        peso_ideal = conversao_peso_ideal(altura, sexo)
        print(f"Seu peso ideal é: {peso_ideal:.2f}")


if __name__ == "__main__":
    menu()