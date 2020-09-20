# все глобальные перменные для функций, которые работают с гридом
# и считывание xml
import xml.etree.ElementTree as ET

name = "grid_example.xml"
tree = ET.parse(name)
root = tree.getroot()

algorithm = root[0].attrib['type']
start_i = int(root[1].attrib['start.i'])
start_j = int(root[1].attrib['start.j'])
finish_i = int(root[1].attrib['goal.i'])
finish_j = int(root[1].attrib['goal.j'])
connect = int(root[2].attrib['connectedness'])
width = int(root[2].attrib['width'])
height = int(root[2].attrib['height'])

start = (start_i, start_j)
finish = (finish_i, finish_j)

shift8 = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
shift4 = [(0, -1), (0, 1), (-1, 0), (1, 0)]

open = []
closed = []

grid = []
for row in range(width):
    grid.append([])
    for column in range(height * 2-1):
        if column % 2 == 0:
            grid[row].append(int(root[2][row].text[column]))

# для дейкстры
matrix_numbers = [[[] for j in range(width)] for i in range(height)]
