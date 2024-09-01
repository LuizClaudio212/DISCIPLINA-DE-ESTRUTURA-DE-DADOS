"""
Faça uma função dia_da_semana(dia) que recebe como parâmetro um número e retorna o dia correspondente da
semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve retornar valor inválido.
"""

def dia_da_semana(dia):
    Dias = ["Domingo", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado"]
    return Dias[dia-1]

def input_numero_semana():
    numero = int(input("Informe o numero para saber o seu dia da semana correspondente: "))
    return numero



dia_semana = dia_da_semana(input_numero_semana())

print(dia_semana)
