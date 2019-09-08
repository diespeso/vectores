import pygame

class Canvas:
	#una subventana para renderizar lo que se quiera
	def __init__(self, pantalla, tamano, origen):
		self.tamano = tamano
		self.origen = origen
		self.pantalla = pantalla
		self.superficie = pygame.Surface(tamano)
		self.ratio_vertical = 0.60 #ajusta la proporción vertical
		self.ratio_horizontal = 0.5 #no es relevante al final

	def getSuperficie(self):
		return self.superficie

	def update(self):
		self.pantalla.blit(self.superficie, self.origen)

	def get_tamano_lista(self):
		#muestra el tamano en forma de array []
		width, height = self.tamano
		return [width, height]


	def ajustarPredefinido(self):
		#ajusta las proporciones a la ventana.
		self.tamano = (self.tamano[0] * self.ratio_horizontal, self.tamano[1] * self.ratio_vertical)
		self.origen = (self.origen[0], self.pantalla.get_height() * (1 - self.ratio_vertical)) # para que quede abajo
