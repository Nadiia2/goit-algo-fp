import heapq
import networkx as nx
import matplotlib.pyplot as plt
import uuid
from queue import Queue

class TreeNode:
    def __init__(self, value, color="skyblue", visited_order=0):
        self.left = None
        self.right = None
        self.value = value
        self.color = color
        self.visited_order = visited_order
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.value, visited_order=node.visited_order)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2 ** layer
            pos[node.left.id] = (left_x, y - 1)
            add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2 ** layer
            pos[node.right.id] = (right_x, y - 1)
            add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(root_node, total_visited):
    tree_graph = nx.DiGraph()
    position = {root_node.id: (0, 0)}
    tree_graph = add_edges(tree_graph, root_node, position)

    node_colors = [
        generate_color(node[1]["visited_order"], total_visited)
        for node in tree_graph.nodes(data=True)
    ]
    node_labels = {node[0]: node[1]["label"] for node in tree_graph.nodes(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw(tree_graph, pos=position, labels=node_labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def heap_to_tree(heap_list, index=0):
    if index < len(heap_list):
        node = TreeNode(heap_list[index])
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        if left_child_index < len(heap_list):
            node.left = heap_to_tree(heap_list, left_child_index)
        if right_child_index < len(heap_list):
            node.right = heap_to_tree(heap_list, right_child_index)
        return node
    return None

def generate_color(order, total_nodes):
    intensity = int((order / total_nodes) * 255)
    return f"#{intensity:02x}{intensity:02x}FF"

def depth_first_search(node, visited_nodes=None, visit_order=0):
    if visited_nodes is None:
        visited_nodes = {}
    visited_nodes[node.id] = visit_order
    node.visited_order = visit_order
    visit_order += 1
    if node.left:
        visit_order = depth_first_search(node.left, visited_nodes, visit_order)
    if node.right:
        visit_order = depth_first_search(node.right, visited_nodes, visit_order)
    return visit_order

def breadth_first_search(root_node):
    visit_order = 0
    visited_nodes = {}
    node_queue = Queue()
    node_queue.put((root_node, visit_order))
    while not node_queue.empty():
        current_node, visit_order = node_queue.get()
        if current_node.id not in visited_nodes:
            visited_nodes[current_node.id] = visit_order
            current_node.visited_order = visit_order
            visit_order += 1
            if current_node.left:
                node_queue.put((current_node.left, visit_order))
            if current_node.right:
                node_queue.put((current_node.right, visit_order))
    return max(visited_nodes.values())

def reset_visited_order(node):
    if node is not None:
        node.visited_order = 0
        reset_visited_order(node.left)
        reset_visited_order(node.right)

heap_list = [1, 3, 5, 7, 9, 2, 4]
heapq.heapify(heap_list)
heap_tree = heap_to_tree(heap_list)

reset_visited_order(heap_tree)
total_visited_dfs = depth_first_search(heap_tree)
draw_tree(heap_tree, total_visited_dfs)

reset_visited_order(heap_tree)
total_visited_bfs = breadth_first_search(heap_tree)
draw_tree(heap_tree, total_visited_bfs)
