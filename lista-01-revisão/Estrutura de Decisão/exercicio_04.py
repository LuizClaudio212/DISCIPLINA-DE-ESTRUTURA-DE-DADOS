"""
Exercicio 04: Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem um

triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados
for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
#Essa função recebe os valores dos lados do triangulo e retorna eles.
def input_lados_do_triangulo():
    triangulo = []
    for v in range(1, 4):
        lado = float(input(f"Informe o valor do {v} lado do triangulo: "))
        triangulo.append(lado)
    if ((triangulo[0] + triangulo[1]) > triangulo[2]) or ((triangulo[0] + triangulo[2]) > triangulo[1]) or ((triangulo[1] + triangulo[2]) > triangulo[0]):
        return triangulo
    else:
        return None

#Essa função descobre o tipo de triangulo usando os lados como base.
def tipo_do_triangulo(lados_do_triangulo):
    l1, l2, l3 = lados_do_triangulo
    if (l1 == l2 and l1 == l3):
        return "Triângulo Equilátero"
    elif (l1 == l2 or l1 == l3 or l2 == l3):
        return "Triângulo Isósceles"
    elif (l1 != l2 and l1 != l3 and l2 != l3):
        return "Triãngulo Escaleno"
    

def menu():
    lados_do_triangulo = input_lados_do_triangulo()
    if lados_do_triangulo is None:
        print("Erro!")
    else:
        print(tipo_do_triangulo(lados_do_triangulo))

if __name__ == "__main__":
    menu()