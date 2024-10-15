from collections import deque

class PilhaComFila:
    def __init__(self):
        self._fila = deque()  # Usando deque para a fila (deque tem operações O(1) nas extremidades)

    def push(self, e):
        """Insere um elemento 'e' na pilha."""
        self._fila.append(e)  # Enfileira o novo elemento (inserção ao final da fila)
        
        # Reordenar a fila para que o último elemento inserido seja o primeiro a sair (LIFO)
        for _ in range(len(self._fila) - 1):
            self._fila.append(self._fila.popleft())  # Mover os elementos anteriores para o final da fila

    def pop(self):
        """Remove e retorna o elemento no topo da pilha."""
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._fila.popleft()  # Remover o primeiro elemento da fila, que é o topo da pilha

    def top(self):
        """Retorna o elemento no topo da pilha sem removê-lo."""
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._fila[0]  # O topo da pilha é o primeiro elemento da fila

    def is_empty(self):
        """Retorna True se a pilha estiver vazia, False caso contrário."""
        return len(self._fila) == 0

    def size(self):
        """Retorna o número de elementos na pilha."""
        return len(self._fila)

# Exemplo de uso
pilha = PilhaComFila()
pilha.push(10)
pilha.push(20)
pilha.push(30)
print(pilha.top())  # 30
print(pilha.pop())  # 30
print(pilha.pop())  # 20
print(pilha.size())  # 1
 