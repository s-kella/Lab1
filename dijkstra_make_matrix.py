from globals_grid import *


def make_matrix():
    if connect == 4:  # четырёхсвязный
        shifts = shift4
    elif connect == 8:  # восьмисвязный
        shifts = shift8

    count_of_nodes = height * width
    matrix_grid_to_graph = [[8 for j in range(count_of_nodes)] for i in range(count_of_nodes)]

    count = 0
    for i in matrix_numbers:
        for j in range(height):
            i[j] = count
            count += 1
# заполнение матрицы соседей
    for row in range(width):
        for column in range(height * 2 - 1):
            for shift in shifts:
                try:
                    # если в гриде нет стены и индексы положительные (не будут искаться ячейки "с конца")
                    if grid[row + shift[0]][column + shift[1]] == 0 and grid[row][column] == 0 and row + shift[0] >= 0 and column + shift[1] >= 0:
                        # то два элемента считаются соседями
                        matrix_grid_to_graph[matrix_numbers[row][column]][matrix_numbers[row + shift[0]][column + shift[1]]] = 1
                        matrix_grid_to_graph[matrix_numbers[row + shift[0]][column + shift[1]]][matrix_numbers[row][column]] = 1
                except IndexError:
                    continue

    return matrix_grid_to_graph
