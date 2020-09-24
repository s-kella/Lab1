from globals_graph import nodes, edges
# классы Node, Edge и функции для добавления их в список всех вершин и маршрутов


class Edge:
    source = ''
    target = ''
    weight = 0

    def __init__(self):
        Edge.source = ''
        Edge.target = ''
        Edge.weight = 0


class Node:
    id = ''
    g = 0
    parent = 0

    def __init__(self, id = 0, g = 0, parent = 0):
        self.id = id

        # для А*
        self.g = g
        self.parent = parent


def addEdge(n, root):
    new_edge = Edge()
    new_edge.source = root[2][n].attrib['source']
    new_edge.target = root[2][n].attrib['target']
    new_edge.weight = root[2][n].attrib['weight']
    edges.append(new_edge)


def addNode(n, root):
    new_node = Node()
    new_node.id = root[2][n].attrib['id']
    nodes.append(new_node)