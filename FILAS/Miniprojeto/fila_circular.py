class ja_existe(Exception):
    """Exceção levantada quando um elemento já existe na fila."""
    pass

class nao_existe(Exception):
    """Exceção levantada quando um elemento não existe na fila."""
    pass

class FilaVazia(Exception):
    """Exceção levantada quando se tenta operar em uma fila vazia."""
    pass

class SetWithQueue:
    """Implementa uma fila circular com funcionalidades de conjunto."""

    CAPACIDADE_PADRAO = 5  # Capacidade inicial padrão da fila

    def __init__(self):
        """Inicializa a fila circular com capacidade padrão."""
        self._dados = [None] * SetWithQueue.CAPACIDADE_PADRAO  # Armazena os dados
        self._tamanho = 0  # Número de elementos na fila
        self._inicio = 0  # Índice do início da fila

    def contains(self, element):
        """Verifica se o elemento está na fila circular."""
        posicao = self._inicio
        for i in range(self._tamanho):
            if self._dados[posicao] == element:
                return True
            posicao = (posicao + 1) % len(self._dados)  # Avança na fila circular
        return False

    def size(self):
        """Retorna o número de elementos na fila."""
        return self._tamanho

    def is_empty(self):
        """Verifica se a fila está vazia."""
        return self._tamanho == 0

    def remove(self, element):
        
        """
        Remove um elemento da fila circular sem mover os outros.

        Parâmetros:
            element: O elemento a ser removido da fila.

            Retorna:
            O elemento removido, se encontrado.

            Excepts:
            FilaVazia: Se a fila estiver vazia.
            nao_existe: Se o elemento não estiver na fila.
        """
        #validações
        if self.is_empty():
            raise FilaVazia('A Fila está vazia')
        if not self.contains(element):
            raise nao_existe("Erro! O elemento não está na fila.")

        # Inicia a busca pelo elemento a ser removido
        posicao = self._inicio
        for i in range(self._tamanho):
            if self._dados[posicao] == element:
                self._dados[posicao] = None  # Marca o elemento como removido
                self._tamanho -= 1  # Reduz o tamanho da fila
                
                # Ajusta o índice de início se o elemento removido for o primeiro
                if posicao == self._inicio:
                    while self._dados[self._inicio] is None and self._tamanho > 0:
                        # Avança o índice de início até encontrar um elemento válido
                        self._inicio = (self._inicio + 1) % len(self._dados)
                        
                return element  # Retorna o elemento removido
            
            # Avança para a próxima posição na fila circular
            posicao = (posicao + 1) % len(self._dados)

        raise nao_existe("Erro! O elemento não está na fila.")  # Se o elemento não foi encontrado, levanta uma exceção


    def add(self, element):
        """Adiciona um elemento na fila circular."""
        if self.contains(element):
            raise ja_existe("Erro! O elemento já está na fila.")
        if self._tamanho == len(self._dados):
            self._altera_tamanho(2 * len(self._dados))  # Redimensiona a fila se cheia

        # Calcula o índice disponível para adicionar o novo elemento
        disponivel = (self._inicio + self._tamanho) % len(self._dados)
        self._dados[disponivel] = element  # Adiciona o elemento
        self._tamanho += 1  # Aumenta o tamanho da fila

    def _altera_tamanho(self, novo_tamanho):
        """Redimensiona a capacidade da fila circular."""
        dados_antigos = self._dados
        self._dados = [None] * novo_tamanho  # Cria novo array maior
        posicao = self._inicio
        for k in range(self._tamanho):
            self._dados[k] = dados_antigos[posicao]  # Copia elementos para o novo array
            posicao = (1 + posicao) % len(dados_antigos)
        self._inicio = 0  # Reinicia o início para o novo array

    def list(self):
        """Retorna a lista dos elementos válidos na fila."""
        result = []
        posicao = self._inicio
        for i in range(len(self._dados)):
            if self._dados[posicao] is not None:  # Adiciona apenas elementos não None
                result.append(self._dados[posicao])
            posicao = (posicao + 1) % len(self._dados)
        return result

