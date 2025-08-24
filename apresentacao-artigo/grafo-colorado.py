import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -----------------------------
# 1. Dados de exemplo
# -----------------------------
disciplinas = {
    "DL": [1, 2, 3, 4, 5],
    "C": [3, 4, 6, 7],
    "OB": [2, 8, 9],
    "AC": [1, 6, 9],
    "MATH": [2, 3, 7],
    "DBMS": [4, 5, 7],
    "OS": [8, 9, 10],
    "ALG": [1, 7, 10]
}

# -----------------------------
# 2. Construção do grafo
# -----------------------------
G = nx.Graph()
for d in disciplinas.keys():
    G.add_node(d)

for d1 in disciplinas:
    for d2 in disciplinas:
        if d1 != d2 and set(disciplinas[d1]) & set(disciplinas[d2]):
            G.add_edge(d1, d2)

# -----------------------------
# 3. Ordem e preparação do algoritmo
# -----------------------------
ordem_vertices = sorted(G.nodes(), key=lambda x: G.degree[x], reverse=True)
cores = {}
paleta = plt.cm.tab10.colors  # até 10 cores distintas
etapas = []  # guarda estados parciais

for v in ordem_vertices:
    vizinhos = [cores.get(n) for n in G.neighbors(v)]
    cor = 0
    while cor in vizinhos:
        cor += 1
    cores[v] = cor
    etapas.append(dict(cores))  # salva estado parcial

# -----------------------------
# 4. Animação
# -----------------------------
pos = nx.spring_layout(G, seed=42)  # posição fixa dos nós
fig, ax = plt.subplots(figsize=(6, 6))

def update(frame):
    ax.clear()
    cores_parciais = etapas[frame]
    color_map = []
    for node in G.nodes():
        if node in cores_parciais:
            color_map.append(paleta[cores_parciais[node] % len(paleta)])
        else:
            color_map.append("lightgray")
    nx.draw(
        G, pos, ax=ax, with_labels=True,
        node_color=color_map, node_size=1200, font_size=10
    )
    ax.set_title(f"Etapa {frame+1}: coloração parcial")

ani = animation.FuncAnimation(
    fig, update, frames=len(etapas),
    interval=1500, repeat=False
)

# Para visualizar na tela:
plt.show()
# Para salvar como MP4:
ani.save("coloracao.gif", writer="imagemagick")
