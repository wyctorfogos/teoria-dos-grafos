##  Wyctor Fogos da Rocha ##
import sys

def bellmanford(n, arestas):
    """
        Código do BellmanFord
    """
    try:    
        # Tentar detectar ciclos inicialmente
        dist = [0] * n  
        for _ in range(n - 1):
            for u, v, w in arestas:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Verficar se tem algum ciclo negativo
        for u, v, w in arestas:
            # Ciclo negativo encontrado
            if dist[u] + w < dist[v]:
                return True
        return False
    except Exception as e:
        raise ValueError(f"Erro: {e}\n")
    
def resolucao(casos):
    results = []
    for n, m, wormholes in casos:
        if bellmanford(n=n, arestas=wormholes):
            results.append("possible")
        else:
            results.append("not possible")
    return results

def load_text_content():
    ## Carregamento dos dados via stdin
    return sys.stdin.read()


def valida_nm(n, m):
    """
        Verifica os limites de 'n' e 'm'
    """
    if not (1 <= n <= 1000):
        raise ValueError(f"Valor inválido de n: {n} (esperado entre 1 e 1000)")
    if not (0 <= m <= 2000):
        raise ValueError(f"Valor inválido de m: {m} (esperado entre 0 e 2000)")

def valida_arestas(x, y, t, n):
    """
        Verificar as limitações de 'x' e 'y'
    """
    if not (0 <= x < n):
        raise ValueError(f"Valor inválido de x: {x} (esperado entre 0 e {n-1})")
    if not (0 <= y < n):
        raise ValueError(f"Valor inválido de y: {y} (esperado entre 0 e {n-1})")
    if not (-1000 <= t <= 1000):
        raise ValueError(f"Valor inválido de t: {t} (esperado entre -1000 e 1000)")
    return True


def main():
    ## Pipeline do processamento dos dados
    input_text = load_text_content()
    lines = input_text.strip().split('\n')

    index = 0
    # Nº de casos
    c = int(lines[index])
    index += 1
    casos = []
        
    for _ in range(c):
        n, m = map(int, lines[index].split())
        valida_nm(n=n, m=m)
        index += 1
        wormholes = []
        for _ in range(m):
            x, y, t = map(int, lines[index].split())
            valida_arestas(x, y, t, n)
            
            wormholes.append((x, y, t))
            index += 1
        casos.append((n, m, wormholes))

    ## Processa e imprime
    results = resolucao(casos=casos)
    for result in results:
        sys.stdout.write(str(result) + '\n')

if __name__=="__main__":
    ## Leitura dos dados de entrada
    main()