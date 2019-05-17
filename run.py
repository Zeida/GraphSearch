# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
ac = search.GPSProblem('A', 'C'
                       , search.romania)
az = search.GPSProblem('A', 'Z'
                       , search.romania)
bz = search.GPSProblem('B', 'Z'
                       , search.romania)
ba = search.GPSProblem('B', 'A'
                       , search.romania)

#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())
print("Ramificación y acotación")
print(search.branch_and_bounds(ac).path())
print("Ramificación y acotación con subestimación")
print(search.ramificacion_acotacion_subestimacion(ac).path())
print("######################################################")
print("Ramificación y acotación")
print(search.branch_and_bounds(az).path())
print("Ramificación y acotación con subestimación")
print(search.ramificacion_acotacion_subestimacion(az).path())
print("######################################################")
print("Ramificación y acotación")
print(search.branch_and_bounds(bz).path())
print("Ramificación y acotación con subestimación")
print(search.ramificacion_acotacion_subestimacion(bz).path())
print("######################################################")
print("Ramificación y acotación")
print(search.branch_and_bounds(ba).path())
print("Ramificación y acotación con subestimación")
print(search.ramificacion_acotacion_subestimacion(ba).path())
print("######################################################")
print("Ramificación y acotación")
print(search.branch_and_bounds(ab).path())
print("Ramificación y acotación con subestimación")
print(search.ramificacion_acotacion_subestimacion(ab).path())




# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
