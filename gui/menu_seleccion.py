import pygame
import thorpy

class MenuSeleccion:
	#no usar sin inicializar pygame.init() primero

	def __init__(self, titulo= "Selecciona:", opciones=[]):
		self.titulo = titulo
		self.checkers = {}
		for opcion in opciones:
			self.add_checker(opcion)
		self.last_checked = None
		self.titulo_element = thorpy.make_text(self.titulo, 12, (0, 0, 0))

	def add_checker(self, nombre):
		self.checkers[nombre] = thorpy.Checker(nombre, value=False)

	def check(self, nombre):
		#chequea una opcion y deschequea las demás
		self.uncheck_all()
		for _nombre, checker in self.checkers.items():
			if _nombre == nombre:
				self.checkers[_nombre].check()
				self.last_checked = _nombre

	def uncheck_all(self):
		for checker in self.checkers.values():
			checker.set_value(False)

	def get_checked(self):
		#mustra la opción elegida
		for nombre, checker in self.checkers.items():
			if checker.get_value() == True:
				return nombre

	def get_caja(self):
		elementos = [self.titulo_element]
		for checker in self.checkers.values():
			elementos.append(checker)

		return thorpy.Box(elements=elementos)

	def update(self):
		#hace que solo se vea elegida, la que fue elegida
		for _nombre, checker in self.checkers.items():
			if _nombre == self.last_checked:
				continue
			elif checker.get_value():
				self.check(_nombre)
				break
			#importante para que se muestre bien.
			checker.total_unblit()
