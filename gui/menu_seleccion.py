import pygame
import thorpy

class MenuSeleccion:
	#no usar sin inicializar pygame.init() primero

	def __init__(self, opciones=[]):
		self.checkers = {}
		for opcion in opciones:
			self.add_checker(opcion)
		self.last_checked = None

	def add_checker(self, nombre):
		self.checkers[nombre] = thorpy.Checker(nombre, value=False)

	def check(self, nombre):
		self.uncheck_all()
		for _nombre, checker in self.checkers.items():
			if _nombre == nombre:
				#self.checkers[_nombre].value = True
				#print(self.checkers[_nombre].value)
				self.checkers[_nombre].check()
				self.last_checked = _nombre

	def uncheck_all(self):
		for checker in self.checkers.values():
			checker.set_value(False)

	def get_checked(self):
		for nombre, checker in self.checkers.items():
			if checker.get_value() == True:
				return nombre

	def get_caja(self):
		elementos = []
		for checker in self.checkers.values():
			elementos.append(checker)

		return thorpy.Box(elements=elementos)

	def update(self):
		for _nombre, checker in self.checkers.items():
			if _nombre == self.last_checked:
				continue
			elif checker.get_value():
				self.check(_nombre)
				break
			checker.total_unblit()
