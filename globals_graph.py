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
let_to_num = {}
num_to_let = {}
routes_dict = {}
open = []
closed = []
pathes = []
routes_matrix = []
