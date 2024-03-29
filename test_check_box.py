#!/usr/bin/env python3
import pygame
import thorpy

tamano = (400, 400)

pygame.init()
pantalla = pygame.display.set_mode(tamano)
pantalla.fill((255, 255, 255))

class MenuSeleccion:

	def __init__(self, opciones=[]):
		self.checkers = {}
		for opcion in opciones:
			self.addChecker(opcion)
		self.last_checked = None

	def addChecker(self, nombre):
		self.checkers[nombre] = thorpy.Checker(nombre, value=False)

	def check(self, nombre):
		self.uncheckAll()
		for _nombre, checker in self.checkers.items():
			if _nombre == nombre:
				#self.checkers[_nombre].value = True
				#print(self.checkers[_nombre].value)
				self.checkers[_nombre].check()
				self.last_checked = _nombre

	def uncheckAll(self):
		for checker in self.checkers.values():
			checker.set_value(False)

	def getChecked(self):
		for nombre, checker in self.checkers.items():
			if checker.get_value() == True:
				return nombre

	def to_caja(self):
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

menu_s = MenuSeleccion(opciones=["suma", "resta",
	"producto punto", "producto vectorial"])
"""
menu_s.addChecker("suma")
menu_s.addChecker("resta")
menu_s.addChecker("producto punto")
menu_s.addChecker("producto vectorial")
"""

caja = menu_s.to_caja()
menu = thorpy.Menu()
menu.add_to_population(caja)

for elemento in menu.get_population():
	elemento.surface = pantalla

caja.blit()
caja.update()


corriendo = True
while corriendo:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			corriendo = False

	menu.react(evento)
	menu_s.update()
	print(menu_s.getChecked())

	pygame.display.flip()

pygame.quit()