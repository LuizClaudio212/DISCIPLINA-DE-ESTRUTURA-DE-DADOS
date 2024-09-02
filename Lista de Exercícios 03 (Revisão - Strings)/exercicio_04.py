"""
4. As companhias de transportes aéreos costumam representar os nomes dos passageiros no formato último
sobrenome/nome. Por exemplo, o passageiro Carlos Drumond de Andrade seria indicado por Andrade/Carlos. Escreva um
programa que lê um nome e o escreve no formato acima.
"""

def input_nome():
    return input("Qual é o seu nome?: ")


def formato_sobrenome_nome(nome):
    nome_completo = nome.split()
    if len(nome_completo) <2:
        raise ValueError("O nome deve ter pelo menos um sobrenome e um nome.")
    
    primeiro_nome = nome_completo[0]
    sobrenome = nome_completo[1]

    return f"{sobrenome}/{primeiro_nome}".lower()


def menu():
    nome = input_nome()

    formato = formato_sobrenome_nome(nome)

    print(formato)


if __name__ == "__main__":
    menu()