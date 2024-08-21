#Exercicio 02: Armazenar em uma lista todos os múltiplos de 3, entre 1 e 100. Imprima cada elemento da lista, um por linha.

#Essa função retorna uma lista contendo todos os múltiplos de 3 entre 1 e 100.
def multiplos_de_tres():
    mult_de_tres = list()
    for n in range (1, 101):
        if n % 3 == 0:
            mult_de_tres.append(n)
    return mult_de_tres

#Essa função imprime cada número da lista, um por linha.
def ImprimirNumeros(numeros):
    for n in numeros:
        print(n)

#Essa função obtém a lista de múltiplos de 3 e a imprime.
def menu():

    multiplos = multiplos_de_tres()

    ImprimirNumeros(multiplos)

if __name__ == "__main__":
    menu()