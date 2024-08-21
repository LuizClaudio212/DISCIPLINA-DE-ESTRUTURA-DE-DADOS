#Exercicio 01 : Imprima a soma dos números entre 150 e 300.

#Função que calcula a soma dos números no intervalo de 150 a 300
def soma():
    resultado = 0
    for n in range (150, 301):
        resultado += n
    return resultado

#Função que chama a função soma() para obter o resultado da soma e, em seguida, imprime esse resultado.
def menu():
    resultado = soma()
    print(resultado)

if __name__ == "__main__":
    menu()