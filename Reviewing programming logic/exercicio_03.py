#Exercicio 03. Calcule o fatorial de um numero qualquer. O fatorial de um número n é n * (n-1) * (n-2) * ... * 1.

def input_numero_qualquer():
    numero_qualquer = int(input("Digite um número inteiro qualquer para calcular seu fatorial: "))
    return numero_qualquer

def calcular_fatorial(numero_qualquer):
    if numero_qualquer < 0:
        return "Não é possivel calcular o fatorial de um número negativo!"
    elif numero_qualquer == 0:
        return 1
    else:
        fatorial = 1
        for n in range(1, numero_qualquer+1):
            fatorial *= n
        return fatorial
    

def menu():
    numero_qualquer = input_numero_qualquer()

    fatorial = calcular_fatorial(numero_qualquer)
    
    print(f"O fatorial de {numero_qualquer} é {fatorial}")


if __name__ == "__main__":
    menu()