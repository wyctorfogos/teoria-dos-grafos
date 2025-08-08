##  Wyctor Fogos da Rocha ##
from collections import deque
import sys

def is_bicolorable(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n  # -1 = não colorido
    queue = deque()

    # Como o grafo é conectado, podemos começar do nó 0
    queue.append(0)
    color[0] = 0

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                return False  # Vértices adjacentes com a mesma cor

    return True

def main():
    input_lines = sys.stdin.read().splitlines()
    i = 0
    while i < len(input_lines):
        n = int(input_lines[i])
        i += 1
        if n == 0:
            break
        l = int(input_lines[i])
        i += 1
        edges = []
        for _ in range(l):
            u, v = map(int, input_lines[i].split())
            edges.append((u, v))
            i += 1
        if is_bicolorable(n, edges):
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")

if __name__ == "__main__":
    main()
