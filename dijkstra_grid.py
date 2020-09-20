from globals_graph import *
import EdgeNode_graph
from globals_grid import matrix_numbers, start_j, start_i

def algorithm(start, finish, matrix):
    count_node = len(matrix)
    cost = [1000000] * count_node
    cost[start] = 0
    pathes[start] = str(matrix_numbers[start_i][start_j])
    while finish not in closed:
        for i in range(count_node):
            min_cost = 1000001
            index_min_cost = -1
            for node_id in range(count_node):
                if node_id not in closed and cost[node_id] < min_cost:
                    if node_id not in open:
                        open.append(node_id)
                    min_cost = cost[node_id]
                    index_min_cost = node_id
            for node_id in range(count_node):
                if cost[index_min_cost] + matrix[index_min_cost][node_id] < cost[node_id]:
                    cost[node_id] = cost[index_min_cost] + matrix[index_min_cost][node_id]
                    pathes[node_id] = str(pathes[index_min_cost]) + str(node_id)
            open.remove(index_min_cost)
            closed.append(index_min_cost)
            if finish in closed:
                return cost[finish]
    return cost[finish]


def make_routes():  # функция для считывания маршрутов из xml
    node_is_end = False
    for i in range(len(root[2])):
        if 'id' in root[2][i].attrib:  # считывание вершин
            EdgeNode_graph.addNode(i, root)
            let_to_num[nodes[i].id] = i
            num_to_let[i] = nodes[i].id
        else:
            EdgeNode_graph.addEdge(i, root)  # считывание маршрутов
            if node_is_end == False:
                routes_matrix = [[1000000 for j in range(len(nodes))] for k in range(len(nodes))]
                node_is_end = True
            routes_matrix[let_to_num[root[2][i].attrib['source']]][let_to_num[root[2][i].attrib['target']]] = int(
                root[2][i].attrib['weight'])
    return routes_matrix
