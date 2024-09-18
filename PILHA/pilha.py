from excecao import *
class PilhaArray:
    
    def __init__(self):
        self._pilha = []
    
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

        