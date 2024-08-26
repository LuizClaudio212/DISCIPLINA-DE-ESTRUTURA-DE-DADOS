"""
Exercicio 3: Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

"""
#Essa função recebe a quantidade de valor por hora e retorna o valor
def qtd_valor_por_hora():
    try:
        valor_por_hora = float(input("Quanto você ganha por hora?: "))
        return valor_por_hora
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return None

#Essa função recebe a quantidade de horas trabalhadas no mes e retorna o valor
def qtd_horas_trabalhadas_no_mes():
    try:
        horas_trabalhadas_no_mes = float(input("Quantas horas você trabalha por mes?(Ex: 160): "))
        return horas_trabalhadas_no_mes
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return None

#Essa função realiza o calculo do salario
def calculo_do_salario(valor_por_hora, horas_trabalhadas_no_mes):
    return valor_por_hora * horas_trabalhadas_no_mes


def menu():
    valor_por_hora = qtd_valor_por_hora()
    horas_trabalhadas_no_mes = qtd_horas_trabalhadas_no_mes()

    if valor_por_hora is None or horas_trabalhadas_no_mes is None:
        print("Erro! Não foi possível realizar o calculo do salário.")
    else:
        salario = calculo_do_salario(valor_por_hora, horas_trabalhadas_no_mes)
        print(f"O total do seu salário é: {salario:.2f} R$")

if __name__ == "__main__":
    menu()