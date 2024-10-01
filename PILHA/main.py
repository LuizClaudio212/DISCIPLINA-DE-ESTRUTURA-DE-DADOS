import pilha as p
"""
p = p.PilhaArray() # conteúdo [ ]
p.push(5) # conteúdo [5]
p.push(3) # conteúdo [5, 3]
print(len(p)) # conteúdo [5, 3]; retorna 2
print(p.pop()) # conteúdo [5]; retorna 3
print(p.is_empty()) # conteúdo [5]; retorna False
print(p.pop()) # conteúdo [ ]; retorna 5
print(p.is_empty()) # conteúdo [ ]; retorna True
p.push(7) # conteúdo [7]
p.push(9) # conteúdo [7, 9]
print(p.top()) # conteúdo [7, 9]; retorna 9
p.push(4) # conteúdo [7, 9, 4]
print(p.size()) # conteúdo [7, 9, 4]; retorna 3
print(p.pop()) # conteúdo [7, 9]; retorna 4
p.push(6) # conteúdo [7, 9, 6]
p.push(8) # conteúdo [7, 9, 6, 8]
print(p.pop()) # conteúdo [7, 9, 6]; retorna 8
"""
#Invertendo dados
"""
Protocolo LIFO, Uma pilha pode ser ultilizada para inverter dados

"""

def inverte_texto(texto):
    p1 = p.PilhaArray()
    for letra in texto:
        p1.push(letra)
    palavra = ''
    while not p1.is_empty():
        palavra += p1.pop()
    return palavra
        

text = inverte_texto('abc')
print(text)


#inverter arquivo

def inverte_arquivo(nome_arquivo):
    p1 = p.PilhaArray()
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                p1.push(linha.rstrip('\n'))
        
        with open(nome_arquivo, 'w') as output:
            while not p1.is_empty():
                output.write(p1.pop() + '\n')
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
        
nome_arquivo = 'test.txt'
inverte_arquivo(nome_arquivo)

"""
Quais dessas expressões estão corretas? 1. ()(()){([()])} 2. ((()(()){([()])})) 3. )(()){([()])} 4. ({[])} 5. (
Como seria o algoritmo para verificar se os delimitadores de uma expressão estão corretos ou não?
"""
#Algoritmo para verificar delimitadores

def is_matched(expr):
    abre = '({[' # delimitadores - abertura
    fecha = ')}]' # delimitadoers - fechamento
    pilha = p.PilhaArray()
    for d in expr:
        if d in abre:
            pilha.push(d) # push o delimitador de abertura
        elif d in fecha:
            if pilha.is_empty():
                return False # não bate
        if fecha.index(d) != abre.index(pilha.pop()):
            return False # não bate
    return pilha.is_empty() # tem mais delimitadores na pilha?

