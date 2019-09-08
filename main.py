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
pygame.font.init()
#imports que solo funcionan después de pygame.init()
from gui.vector_gui import VectorGui
from gui.menu_seleccion import MenuSeleccion
from gui.caja_texto import CajaTexto

tamano_ventana = (640, 420)
ventana = pygame.display.set_mode(tamano_ventana)
ventana.fill((255, 255, 255))

canvas = Canvas(ventana, tamano_ventana, (0, 0))
canvas.ajustarPredefinido()

#las cajas de entrada de los vectores
gui_vector_a = VectorGui(tamano_ventana)
gui_vector_b = VectorGui(tamano_ventana)
#el menu de seleccion
gui_menu_s = MenuSeleccion(titulo="Elige una operación",
	opciones=["suma", "resta",
	"producto punto", "producto cruz"])

#empiezan las declaraciones del plano 3d
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
#terminan las declaraciones del plano 3d


#se arma y llena el motor de proyecciones
pv = wireframeDisplay.ProjectionViewer(canvas, canvas.tamano, displayEdges=False)
pv.addWireframe("eje_i_positivo", eje_i_positivo, (255, 0, 0))
pv.addWireframe("eje_i_negativo", eje_i_negativo, (100, 0, 0))
pv.addWireframe("eje_j_positivo", eje_j_positivo, (0 ,255, 0))
pv.addWireframe("eje_j_negativo", eje_j_negativo, (0 ,100, 0))
pv.addWireframe("eje_k_positivo", eje_k_positivo, (0, 0, 255))
pv.addWireframe("eje_k_negativo", eje_k_negativo, (0, 0, 100))

#se manda el motor de proyecciones a las entradas de vectores a y b
gui_vector_a.set_projectionViewer(pv, "a", (255, 255, 0)) #amarillo
gui_vector_b.set_projectionViewer(pv, "b") #blanco



menu = thorpy.Menu()
#hacer cajas de las instancias de la clase vector
#posicionarlas
caja_vector_a = gui_vector_a.get_caja()
caja_vector_a.set_topleft((150, 0))
caja_vector_b = gui_vector_b.get_caja()
caja_vector_b.set_topleft((255, 0))

#el vector del resultado, sin gui
vector_c = vector.Vector([0, 0, 0])

#hacer una caja a partir de la clase y posicionarla
caja_menu_s = gui_menu_s.get_caja()

#texto para el vector c
fuente = pygame.font.SysFont("arial", 14)
posicion_fuente = (370, 10)
#mensaje de resultado
mensaje_resultado = fuente.render("Resultado:", False, (0, 0, 0))
gui_vector_c = fuente.render("", False, (0, 0, 0))

caja_nota = CajaTexto(
	"Nota: i: rojo,j: verde,\nk:azul.\n" +
	"los ejes\n negativos son obscuros\n" +
	"usa q,w,a,s,z,x para rotar\n" + 
	"usa r,d,f,g para trasladar", position=(380, 40))

caja_nota_real = caja_nota.get_caja()

menu.add_to_population(caja_vector_a)
menu.add_to_population(caja_vector_b)
menu.add_to_population(caja_menu_s)
menu.add_to_population(caja_nota_real)

#se indica que se renderizará a la ventana
for elemento in menu.get_population():
	elemento.surface = ventana

#para que todo salga bien, limpio
caja_vector_a.blit()
caja_vector_a.update()
caja_vector_b.blit()
caja_vector_b.update()
caja_menu_s.blit()
caja_menu_s.update()
caja_nota_real.blit()
caja_nota_real.update()

corriendo = True
flag_vector_c = False
while corriendo:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			corriendo = False
		menu.react(event)
		gui_menu_s.update()
		pv.run(event)

		#si se introdujeron ambos vectores, sólo una vez
		if "a" in util.vector_flags.keys() and "b" in util.vector_flags.keys() and not flag_vector_c:
			vector_c = gui_vector_a.get_vector()
			if gui_menu_s.get_checked() == "suma":
				vector_c = vector_c.sumar(gui_vector_b.get_vector())
				gui_vector_c = fuente.render("c: {}".format(vector_c), False, (0, 0, 0))
			elif gui_menu_s.get_checked() == "resta":
				vector_c = vector_c.restar(gui_vector_b.get_vector())
				gui_vector_c = fuente.render("c: {}".format(vector_c), False, (0, 0, 0))
			elif gui_menu_s.get_checked() == "producto punto":
				#no se grafica
				producto_punto = vector_c.producto_punto(gui_vector_b.get_vector())
				gui_vector_c = fuente.render("Escalar: {}".format(producto_punto), False, (0, 0, 0))
			elif gui_menu_s.get_checked() == "producto cruz":
				vector_c = vector_c.producto_cruz(gui_vector_b.get_vector())
				gui_vector_c = fuente.render("c: {}".format(vector_c), False, (0, 0, 0))
			else:
				print("!!!!!!!!!!!!!!!!!!!!!!!! Opcion no vaĺida, esto no debería pasar. Revisar el código")
			#salida a consola
			print(gui_vector_a)
			print(gui_vector_b)
			print("{}: {}".format("c", vector_c))
			#se grafica el vector c, resultante
			pv.addWireframe("c", vector_c.to_wireframe(), (255, 100, 150))
			#se mueve todo al centro para mostrarse bien
			pv.translateAll((canvas.get_tamano_lista()[0], canvas.get_tamano_lista()[1] * 0.5, 0))
			flag_vector_c = True
	#rutinas de renderizado de sistemas y de pygame		
	ventana.blit(mensaje_resultado, (370, 0))
	ventana.blit(gui_vector_c, (370, 15))
	pygame.display.flip()
	canvas.update()

