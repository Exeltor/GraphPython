from grapher_core import Graph

g = Graph()

for n in range(10):
	g.addVertex(n)

g.vertexList

g.addEdge(1, 3)
g.addEdge(4, 7)
g.addEdge(8, 1)

for vertex in g:
	for w in vertex.getConnections():
		print("( %s , %s )" % (vertex.getData(), w.getData()))