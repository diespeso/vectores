import pygame
import thorpy

class CajaTexto:

	def __init__(self, texto = "", position=(0, 0)):
		self.position = position
		self.area_texto = thorpy.make_text(texto, 12, (0, 0, 0))

	def get_caja(self):
		elements = [self.area_texto]
		caja = thorpy.Box(elements=elements)
		caja.set_topleft(self.position)

		return caja