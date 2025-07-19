def bellman_ford(n, edges):
    dist = [0] * n  # Pode começar com 0 pois queremos detectar ciclos, não distâncias reais
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Verifica se ainda é possível relaxar (ou seja, existe ciclo negativo)
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return True  # ciclo negativo encontrado
    return False

def solve_cases(cases):
    results = []
    for n, m, wormholes in cases:
        if bellman_ford(n, wormholes):
            results.append("possible")
        else:
            results.append("not possible")
    return results

def load_text_content(data_file_dir_path: str):
    try:
        with open(data_file_dir_path, 'r') as file:
            return file.read()
    except Exception as e:
        raise e

def main():
    # Leitura de entrada (exemplo com os dados fornecidos)
    input_text = load_text_content(data_file_dir_path="trabalho-2/questoes/data/questao_3/input.txt")
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

    # Processa e imprime
    results = solve_cases(cases)
    for res in results:
        print(res)


if __name__=="__main__":
    main()