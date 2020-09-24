# все глобальные перменные для функций, которые работают с графом
# и считывание xml
import xml.etree.ElementTree as ET

tree = ET.parse("graph_example.xml")
root = tree.getroot()

start = root[1].attrib['start.id']
finish = root[1].attrib['goal.id']
algorithm = root[0].attrib['type']
nodes = []
edges = []
let_to_num = {}  # словарь номер вершины : буквенное обозначение
num_to_let = {}  # буквенное обозначение : словарь номер вершины
routes_dict = {}  # словарь вершина : её соседи
open = []
closed = []
pathes = []
routes_matrix = []  # матрица стоимости связей между вершинами
