from queue import Queue, LifoQueue, PriorityQueue


class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """

    def __init__(self, estado: str, pai: object, acao: str, custo: int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo


def sucessor(estado: str) -> list:
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """

    def move_vazio(estado_atual: str, pos_vazio: int, nova_pos: int) -> str:
        """
        Recebe o estado atual (string), a posição do caractere vazio (int) e a nova posição do caractere vazio (int), retornando o novo estado possível de ser atingível (string)
        """
        lista_estado = list(estado_atual)
        lista_estado[pos_vazio], lista_estado[nova_pos] = (
            lista_estado[nova_pos],
            lista_estado[pos_vazio],
        )
        return "".join(lista_estado)

    ACOES = ["acima", "direita", "abaixo", "esquerda"]
    VAZIO = "_"

    TOP_ROW = [0, 1, 2]
    RIGHT_COLUMN = [2, 5, 8]
    BOTTOM_ROW = [6, 7, 8]
    LEFT_COLUMN = [0, 3, 6]

    posicao_vazio = estado.find(VAZIO)
    lista_sucessores = []

    # Se VAZIO não está na linha de cima
    if posicao_vazio not in TOP_ROW:
        # pode mover pra cima
        lista_sucessores.append((ACOES[0], move_vazio(estado, posicao_vazio, posicao_vazio - 3)))

    # Se não está na coluna da direita
    if posicao_vazio not in RIGHT_COLUMN:
        # pode mover pra direita
        lista_sucessores.append((ACOES[1], move_vazio(estado, posicao_vazio, posicao_vazio + 1)))

    # Se não está na linha de baixo
    if posicao_vazio not in BOTTOM_ROW:
        # pode mover pra baixo
        lista_sucessores.append((ACOES[2], move_vazio(estado, posicao_vazio, posicao_vazio + 3)))

    # Se não está na coluna da esquerda
    if posicao_vazio not in LEFT_COLUMN:
        # pode mover pra esquerda
        lista_sucessores.append((ACOES[3], move_vazio(estado, posicao_vazio, posicao_vazio - 1)))

    return lista_sucessores


def expande(nodo: Nodo) -> list:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    conjunto_nodos = set()
    lista_sucessores = sucessor(nodo.estado)

    for element in lista_sucessores:
        conjunto_nodos.add(Nodo(element[1], nodo, element[0], nodo.custo + 1))

    return conjunto_nodos


def find_path(cur_node: Nodo) -> list:
    caminho = list()
    while cur_node.pai != None:
        caminho.insert(0, cur_node.acao)
        cur_node = cur_node.pai
    return caminho


def bfs(estado: str):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """

    # Se o estado inicial não for válido, ou se o estado inicial não houver solução:
    if (not check_initial_state(estado)) or (not check_solvable(estado)):
        return None

    # Se já for o estado final, não tem o que fazer
    if check_final_state(estado):
        return list()

    nodo_inicial = Nodo(estado, None, None, 0)
    explorados = set()
    fronteira = Queue()
    fronteira.put(nodo_inicial)

    while fronteira:
        node_temp = fronteira.get()
        if check_final_state(node_temp.estado):
            return find_path(node_temp)
        if node_temp.estado not in explorados:
            explorados.add(node_temp.estado)
            candidatos = expande(node_temp)
            for node in candidatos:
                fronteira.put(node)
    return None


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # Se o estado inicial não for válido, ou se o estado inicial não houver solução:
    if (not check_initial_state(estado)) or (not check_solvable(estado)):
        return None

    if check_final_state(estado):
        return list()

    nodo_inicial = Nodo(estado, None, None, 0)
    explorados = set()
    fronteira = LifoQueue()
    fronteira.put(nodo_inicial)

    while fronteira:
        node_temp = fronteira.get()
        if check_final_state(node_temp.estado):
            return find_path(node_temp)
        if node_temp.estado not in explorados:
            explorados.add(node_temp.estado)
            candidatos = expande(node_temp)
            for node in candidatos:
                fronteira.put(node)
    return None


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def check_initial_state(estado: str) -> bool:
    valid_chars = "12345678_"
    if (len(estado) == len(valid_chars)) and (all(char in estado for char in valid_chars)):
        return True
    else:
        return False


def check_final_state(estado: str) -> bool:
    if estado == "12345678_":
        return True
    else:
        return False


def check_solvable(estado: str) -> bool:
    VAZIO = "_"
    lista_estados = list(estado)
    count_inversoes = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if lista_estados[j] != VAZIO and lista_estados[i] != VAZIO and lista_estados[i] > lista_estados[j]:
                count_inversoes += 1
    if count_inversoes % 2 == 0:
        return True
    else:
        return False
