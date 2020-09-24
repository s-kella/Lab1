from globals_graph import *
import EdgeNode_graph


def make_routes():
    for i in range(len(root[2])):
        if 'id' in root[2][i].attrib:
            EdgeNode_graph.addNode(i, root)
            let_to_num[nodes[i].id] = i
            num_to_let[i] = nodes[i].id
        else:
            EdgeNode_graph.addEdge(i, root)
    for edge in edges:
        if let_to_num[edge.source] not in routes_dict:
            routes_dict[let_to_num[edge.source]] = []
        routes_dict[let_to_num[edge.source]].append(let_to_num[edge.target])
    return routes_dict


def algorithm(start, cost):
    cost[start] = 0  # стоимость начальной вершины
    open.append(start)  # добавляем начальную вершину в очередь
    #while open:  # пока там что-то есть
    while let_to_num[finish] not in open:
        if let_to_num[finish] in open:
            return
        closed.append(open[0])
        node = open.pop(0)  # извлекаем вершину
        for neighbour in routes_dict[node]:
            if neighbour not in open and neighbour not in closed:
                open.append(neighbour)  # добавление вершины в очередь
                cost[neighbour] = cost[node] + 1  # подсчитываем уровень вершины
                pathes[neighbour] = pathes[node] + num_to_let[neighbour]


def main(start_num):
    cost = [-1] * len(routes_dict)  # список стоимоcти дороги до вершин
    pathes[let_to_num[start]] = start
    algorithm(start_num, cost)
    return cost[let_to_num[finish]]