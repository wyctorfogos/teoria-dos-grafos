##  Wyctor Fogos da Rocha ##
from collections import defaultdict
import sys

def load_text_content():
    ## Carregamento dos dados via stdin
    return sys.stdin.read()

def verifyCondition(n, m):
    ''''
        Verificar a conexidade do grafo, pois o problema pode ser representado como um grafo completamente conexo
    '''
    if ((n<0) or (n>100)):
        print("O 'n' está além dos limites!\n")
        return False
    # Verificação 
    if ((m<0) and (m>((n*(n-1))/2))):
        print("O 'm' está além dos limites!\n")
        return False
    return True

def preprocessing_data(data_context: str):
    try:
        lines = data_context.strip().split("\n")
        n, m = map(int, lines[0].split())
        edges = [tuple(map(int, line.split())) for line in lines[1:]]

        #  Verificar as condições a serem feitas
        result = verifyCondition(n, m )
        if result:
            return n, m, edges
        
    except Exception as e:
        raise ValueError(f"Erro ao processar dados: {e}")

def students_and_shoelaces(n, m, edges):
    adj = defaultdict(set)
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)

    rounds = 0
    while True:
        to_remove = [node for node in adj if len(adj[node]) == 1]
        if not to_remove:
            break
        for node in to_remove:
            for neighbor in adj[node]:
                adj[neighbor].discard(node)
            del adj[node]
        rounds += 1
    return rounds

if __name__ == "__main__":       
    raw_data = load_text_content()
    # Preprocessamento
    n, m, edges = preprocessing_data(raw_data)
    
    result = students_and_shoelaces(n, m, edges)

    sys.stdout.write(str(result) + '\n')