from globals_grid import *
from node_grid import Node


def algorithm():
    # создание объектов класса Node
    start_node = Node(None, start)  # Первый аргумент - родитель, второй  - координаты
    start_node.g = start_node.h = start_node.f = 0
    finish_node = Node(None, finish)
    finish_node.g = finish_node.h = finish_node.f = 0

    open.append(start_node)
    while len(open) > 0:
        current_node = open[0]
        current_index = 0
        for index, node in enumerate(open):
            if node.f < current_node.f:
                current_node = node
                current_index = index
        open.pop(current_index)
        closed.append(current_node)

        if current_node == finish_node:  # если нужная вершина найдена, ищем её путь
            path = []
            while current_node is not None:
                path.append(current_node.coordinate)
                current_node = current_node.parent
            path = path[::-1]  # переворачиваем путь
            open_id = []  # номера Node из списка опен
            closed_id = []
            for i in open:
                open_id.append(i.coordinate)
            for i in closed:
                closed_id.append(i.coordinate)
            return path, open_id, closed_id

        children = []
        if connect == 4:  # 4-связный грид
            shifts = shift4
        elif connect == 8:  # 8-связный грид
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
            new_node = Node(current_node, node_position)  # если всё норм, то перемещаемся туда
            children.append(new_node)

        for child in children:
            for closed_child in closed:
                if child == closed_child:
                    continue
            child.g = current_node.g + 1
            child.h = abs(child.coordinate[0] - finish_node.coordinate[0]) + abs(child.coordinate[1] - finish_node.coordinate[1])
            child.f = child.g + child.h
            open.append(child)  # добавляем в опен

