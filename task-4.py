import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4()) 

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} 

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

class BinaryHeap:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
    
        queue = [node]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = Node(key)
                self._heapify_up(current.left)
                return
            elif not current.right:
                current.right = Node(key)
                self._heapify_up(current.right)
                return
            else:
                queue.append(current.left)
                queue.append(current.right)

    def _heapify_up(self, node):
        parent = self._find_parent(self.root, node)
        while parent and node.val > parent.val:
            node.val, parent.val = parent.val, node.val
            node = parent
            parent = self._find_parent(self.root, node)

    def _find_parent(self, root, child):
        if root is None:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left == child or node.right == child:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None

heap = BinaryHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(15)
heap.insert(30)
heap.insert(25)

draw_tree(heap.root)
