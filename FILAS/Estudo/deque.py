class FilaVazia(Exception):
    """Exceção levantada quando o deque está vazio."""
    pass

class Deck:
    """
    Implementação de um deque usando uma fila circular com redimensionamento dinâmico.
    O deque permite adição e remoção de elementos em ambas as extremidades.
    """

    CAPACIDADE_PADRAO = 5

    def __init__(self):
        """Inicializa o deque com uma capacidade padrão."""
        self._dados = [None] * Deck.CAPACIDADE_PADRAO
        self._tamanho = 0
        self._inicio = 0

    def __len__(self):
        """Retorna o número de elementos no deque."""
        return self._tamanho  # O(1)

    def is_empty(self):
        """Verifica se o deque está vazio."""
        return self._tamanho == 0

    def first(self):
        """Retorna o primeiro elemento do deque, sem removê-lo."""
        if self.is_empty():
            raise FilaVazia('O deque está vazio')
        return self._dados[self._inicio]

    def last(self):
        """
        Retorna o último elemento do deque, sem removê-lo.
        Calcula a posição do último elemento com base no início e no tamanho.
        """
        if self.is_empty():
            raise FilaVazia('O deque está vazio')
        ultimo = (self._inicio + self._tamanho - 1) % len(self._dados)
        return self._dados[ultimo]

    def add_first(self, e):
        """
        Adiciona um elemento na frente (início) do deque.
        O índice `_inicio` é movido para trás, utilizando a propriedade circular da fila.
        """
        if self._tamanho == len(self._dados):
            self._altera_tamanho(2 * len(self._dados))
        self._inicio = (self._inicio - 1) % len(self._dados)  # Movimenta o início para trás
        self._dados[self._inicio] = e
        self._tamanho += 1

    def add_last(self, e):
        """
        Adiciona um elemento no final do deque.
        Utiliza a lógica existente de cálculo da posição disponível no final.
        """
        if self._tamanho == len(self._dados):
            self._altera_tamanho(2 * len(self._dados))
        disponivel = (self._inicio + self._tamanho) % len(self._dados)
        self._dados[disponivel] = e
        self._tamanho += 1

    def remove_first(self):
        """
        Remove e retorna o primeiro elemento do deque.
        O índice `_inicio` é movido para frente, mantendo a circularidade.
        """
        if self.is_empty():
            raise FilaVazia('O deque está vazio')
        result = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) % len(self._dados)
        self._tamanho -= 1
        return result

    def remove_last(self):
        """
        Remove e retorna o último elemento do deque.
        Calcula a posição do último elemento com base no início e no tamanho atual.
        """
        if self.is_empty():
            raise FilaVazia('O deque está vazio')
        ultimo = (self._inicio + self._tamanho - 1) % len(self._dados)
        result = self._dados[ultimo]
        self._dados[ultimo] = None
        self._tamanho -= 1
        return result

    def _altera_tamanho(self, novo_tamanho):
        """
        Redimensiona o deque quando a capacidade máxima é atingida.
        Os elementos são realinhados no novo array, começando do índice zero.
        """
        dados_antigos = self._dados
        self._dados = [None] * novo_tamanho
        posicao = self._inicio
        for k in range(self._tamanho):
            self._dados[k] = dados_antigos[posicao]
            posicao = (1 + posicao) % len(dados_antigos)
        self._inicio = 0  # Realinha o início

    def show(self):
        """Método para mostrar o deque em formato de string."""
        print(self)

    def __str__(self):
        """Retorna a representação em string do deque."""
        posicao = self._inicio
        result = "["
        for k in range(self._tamanho):
            result += str(self._dados[posicao]) + ", "
            posicao = (1 + posicao) % len(self._dados)
        result += f'] tamanho: {len(self)} capacidade {len(self._dados)}\n'
        return result


# Testando o deque
deque = Deck()

# Adicionando elementos nas duas extremidades
deque.add_first(10)
deque.add_last(20)
deque.add_first(5)
deque.add_last(25)

# Mostrando o deque atual
print(deque)  # Esperado: [5, 10, 20, 25]

# Removendo das duas extremidades
deque.remove_first()  # Remove 5
deque.remove_last()   # Remove 25

# Mostrando o deque após remoções
print(deque)  # Esperado: [10, 20]