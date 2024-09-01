"""
Faça uma função eh_data_valida(dia, mes, ano) que recebe como parâmetro três valores, representando dia, 
mês e ano. Essa função deve retornar True se os valores formarem uma data válida, e False caso contrário
"""

def eh_data_valida(data):
    dia, mes, ano = data
    if dia >0 and dia <=31 and mes >0 and mes <=12 and ano >0:
        return True
    return False

data = [12, 12, 2004]
data2 = [32, 13, 2002]
print(eh_data_valida(data))
print(eh_data_valida(data2))