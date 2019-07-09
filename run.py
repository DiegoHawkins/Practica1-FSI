# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
sp = search.GPSProblem('S', 'P', search.romania)

print('----------Búsqueda en anchura AB------------')
print(search.breadth_first_graph_search(ab).path())
print('----------Búsqueda en profundidad AB------------')
print(search.depth_first_graph_search(ab).path())
print('----------Ramificación y acotación AB ------------')
print(search.ram_aco(ab).path())
print('----------Ramificación y acotación con subestimación AB------------')
print(search.ram_aco_sub(ab).path())

print('********************************************************************')

print('----------Búsqueda en anchura SP------------')
print(search.breadth_first_graph_search(sp).path())
print('----------Búsqueda en profundidad SP------------')
print(search.depth_first_graph_search(sp).path())
print('----------Ramificación y acotación SP------------')
print(search.ram_aco(sp).path())
print('----------Ramificación y acotación con subestimación SP------------')
print(search.ram_aco_sub(sp).path())



# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
