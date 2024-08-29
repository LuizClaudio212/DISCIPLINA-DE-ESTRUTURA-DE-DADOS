"""
Exercicio 03: Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
#Essa função recebe um numero de 1 a 7 e retorna.
def input_numero():
    numero = int(input("Digite um número de 1 ate 7 para saber o seu dia: "))

    if numero <= 0 or numero > 7:
        return None
    else:
        return numero

#Essa função recebe o valor do número e busca na lista dos dias da semana o número correspondente ao dia.
def dia_correspondente(numero):
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]
    return dias_semana[numero-1]


def menu():
    numero = input_numero()
    if numero is None:
        print("Valor invalido!")
    else: 
        dia_semana = dia_correspondente(numero)
    
        print(f"O dia que corresponde ao número {numero} e {dia_semana}.")


if __name__ == "__main__":
    menu()