from excecao import *


class PilhaArray:
    
    def __init__(self):
        self._pilha = []
        self._maiores = []
    
    def __repr__(self) -> str:
        return f'{self._pilha}'
    
    def __len__(self):
        return len(self._pilha)
    
    def size(self):
        return self.__len__()
    
    def push(self, e):
        self._pilha.append(e)

    def is_empty(self):
        return len(self._pilha) == 0

    def top(self):
        if self.is_empty():
            raise PilhaVazia("A pilha está vazia")
        return self._pilha[-1]

    def pop(self):
        if self.is_empty():
            raise PilhaVazia("A pilha estã vazia")
        return self._pilha.pop()

cont = 0
pilha = PilhaArray(); 
maiores = PilhaArray()
pilha.push('5'); 
if '5' > maiores.top(): maiores.push('5')


pilha.push('3'); 
if '3' > maiores.top(): maiores.push('3')

pilha.push('7'); 
if '7' > maiores.top(): maiores.push('7')

nova_pilha = PilhaArray()

if pilha.is_empty == False and cont == 0:
    nova_pilha.push(pilha.top())
    cont +=1

print(pilha)
print(nova_pilha)


