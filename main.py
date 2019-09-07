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
tamano_ventana = (480, 360)
ventana = pygame.display.set_mode((480, 360))
ventana.fill((255, 255, 255))

canvas = Canvas(ventana, tamano_ventana, (0, 0))
canvas.ajustarPredefinido()

gui_vector_a = VectorGui(tamano_ventana)
gui_vector_b = VectorGui(tamano_ventana)

menu = thorpy.Menu()
caja_vector_a = gui_vector_a.get_caja()
caja_vector_b = gui_vector_b.get_caja()
caja_vector_b.set_topleft((200, 0))

vector_c = vector.Vector([0, 0, 0])

menu.add_to_population(caja_vector_a)
menu.add_to_population(caja_vector_b)

for elemento in menu.get_population():
	elemento.surface = ventana

caja_vector_a.blit()
caja_vector_a.update()
caja_vector_b.blit()
caja_vector_b.update()

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
		pv.run(event)
		if "a" in util.vector_flags.keys() and "b" in util.vector_flags.keys() and not flag_vector_c:
			vector_c = gui_vector_a.get_vector()
			print("----------------")
			vector_c = vector_c.sumar(gui_vector_b.get_vector())
			print(vector_c)

			pv.addWireframe("c", vector_c.to_wireframe(), (255, 100, 150))
			flag_vector_c = True
	pygame.display.flip()
	canvas.update()
