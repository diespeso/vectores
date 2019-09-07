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
		return "{}i {}j {}k".format(self.i, self.j, self.k)

	def to_wireframe(self):
		wf = Wireframe()
		wf.addNodes([(0, 0, 0), (self.i* 10, self.j * 10, -self.k * 10)])
		wf.addEdges([(0, 1)])
		return wf

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

	