import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def to_networkx_graph(self):
        G = nx.Graph()
        for u, v, weight in self.edges:
            G.add_edge(u, v, weight=weight)
        return G

    def to_vertices_dict(self):
        vertices = {}
        for u, v, weight in self.edges:
            if u not in vertices:
                vertices[u] = []
            if v not in vertices:
                vertices[v] = []
            vertices[u].append((v, weight))
            vertices[v].append((u, weight)) 
        return vertices

def dijkstra(graph, start):
    vertices = graph.to_vertices_dict()

    distances = {vertex: float('infinity') for vertex in vertices}
    previous_vertices = {vertex: None for vertex in vertices}
    distances[start] = 0
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in vertices[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_vertices

def shortest_path(previous_vertices, start, target):
    path = []
    current_vertex = target
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path = path[::-1]
    if path[0] == start:
        return path
    else:
        return []

graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

G = graph.to_networkx_graph()
start_vertex = 'A'
distances, previous_vertices = dijkstra(graph, start_vertex)
print("Shortest distances from vertex {}:".format(start_vertex))
for vertex in distances:
    print("Distance to {}: {}".format(vertex, distances[vertex]))

pos = nx.spring_layout(G)
plt.figure()
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

for target_vertex in distances:
    if target_vertex != start_vertex:
        path = shortest_path(previous_vertices, start_vertex, target_vertex)
        if path:
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

plt.title(f"Shortest paths from {start_vertex}")
plt.show()
