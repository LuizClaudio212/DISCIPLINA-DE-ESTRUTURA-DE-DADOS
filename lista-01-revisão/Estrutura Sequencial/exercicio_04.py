"""
Exercicio 04: Faça um Programa que peça a temperatura em graus Farenheit, transforme e
mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)
"""
#Essa função recebe o valor de farenheit e retorna o mesmo.
def input_farenheit():
    try:
        farenheit = float(input("Insira a temperatura Farenheit que você deseja converter para graus Celsius: "))
        return farenheit
    except ValueError:
        print("Valor invalido!")
        return None
    

#Essa função converte o valor de farenheit para graus celsius.
def conversao_farenheit_para_celsius(farenheit):
    return (5 * (farenheit - 32) / 9)


def menu():
    farenheit = input_farenheit()
    if farenheit is None:
        print("Erro! Não foi possivel realizar a conversão.")
    else:
        celsius = conversao_farenheit_para_celsius(farenheit)
        print(f"{farenheit:.2f}F graus farenheit convertidos em graus celsius e igual a: {celsius:.2f}C")


if __name__ == "__main__":
    menu()