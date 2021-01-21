import dijkstra_graph as d_graph
import dijkstra_grid as d_grid
import bfs_graph
import bfs_grid
import a_star_grid
import a_star_graph
import dijkstra_make_matrix


type_of_data = input('Enter type: grid or graph\n')
if type_of_data == 'grid':
    from globals_grid import *
elif type_of_data == 'graph':
    from globals_graph import *

if algorithm == 'bfs':
    if type_of_data == 'graph':
        routes_dict = bfs_graph.make_routes()  # словарь вершмна : её соседи
        start_num = let_to_num[start]  # превращение букв в цифры, чтобы было легче работать
        finish_num = let_to_num[finish]
        for i in range(len(routes_dict)):
            pathes.append('0')  # пути к вершинам
        distance = bfs_graph.main(start_num)
        print('algorithm:', algorithm)
        print('type:', type_of_data)
        print(start, finish, '=', distance)
        let_closed = []
        let_open = []
        for i in closed:
            let_closed.append(num_to_let[i])  # превращение цифр в буквы для вывода
        for i in open:
            let_open.append(num_to_let[i])
        print('open:', let_open, ', closed:', let_closed)
        print('path:', pathes[finish_num])
    elif type_of_data == 'grid':
        print('algorithm:', algorithm)
        print('type:', type_of_data, connect)
        path = bfs_grid.algorithm()
        print('path:', path)
        print('start:', start, 'finsh:', finish, 'distance:', len(path))
        print('open:', open_id, 'closed:', closed_id)

if algorithm == 'dijkstra':
    if type_of_data == 'graph':
        routes_matrix = d_graph.make_routes()  # матрица вершина - вершина - длина их ребра
        start_num = let_to_num[start]  # превращение букв в цифры, чтобы было легче работать
        finish_num = let_to_num[finish]
        for i in range(len(routes_matrix)):
            pathes.append('0')
        print('algorithm:', algorithm)
        print('type:', type_of_data)
        print(start, finish, '=', d_graph.algorithm(start_num, let_to_num[finish], routes_matrix))
        let_closed = []
        for i in closed:
            let_closed.append(num_to_let[i])
        print('open:', open, ', closed:', let_closed)
        print('path:', pathes[let_to_num[finish]])
    elif type_of_data == 'grid':
        from globals_graph import let_to_num, pathes, num_to_let
        grid_to_graph = dijkstra_make_matrix.make_matrix()  # из матрицы грида делаем матрицу со связами (чтобы было видно соседей)
        routes_matrix = d_graph.make_routes()  # матрица вершина - вершина - длина их ребра (тут заодно num_to_let заполняется)
        start_num = matrix_numbers[start_i][start_j]  # matrix_numbers - матрица номеров вершин
        finish_num = matrix_numbers[finish_i][finish_j]
        for i in range(len(grid_to_graph)):
            pathes.append('')
        print('algorithm:', algorithm)
        print('type:', type_of_data)
        print(start, finish, '=', d_grid.algorithm(start_num, matrix_numbers[finish_i][finish_j], grid_to_graph))
        let_closed = []
        for i in closed:
            let_closed.append(num_to_let[i])
        print('open:', open, ', closed:', let_closed)
        grid_path = []  # чтобы путь выводился в виде точек с координатами (x, y)
        list_path = pathes[matrix_numbers[finish_i][finish_j]].split(' ')  # превращение строки в список
        for i in list_path:
            for j in range(len(matrix_numbers)):
                if int(i) in matrix_numbers[j]:
                    grid_path.append((j, matrix_numbers[j].index(int(i))))
        print('path:', grid_path)

if algorithm == 'astar':
    if type_of_data == 'grid':
        print('algorithm:', algorithm)
        print('type:', type_of_data, connect)
        print('start:', start, 'finsh:', finish)
        path, open_id, closed_id = a_star_grid.algorithm()
        print('path:', path)
        print('distance:', len(path))
        print('open:', open_id, 'closed:', closed_id)
    elif type_of_data == 'graph':
        open_id, closed_id = a_star_graph.main()
        let_closed = []
        let_open = []
        for i in closed_id:
            let_closed.append(num_to_let[i])
        for i in open_id:
            let_open.append(num_to_let[i])
        print('algorithm:', algorithm)
        print('type:', type_of_data)
        print(start, finish, '=', len(pathes[let_to_num[finish]])-1)
        print('open:', let_open, 'closed:', let_closed)
        print('path:', pathes[let_to_num[finish]])
