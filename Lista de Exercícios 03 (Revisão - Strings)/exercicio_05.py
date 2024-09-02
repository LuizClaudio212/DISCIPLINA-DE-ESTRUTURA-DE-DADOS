"""
5. As normas para a exibição da bibliografia de um artigo científico, de uma monografia, de um livro texto, etc., exigem que o
nome do autor seja escrito no formato último sobrenome, sequência das primeiras letras do nome e dos demais
sobrenomes, seguidas de ponto final. Por exemplo, Antônio Carlos Jobim seria referido por Jobim, A. C.. Escreva um
programa que receba um nome e o escreva no formato de bibliografia.
"""

def input_nome():
    return input("Qual é o seu nome?: ")

def nome_formato_bibliografia(nome):
    nome_bibliografia = []

    partes_nome = nome.split()
    ultimo_sobrenome = partes_nome[-1]

    partes_nome.pop()

    iniciais = [parte[0] + '.' for parte in partes_nome]


    nome_bibliografia = f"{ultimo_sobrenome}, {' '.join(iniciais)}."
    
    return nome_bibliografia


def menu():
    nome = input_nome()

    nome_bibliofrafico = nome_formato_bibliografia(nome)

    print(nome_bibliofrafico)


if __name__ == "__main__":
    menu()