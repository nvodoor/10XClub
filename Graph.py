class Node():

	def __init__(self, vertex):
		self.vertex = vertex;
		self.value = None;
		self.edge = [];


class Graph():

	def __init__(self):
		self.vertexes = [];

	def add_vertex(x):

		vertice = Node(x);
		self.vertexes.append(vertice)

	def remove_vertex(x):

		for vertice in self.vertexes:
			if vertice.vertex == x:
				del self.vertexes[vertice]

	def add_edge(x,y):

		for vertice in self.vertexes:
			if vertice.vertex == y:
				if x not in vertice.edge:
					vertice.edge.append(x);
		return True

	def remove_edge(x,y):

		for vertice in self.vertexes:
			if vertice.vertex == y:
				if x in vertice.edge:
					del vertice.edge[x]


	def get_vertex_value(x):

		for vertice in self.vertexes:
			if vertice.vertex == x:
				return vertice.value

	def set_vertex_value(x,v):

		for vertice in self.vertexes:
			if vertice.vertex == x:
				vertice.value = v

	def adjacent(x,y):

		for vertice in self.vertexes:
			if vertice.vertex == x:
				if y in vertice.edge:
					return True
				else:
					return False

	def neighbors(x):

		for vertice in self.vertexes:
			if vertice.vertex == x:
				return vertice.edge

