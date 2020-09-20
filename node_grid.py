class Node():
    def __init__(self, parent=None, coordinate=None):
        self.parent = parent  # родительская вершина, для вывода пути
        self.coordinate = coordinate

        # для А*
        self.g = 0
        self.h = 0
        self.f = 0

        # для bfs
        self.cost = -1

    def __eq__(self, second):  # для сравнения вершин (текущая = искомой)
        return self.coordinate == second.coordinate
