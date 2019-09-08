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
		self.titulo = None

	def __str__(self):
		return "{}: ({}i, {}j, {}k)".format(self.name,
			self.componentes[0],
			self.componentes[1],
			self.componentes[2])

	def get_caja(self):
		return thorpy.Box(elements=[self.titulo, self.insertion_i,
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
		self.titulo = thorpy.make_text(self.name, 12, (0, 0, 0))