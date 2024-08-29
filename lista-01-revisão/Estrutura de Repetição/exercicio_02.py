"""
Exercicio 02: Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.
"""
#Essa função recebe e retorna o nome do usuario.
def input_nome_usuario():
    nome = input("Informe seu nome: ")
    return nome.upper()


#Essa função recebe e retorna a senha do usuario.
def input_senha_usuario():
    senha = input("Informe qual vai ser sua senha: ")
    return senha.upper()

#Estrutura de repetição para validar se a senha e diferente do nome
def menu():
    while True:
        nome = input_nome_usuario()
        senha = input_senha_usuario()

        if senha != nome:
            print("Cadastro realizado com sucesso!")
            break  
        else:
            print("Erro! Sua senha não pode ser igual ao seu nome.")


if __name__ == "__main__":
    menu()