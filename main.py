#!/usr/bin/env python3

from canvas import Canvas
from proyeccion.wireframe import Wireframe
from proyeccion.wireframe import Edge
from proyeccion import wireframeDisplay
import pygame
import thorpy

import util

import vector

pygame.init()
from gui.vector_gui import VectorGui
from gui.menu_seleccion import MenuSeleccion

tamano_ventana = (480, 360)
ventana = pygame.display.set_mode((480, 360))
ventana.fill((255, 255, 255))

canvas = Canvas(ventana, tamano_ventana, (0, 0))
canvas.ajustarPredefinido()

gui_vector_a = VectorGui(tamano_ventana)
gui_vector_b = VectorGui(tamano_ventana)
gui_menu_s = MenuSeleccion(opciones=["suma", "resta",
	"producto punto", "producto cruz"])

menu = thorpy.Menu()
#hacer cajas de las instancias de la clase vector
#posicionar la segunda
caja_vector_a = gui_vector_a.get_caja()
caja_vector_a.set_topleft((150, 0))
caja_vector_b = gui_vector_b.get_caja()
caja_vector_b.set_topleft((255, 0))

vector_c = vector.Vector([0, 0, 0])

#hacer una caja a partir de la clase y posicionarla
caja_menu_s = gui_menu_s.get_caja()

menu.add_to_population(caja_vector_a)
menu.add_to_population(caja_vector_b)
menu.add_to_population(caja_menu_s)

for elemento in menu.get_population():
	elemento.surface = ventana

#para que todo salga bien, limpio
caja_vector_a.blit()
caja_vector_a.update()
caja_vector_b.blit()
caja_vector_b.update()
caja_menu_s.blit()
caja_menu_s.update()

eje_i_positivo = Wireframe()
eje_i_negativo = Wireframe()
eje_j_positivo = Wireframe()
eje_j_negativo = Wireframe()
eje_k_positivo = Wireframe()
eje_k_negativo = Wireframe()

eje_i_positivo.addNodes([(0, 0, 0), (100, 0, 0)])
eje_i_negativo.addNodes([(0, 0, 0), (-100, 0, 0)])
eje_j_positivo.addNodes([(0, 0, 0), (0, 100, 0)])
eje_j_negativo.addNodes([(0, 0, 0), (0, -100, 0)])
eje_k_negativo.addNodes([(0, 0, 0), (0, 0, 100)])
eje_k_positivo.addNodes([(0, 0, 0), (0, 0, -100)])

eje_i_positivo.addEdges([(0, 1)])
eje_i_negativo.addEdges([(0, 1)])
eje_j_positivo.addEdges([(0, 1)])
eje_j_negativo.addEdges([(0, 1)])
eje_k_positivo.addEdges([(0, 1)])
eje_k_negativo.addEdges([(0, 1)])

pv = wireframeDisplay.ProjectionViewer(canvas, canvas.tamano, displayEdges=False)
pv.addWireframe("eje_i_positivo", eje_i_positivo, (255, 0, 0))
pv.addWireframe("eje_i_negativo", eje_i_negativo, (100, 0, 0))
pv.addWireframe("eje_j_positivo", eje_j_positivo, (0 ,255, 0))
pv.addWireframe("eje_j_negativo", eje_j_negativo, (0 ,100, 0))
pv.addWireframe("eje_k_positivo", eje_k_positivo, (0, 0, 255))
pv.addWireframe("eje_k_negativo", eje_k_negativo, (0, 0, 100))

gui_vector_a.set_projectionViewer(pv, "a", (255, 255, 0))
gui_vector_b.set_projectionViewer(pv, "b")
#pv.translateAll((canvas.tamano[0], canvas.tamano[1] * 0.5, 0))
pv.rotateAll("X", 0.1)
pv.rotateAll("Y", 0.3)

corriendo = True
flag_vector_c = False
while corriendo:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			corriendo = False
		menu.react(event)
		gui_menu_s.update()
		pv.run(event)
		if "a" in util.vector_flags.keys() and "b" in util.vector_flags.keys() and not flag_vector_c:
			vector_c = gui_vector_a.get_vector()
			if gui_menu_s.get_checked() == "suma":
				vector_c = vector_c.sumar(gui_vector_b.get_vector())
			elif gui_menu_s.get_checked() == "resta":
				vector_c = vector_c.restar(gui_vector_b.get_vector())
			elif gui_menu_s.get_checked() == "producto punto":
				#todo: no se grafica, mostrarlo en texto
				producto_punto = vector_c.producto_punto(gui_vector_b.get_vector())
			elif gui_menu_s.get_checked() == "producto cruz":
				vector_c = vector_c.producto_cruz(gui_vector_b.get_vector())
			else:
				print("!!!!!!!!!!!!!!!!!!!!!!!! Opcion no vaĺida, esto no debería pasar. Revisar el código")
			print(gui_vector_a)
			print(gui_vector_b)
			print("{}: {}".format("c", vector_c))

			pv.addWireframe("c", vector_c.to_wireframe(), (255, 100, 150))
			flag_vector_c = True
	pygame.display.flip()
	canvas.update()
