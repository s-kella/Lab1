from node_grid import Node
from globals_grid import *


def algorithm():
    start_node = Node(None, start)  # Первый аргумент - родитель, второй  - координаты
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, finish)
    end_node.g = end_node.h = end_node.f = 0

    start_node.cost = 0
    open.append(start_node) # добавляем начальную вершину в очередь
    while open:  # пока open не пустой
        closed.append(open[0])
        current_node = open.pop(0)  # достаём вершину
        if connect == 4:
            shifts = shift4
        elif connect == 8:
            shifts = shift8
        for shift in shifts:
            node_position = (current_node.coordinate[0] + shift[0], current_node.coordinate[1] + shift[1])
            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(grid[len(grid) - 1]) - 1) or node_position[1] < 0:  # смотрим, чтобы не выйти за границу грида
                continue
            if grid[node_position[0]][node_position[1]] == 1:  # если там стена
                continue
            if connect == 8 and shift[0] != 0 and shift[1] != 0:  # чтобы не срезать углы (если, например, справа стена, то нельзя пойти вправо-вверх)
                if grid[current_node.coordinate[0]][current_node.coordinate[1] + shift[1]] == 1 or grid[current_node.coordinate[0] + shift[0]][current_node.coordinate[1]] == 1:
                    continue
            new_node = Node(current_node, node_position)
            if new_node not in open and new_node not in closed:
                open.append(new_node)  # добавление вершины в очередь
                new_node.cost += 1
        if current_node == end_node:  # если нужная вершина найдена, ищем её путь
            path = []
            current = current_node
            while current is not None:
                path.append(current.coordinate)
                current = current.parent
            path = path[::-1]  # переворачиваем путь
            for i in open:
                open_id.append(i.coordinate)  # номера Node из списка опен
            for i in closed:
                closed_id.append(i.coordinate)
            return path

