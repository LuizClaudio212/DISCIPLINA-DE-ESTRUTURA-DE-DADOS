class ja_existe(Exception):
    pass

class nao_existe(Exception):
    pass

class FilaVazia(Exception):
    pass

class SetWithQueue:
    CAPACIDADE_PADRAO = 5

    def __init__(self):
        self._dados = [None] * SetWithQueue.CAPACIDADE_PADRAO
        self._tamanho = 0
        self._inicio = 0

    def contains(self, element):
        """Verifica se o elemento está na fila circular"""
        posicao = self._inicio
        for i in range(self._tamanho):
            if self._dados[posicao] == element:
                return True
            posicao = (posicao + 1) % len(self._dados)
        return False

    def size(self):
        return self._tamanho

    def is_empty(self):
        return self._tamanho == 0


    def remove(self, element):
        """Remove um elemento da fila circular sem mover os outros"""
        if self.is_empty():
            raise FilaVazia('A Fila está vazia')
        if not self.contains(element):
            raise nao_existe("Erro! O elemento não está na fila.")

        # Procura o índice do elemento na fila circular
        posicao = self._inicio
        for i in range(self._tamanho):
            if self._dados[posicao] == element:
                self._dados[posicao] = None  # Remove o elemento sem deslocar
                if posicao == self._inicio:
                    # Se for o primeiro elemento, avança o início da fila
                    self._inicio = (self._inicio + 1) % len(self._dados)
                self._tamanho -= 1
                return element
            posicao = (posicao + 1) % len(self._dados)

        raise nao_existe("Erro! O elemento não está na fila.")


    def add(self, element):
        """Adiciona um elemento na fila circular"""
        if self.contains(element):
            raise ja_existe("Erro! O elemento já está na fila.")
        if self._tamanho == len(self._dados):
            self._altera_tamanho(2 * len(self._dados))  # Redimensiona o array se necessário

        # Calcula o índice disponível para adicionar o novo elemento
        disponivel = (self._inicio + self._tamanho) % len(self._dados)
        self._dados[disponivel] = element
        self._tamanho += 1

    def _altera_tamanho(self, novo_tamanho):
        """Redimensiona a capacidade da fila circular"""
        dados_antigos = self._dados
        self._dados = [None] * novo_tamanho
        posicao = self._inicio
        for k in range(self._tamanho):
            self._dados[k] = dados_antigos[posicao]
            posicao = (1 + posicao) % len(dados_antigos)
        self._inicio = 0

    def list(self):
        """Retorna a lista dos elementos válidos na fila"""
        result = []
        posicao = self._inicio
        for i in range(self._tamanho):
            result.append(self._dados[posicao])
            posicao = (posicao + 1) % len(self._dados)
        return result

