"""
Exercicio 5: Escreva uma função em que, dada uma variável x com algum valor inteiro, temos um novo x de acordo com a seguinte
regra:
Se x é par, x = x / 2;
Se x é impar, x = 3 * x + 1;
Imprime x; 
"""

def inputx():
    """
    Solicita ao usuário para inserir um valor inteiro.
    Retorna o valor inserido como um inteiro. Se a entrada não for um número inteiro,
    imprime uma mensagem de erro e retorna None.
    """
    try:
        x = int(input("Insira um valor inteiro: "))
        return x
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        return None

def validacao_do_x(x):
    """
    Aplica a regra de transformação ao valor de x.
    Se x for par, retorna x dividido por 2.
    Se x for ímpar, retorna 3 * x + 1.
    Se x for None, retorna None.
    """
    if x is None:
        return None
    if x % 2 == 0:
        return x / 2
    else:
        return 3 * x + 1

def imprimirx(x):
    """
    Imprime o valor de x. Se x for None, imprime uma mensagem de erro.
    """
    if x is not None:
        print(x)
    else:
        print("Erro!")

def menu():
    """
    Função principal que coordena a execução do programa:
    - Solicita a entrada do usuário.
    - Processa o valor inserido conforme a regra definida.
    - Imprime o resultado.
    """
    x = inputx()
    x = validacao_do_x(x)
    imprimirx(x)

if __name__ == "__main__":
    menu()
