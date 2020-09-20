from globals_graph import *
from EdgeNode_graph import *
import bfs_graph


def algorithm():
    start_node = Node(let_to_num[start], 0)
    open.append(start_node)
    pathes[let_to_num[start]] = start
    while len(open) > 0:
        current_node = open[0]
        current_index = 0
        for index, node in enumerate(open):
            if node.g < current_node.g:
                current_node = node
                current_index = index
        open.pop(current_index)
        closed.append(current_node)

        if current_node.id == let_to_num[finish]:  # если нужная вершина найдена, ищем её путь
            open_id = []
            closed_id = []
            for i in open:
                open_id.append(i.id)
            for i in closed:
                closed_id.append(i.id)
            return open_id, closed_id

        children = []
        for neighbour in routes_dict[current_node.id]:
            #if neighbour not in open and neighbour not in closed:
            if pathes[neighbour] == -1 or current_node.id == 0:
                a = 1 + current_node.g
                new_node = Node(neighbour, a)
                children.append(new_node)  # ???
                #pathes[new_node.id] = pathes[current_node.id] + num_to_let[new_node.id]
                pathes[neighbour] = pathes[current_node.id] + num_to_let[neighbour]
                #open.append(new_node)  # добавляем в опен ?????
                #open.pop(current_node)
        for child in children:
            for closed_child in closed:
                if child == closed_child:
                    continue
            child.g = current_node.g + 1 # ????
            open.append(child)  # добавляем в опен ?????


def main():
    bfs_graph.make_routes()
    for i in range(len(routes_dict)):
        pathes.append(-1)
    open_id, closed_id = algorithm()
    return open_id, closed_id