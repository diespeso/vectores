from proyeccion.wireframe import Wireframe
from proyeccion.wireframe import Edge
from proyeccion import wireframeDisplay

class Vector:
	def __init__(self, componentes):
		self.i = componentes[0]
		self.j = componentes[1]
		self.k = componentes[2]

	def getTuple(self):
		return (self.i, self.j, self.k)

	def __str__(self):
		return "({}i, {}j, {}k)".format(self.i, self.j, self.k)

	def to_wireframe(self):
		wf = Wireframe()
		wf.addNodes([(0, 0, 0), (self.i* 10, self.j * 10, -self.k * 10)])
		wf.addEdges([(0, 1)])
		return wf

	def from_componentes(self, componentes):
		self.i = componentes[0]
		self.j = componentes[1]
		self.k = componentes[2]

	def sumar(self, vector):
		vectorSuma = Vector([0, 0, 0])
		vectorSuma.i = self.i + vector.i
		vectorSuma.j = self.j + vector.j
		vectorSuma.k = self.k + vector.k

		return vectorSuma

	def restar(self, vector):
		vectorResta = Vector([0, 0, 0])
		vectorResta.i = self.i - vector.i
		vectorResta.j = self.j - vector.j
		vectorResta.k = self.k - vector.k

		return vectorResta

	#no se grafica porque no produce vector
	def producto_punto(self, vector):
		sumatoria = 0
		sumatoria += self.i * vector.i
		sumatoria += self.j * vector.j
		sumatoria += self.k * vector.k

		return sumatoria

	def producto_cruz(self, vector):
		i = (self.j * vector.k) - (self.k * vector.j)
		j = - ((self.i * vector.k) - (self.k * vector.i))
		k = (self.i * vector.j) - (self.j * vector.i)

		return Vector([i, j, k])

