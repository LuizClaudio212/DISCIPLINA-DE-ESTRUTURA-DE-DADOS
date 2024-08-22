"""Exercicio 04:Imprima a seguintetabela usando fors encadeados:
1
2 4
3 6 9
4 8 12 16
n n*2 n*3 .... n*n""" 

# Número de linhas da tabela
num_linhas = 4

# Loop para cada linha
for n in range(1, num_linhas+1):
    for i in range(1, n+1):
        print(n * i, end=' ')
    print()
