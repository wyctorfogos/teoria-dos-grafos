##  Wyctor Fogos da Rocha ##
import sys

def bellmanford(n, edges):
    """
        Código do BellmanFord
    """
    try:    
        # Tentar detectar ciclos inicialmente
        dist = [0] * n  
        for _ in range(n - 1):
            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Verifica se ainda é possível relaxar (ou seja, existe ciclo negativo)
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                return True  # ciclo negativo encontrado
        return False
    except Exception as e:
        raise ValueError(f"Erro: {e}\n")
    
def solve_cases(cases):
    results = []
    for n, m, wormholes in cases:
        if bellmanford(n, wormholes):
            results.append("possible")
        else:
            results.append("not possible")
    return results

def load_text_content():
    ## Carregamento dos dados via stdin
    return sys.stdin.read()

def main():
    ## Pipeline do processamento dos dados
    input_text = load_text_content()
    lines = input_text.strip().split('\n')

    index = 0
    c = int(lines[index])
    index += 1
    cases = []

    for _ in range(c):
        n, m = map(int, lines[index].split())
        index += 1
        wormholes = []
        for _ in range(m):
            x, y, t = map(int, lines[index].split())
            wormholes.append((x, y, t))
            index += 1
        cases.append((n, m, wormholes))

    ## Processa e imprime
    # Processamento dos dados
    results = solve_cases(cases)
    for result in results:
        sys.stdout.write(str(result) + '\n')

if __name__=="__main__":
    ## Leitura dos dados de entrada
    main()