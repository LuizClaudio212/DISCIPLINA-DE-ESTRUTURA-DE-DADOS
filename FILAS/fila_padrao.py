

class EmptyQueueError(Exception):
    ...


class FilaArray:
    
    def __init__(self) -> None:
        self._fila = []
    
    def __repr__(self) -> str:
        return f'{self._fila}'
    
    def enqueue(self, valor: any) -> None:
        self._fila.append(valor)
    
    def dequeue(self) -> None:
        if self.is_empty == True:
            raise EmptyQueueError("A fila está vazia.")
        return self._fila.pop(0)
    
    def is_empty(self) -> bool:
        
        return len(self._fila) == 0
    
    def first(self) -> any:
        if self.is_empty():
            raise EmptyQueueError("A fila está vazia.")
        return self._fila[0]
    
    def size(self) -> int:
        return len(self._fila)
    
    def __len__(self) -> int:
        return self.size()
    

# Exemplo de uso:
fila = FilaArray()
fila.enqueue(5)
print(fila)
fila.enqueue(3)
print(fila)
fila.dequeue()
print(fila)
fila.enqueue(2)
print(fila)
fila.enqueue(8)
print(fila)
fila.dequeue()
print(fila)
fila.dequeue()
print(fila)
fila.enqueue(9)
print(fila)
fila.enqueue(1)
print(fila)
fila.dequeue()
print(fila)
fila.enqueue(7)
print(fila)
fila.enqueue(6)
print(fila)
fila.dequeue()
print(fila)
fila.dequeue()
print(fila)
fila.enqueue(4)
print(fila)
fila.dequeue()
print(fila)
fila.dequeue()
print(fila)