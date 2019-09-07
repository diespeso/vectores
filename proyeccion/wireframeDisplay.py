from proyeccion import wireframe
from proyeccion.wireframe import *
import pygame

class ProjectionViewer:

	def __init__(self, superficie, tamano, displayEdges=True, displayNodes=True):
		self.width, self.height = tamano
		self.background = (0, 0, 0)
		self.screen = superficie

		self.wireframes = {}
		self.wireframe_colors = {}
		self.displayNodes = displayEdges
		self.displayEdges = displayNodes

		self.nodeColor = (255, 255, 255)
		self.edgeColor = (255, 255 ,255)

		self.nodeRadius = 3

		self.key_to_function = {
		pygame.K_d: (lambda x: x.translateAll([-10, 0, 0])),
		pygame.K_f: (lambda x: x.translateAll([0, 10, 0])),
		pygame.K_g: (lambda x: x.translateAll([10, 0, 0])),
		pygame.K_r: (lambda x: x.translateAll([0, -10, 0])),
		pygame.K_q: (lambda x: x.rotateAll('X', 0.1)),
		pygame.K_w: (lambda x: x.rotateAll('X', -0.1)),
		pygame.K_a: (lambda x: x.rotateAll('Y', 0.1)),
		pygame.K_s: (lambda x: x.rotateAll('Y', -0.1)),
		pygame.K_z: (lambda x: x.rotateAll('Z', 0.1)),
		pygame.K_x: (lambda x: x.rotateAll('Z', -0.1))
		}

	def run(self, event):
		"""
		key_to_function = {
		pygame.K_d: (lambda x: x.translateAll([-10, 0, 0])),
		pygame.K_f: (lambda x: x.translateAll([0, 10, 0])),
		pygame.K_g: (lambda x: x.translateAll([10, 0, 0])),
		pygame.K_r: (lambda x: x.translateAll([0, -10, 0])),
		pygame.K_q: (lambda x: x.rotateAll('X', 0.1)),
		pygame.K_w: (lambda x: x.rotateAll('X', -0.1)),
		pygame.K_a: (lambda x: x.rotateAll('Y', 0.1)),
		pygame.K_s: (lambda x: x.rotateAll('Y', -0.1)),
		pygame.K_z: (lambda x: x.rotateAll('Z', 0.1)),
		pygame.K_x: (lambda x: x.rotateAll('Z', -0.1))}
		"""
		if event.type == pygame.KEYDOWN:
			if event.key in self.key_to_function:
				self.key_to_function[event.key](self)
		self.display()
		"""
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.KEYDOWN:
					if event.key in key_to_function:
						key_to_function[event.key](self)

			self.display()
			pygame.display.flip()
		"""

	def addWireframe(self, name, wireframe, color=(255, 255, 255)):
		self.wireframes[name] = wireframe
		self.wireframe_colors[name] = color

	def display(self):
		self.screen.superficie.fill(self.background)

		for name, wireframe in self.wireframes.items():
			if self.displayNodes:
				for node in wireframe.nodes:
					pygame.draw.circle(self.screen.superficie, self.nodeColor, (int(node[0]), int(node[1])), self.nodeRadius, 0)
			
			if self.displayEdges:
				
				for node1, node2 in wireframe.edges:
					pygame.draw.aaline(self.screen.superficie, self.wireframe_colors[name] ,
						wireframe.nodes[node1][:2],
						wireframe.nodes[node2][:2],
						1)
				

	def translateAll(self, vector):
		matrix = translationMatrix(*vector) #unpack the tuple
		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

	def rotateAll(self, axis, theta):
		rotateFunction = 'rotate' + axis + 'Matrix'

		for wireframe in self.wireframes.values():
			centre = wireframe.findCentre()
			wireframe.transform(getattr(wireframe, rotateFunction)(theta))
			