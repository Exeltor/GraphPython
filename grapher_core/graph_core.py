class Graph:
	def __init__(self):
		self.vertexList = {}
		self.vertexNum = 0

	def addVertex(self, data):
		self.vertexNum += 1
		newVertex = Vertex(data)
		self.vertexList[data] = newVertex

	def getVertex(self, data):
		if data in self.vertexList:
			return self.vertexList[data]
		else:
			return None

	def addEdge(self, origin, dest, cost = 0):
		if origin not in self.vertexList:
			self.addVertex(origin)
		if dest not in self.vertexList:
			self.addVertex(dest)

		self.vertexList[origin].addConnection(self.vertexList[dest], cost)

	def getEdges(self):
		return self.vertexList.keys()

	def __contains__(self, data):
		return data in self.vertexList

	def __iter__(self):
		return iter(self.vertexList.values())



class Vertex:
	def __init__(self, data):
		self.data = data
		self.connectedTo = {}

	def addConnection(self, target, cost = 0):
		self.connectedTo[target] = cost

	def getConnections(self):
		return self.connectedTo.keys()

	def getData(self):
		return self.data

	def getCost(self, target):
		return self.connectedTo[target]