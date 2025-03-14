import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict


MAX_INT = float('inf')

def minDistance(dist, visited):
    (minimum, minVertex) = (MAX_INT, 0)
    for vertex in range(len(dist)):
        if minimum > dist[vertex] and not visited[vertex]:
            (minimum, minVertex) = (dist[vertex], vertex)
    return minVertex

def Dijkstra(graph, modifiedGraph, src):
    num_vertices = len(graph)
    sptSet = defaultdict(lambda: False)
    dist = [MAX_INT] * num_vertices
    dist[src] = 0

    for count in range(num_vertices):
        curVertex = minDistance(dist, sptSet)
        sptSet[curVertex] = True

        for vertex in range(num_vertices):
            if (not sptSet[vertex] and
                    dist[vertex] > dist[curVertex] + modifiedGraph[curVertex][vertex] and
                    graph[curVertex][vertex] != 0):
                dist[vertex] = dist[curVertex] + modifiedGraph[curVertex][vertex]

    return dist

def BellmanFord(edges, graph, num_vertices):
    dist = [MAX_INT] * (num_vertices + 1)
    dist[num_vertices] = 0

    for i in range(num_vertices):
        edges.append([num_vertices, i, 0])

    for i in range(num_vertices):
        for (src, des, weight) in edges:
            if dist[src] != MAX_INT and dist[src] + weight < dist[des]:
                dist[des] = dist[src] + weight

    return dist[0:num_vertices]

def JohnsonAlgorithm(graph):
    edges = []

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                edges.append([i, j, graph[i][j]])

    modifyWeights = BellmanFord(edges, graph, len(graph))

    modifiedGraph = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                modifiedGraph[i][j] = graph[i][j] + modifyWeights[i] - modifyWeights[j]

    output = "Modified Graph:\n" + str(modifiedGraph) + "\n\n"

    for src in range(len(graph)):
        output += "Shortest Distance with vertex " + str(src) + " as the source:\n"
        distances = Dijkstra(graph, modifiedGraph, src)
        output += str(distances) + "\n\n"
        draw_result_graph(distances, "Shortest Distance with vertex " + str(src) + " as the source")

    return modifiedGraph, output

def draw_graph(graph, title):
    G = nx.DiGraph()

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])

    pos = nx.spring_layout(G, k=10000)
    labels = nx.get_edge_attributes(G, 'weight')
    weights = [graph[u][v] for u, v, _ in G.edges(data=True)]
    nx.draw_networkx(G, pos, with_labels=True, node_size=300, node_color='lightblue')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    nx.draw_networkx_edges(G, pos, width=1, alpha=.5, edge_color='black')
    plt.title(title)
    plt.show()

def draw_result_graph(distances, title):
    num_vertices = len(distances)
    G = nx.DiGraph()

    for vertex, distance in enumerate(distances):
        G.add_node(vertex, label=str(distance))

    for i in range(num_vertices):
        for j in range(num_vertices):
            if distances[i] == 0 and distances[j] == 0:
                G.add_edge(i, j, weight=0)

    pos = nx.spring_layout(G, k=10)
    labels = nx.get_node_attributes(G, 'label')

    nx.draw_networkx(G, pos, with_labels=True, node_size=300, node_color='lightblue')
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, width=1, alpha=.5, edge_color='black')
    plt.title(title)
    plt.show()

def display_result(result):
    result_window = tk.Toplevel(window)
    result_window.title("Johnson Algorithm Result")
    result_window.geometry("400x400")

    lbl_result = tk.Label(result_window, text=result, justify='left')
    lbl_result.pack(pady=10)

def run_algorithm():
    input_graph = txt_input.get("1.0", "end").strip()
    rows = input_graph.split("\n")
    graph = []
    for row in rows:
        graph.append(list(map(int, row.split())))

    draw_graph(graph, "Input Graph")

    modified_graph, result = JohnsonAlgorithm(graph)
    messagebox.showinfo("Johnson Algorithm", result)
    draw_graph(modified_graph, "Modified Graph")
#GUI tkinter 
window = tk.Tk()
window.title("Johnson Algorithm")
window.geometry("480x480")
window.resizable(True, True)
window.configure(background="#C1CDCD")

lbl_input = tk.Label(
    window,
    text="Enter the graph (space-separated values, one row per line) \nfor example:\n0 -5 2 3\n0 0 4 0\n0 0 0 1\n0 0 0 0",
    font=("times", 12, "bold")
)
lbl_input.pack(pady=10)

txt_input = tk.Text(window, height=10, width=30)
txt_input.pack()

lbl_txt = tk.Label(
    window,
    text="After viewing input graph \n close the page to view result graphs and modified graph and algorithm",
    font=("times", 12, "bold")
)
lbl_txt.pack(pady=5)

btn_run = tk.Button(
    window,
    text="Show graph input and algorithm result",
    command=run_algorithm,
    background="#53868B",
    fg="#F8EDE3",
    font=("times", 12, "bold")
)
btn_run.pack(pady=30)

window.mainloop()
