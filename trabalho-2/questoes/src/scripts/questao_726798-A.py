##  Wyctor Fogos da Rocha ##
from collections import defaultdict
import sys

def load_text_content():
    # Função para carregar os dados da entrada padrão (stdin)
    return sys.stdin.read()

def verifyCondition(n, m):
    """
        Verifica se os valores de entrada para as condições do problema
    """
    if not (0 <= n <= 1000):
        raise ValueError("O 'n' está além dos limites permitidos!")

    if not (0 <= m <= (n * (n - 1)) // 2):
        raise ValueError("O 'm' está além dos limites permitidos!")

    return True

def preprocessing_data(data_context: str):
    """
       Extrai n e m, pego a lista de arestar e valida
    """
    try:
        lines = data_context.strip().split("\n")
        n, m = map(int, lines[0].split())

        # Criação das arestas a partir das linhas seguintes
        arestas = [tuple(map(int, line.split())) for line in lines[1:]]

        # Valida os valores de n e m
        verifyCondition(n, m)

        # Verifica se os nós estão no intervalo válido [1, n]
        for a, b in arestas:
            if not (1 <= a <= n and 1 <= b <= n):
                raise ValueError(f"Aresta inválida: {a}, {b}")

        return n, m, arestas

    except Exception as e:
        raise ValueError(f"Erro ao processar dados: {e}")

def students_and_shoelaces(n, m, arestas):
    """
        Calcular o número de rodadas (grupos expulsos).
    """
        
    adj = defaultdict(set)  # Lista de adjacência

    # Construção do grafo
    for a, b in arestas:
        adj[a].add(b)
        adj[b].add(a)
    
    # Contador de rodadas
    rounds = 0  

    while True:
        # Identifica estudantes com grau 1
        vertice_to_remove = []
        for vertice in adj:
            # Verifica se os vizinhos de 'vertice' tem tamanho igual a 1
            if len(adj[vertice]) == 1: 
                vertice_to_remove.append(vertice) # Vou remover

        if not vertice_to_remove:
            break

        # Remove os estudantes e atualiza as conexões dos vizinhos
        for vertice in vertice_to_remove:
            for vizinho in adj[vertice]:
                adj[vizinho].discard(vertice)  # Remove a conexão inversa
            del adj[vertice]  # Remove o estudante do grafo
        
        # Conta uma rodada
        rounds += 1 

    return rounds

if __name__ == "__main__":
    # Leitura dos dados de entrada
    data = load_text_content()

    # Pré-processamento e validações
    n, m, arestas = preprocessing_data(data)

    # Execução da lógica principal
    result = students_and_shoelaces(n, m, arestas)

    # Impressão da saída
    sys.stdout.write(str(result) + '\n')
