import pygame
import thorpy

import vector

import util


class VectorGui:
	#debe de iniciarse pygame.init() antes de usarla

	def leer_i(self):
		self.componentes[0] = int(self.insertion_i.get_value())

	def leer_j(self):
		self.componentes[1] = int(self.insertion_j.get_value())

	def leer_k(self):
		self.componentes[2] = int(self.insertion_k.get_value())

	def leer_todo(self):
		self.leer_i()
		self.leer_j()
		self.leer_k()

		self.vector = vector.Vector(self.componentes)
		print(self.vector)

		if self.projectionViewer != None:
			self.projectionViewer.addWireframe(self.name, self.vector.to_wireframe(), self.color)
		util.vector_flags[self.name] = self

	def __init__(self, size):
		self.componentes = [0, 0, 0]
		self.insertion_i = thorpy.Inserter("i:")
		self.insertion_j = thorpy.Inserter("j:")
		self.insertion_k = thorpy.Inserter("k:")
		self.boton = thorpy.make_button("Ok", func=self.leer_todo)

		self.projectionViewer = None
		self.vector = None

	def get_caja(self):
		return thorpy.Box(elements=[self.insertion_i,
			self.insertion_j, self.insertion_k,
			self.boton])

	def get_componentes(self):
		return self.componentes

	def get_vector(self):
		return self.vector

	def set_projectionViewer(self, projectionViewer, name, color=(255, 255, 255)):
		self.projectionViewer = projectionViewer
		self.color = color
		self.name = name