import numpy as np

class Edge:

	def __init__(self, start, stop):
		self.start = start
		self.stop = stop

class Wireframe:

	def __init__(self):
		self.nodes = np.zeros((0, 4))
		self.edges = []

	def addNodes(self, node_array):
		ones_column = np.ones((len(node_array), 1))
		ones_added = np.hstack((node_array, ones_column))
		self.nodes = np.vstack((self.nodes, ones_added))

	def addEdges(self, edgeList):
		self.edges += edgeList

	def showEdges(self):
		print("--- EDGES ---")
		for i, (x, y, z, _) in enumerate(self.nodes):
			print("   %d: (%d, %d, %d)" % (i, x, y, z))

	def showNodes(self):
		print("--- NODES ---")
		for i, (node1, node2) in enumerate(self.edges):
			print("   %d: %d -> %d" % (i, node1, node2))

	def findCentre(self):
		"""num_nodes = len(self.nodes)
		meanX = sum([node[0] for node in self.nodes]) / num_nodes
		meanY = sum([node[1]for node in self.nodes]) / num_nodes
		meanZ = sum([node[2] for node in self.nodes]) / num_nodes
"""
		min_values = self.nodes[:,:-1].min(axis=0)
		max_values = self.nodes[:,:-1].max(axis=0)
		return 0.5 * (min_values + max_values)

		#return (meanX, meanY, meanZ)

	def transform(self, matrix):
		#apply the transformation aka matrix ending functs
		self.nodes = np.dot(self.nodes, matrix)


	def scaleMatrix(sx = 0, sy = 0, sz = 0):
		return np.array([
			[sx, 0, 0, 0],
			[0, sx, 0, 0],
			[0, 0, sz, 0],
			[0, 0, 0, 1]
			])

	def rotateXMatrix(self, radians):
		c = np.cos(radians)
		s = np.sin(radians)

		return np.array([
			[1, 0, 0, 0],
			[0, c, -s, 0],
			[0, s, c, 0],
			[0, 0, 0, 1]
			])

	def rotateYMatrix(self, radians):
		c = np.cos(radians)
		s = np.sin(radians)

		return np.array([
			[c, 0, s, 0],
			[0, 1, 0, 0],
			[-s, 0, c, 0],
			[0, 0, 0, 1]
			])

	def rotateZMatrix(self, radians):
		c = np.cos(radians)
		s = np.sin(radians)

		return np.array([
			[c, -s, 0, 0],
			[s, c, 0, 0,],
			[0, 0, 1, 0],
			[0, 0, 0, 1]
			])

def translationMatrix(dx = 0, dy = 0, dz = 0):
	return np.array([
		[1, 0, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 1, 0],
		[dx, dy, dz, 1]
		])