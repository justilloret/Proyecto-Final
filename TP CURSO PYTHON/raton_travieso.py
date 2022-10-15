# import pygame
# import random
# pygame.init()
# from Fondo import velocidad_del_juego, fondo,fondo_altura,fondo_ancho 
# from Ratón import personaje_del_juego, 

# def main():
#     global velocidad_del_juego, poosicion_x_fondo, posicion_Y_fondo, puntos, gato_obstáculo
#     correr = True
#     raton = personaje_del_juego(True, False)
#     velocidad_del_juego = 20
#     poosicion_x_fondo = 0
#     posicion_Y_fondo = 380
#     gato_obstáculo = []
#     contador_de_veces_perdidas = 0

#     while correr:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 correr = False

#         pantalla.fill((255, 255, 255))
#         userInput = pygame.key.get_pressed()

#         raton.dibujar(fondo)
#         raton.update(userInput)

#         if len(obstáculos) == 0:
#             if random.randint(0, 2) == 0:
#                 obstáculos.append(obstáculos(gato))

#         for obstáculos in obstáculos:
#             obstáculos.draw(pantalla)
#             obstáculos.update()
#             if raton.raton_rect.colliderect(obstáculos.rect):
#                 pygame.time.delay(2000)
#                 contador_de_veces_perdidas += 1
#                 menu(contador_de_veces_perdidas)

# pygame.display.update()

# def menu(contador_de_veces_perdidas):
#     global puntos
#     correr = True
#     while correr:
#         pantalla.fill((255, 255, 255))
#         fuente_de_las_letras = pygame.font.Font('freesansbold.ttf', 30)

#         if contador_de_veces_perdidas == 0:
#             texto = fuente_de_las_letras.render("Presciona espacio para empezar", True, (0, 0, 0))
#         elif contador_de_veces_perdidas > 0:
#             texto = fuente_de_las_letras.render("Preaciona espacio para seguir jugando", True, (0, 0, 0))
#             score = fuente_de_las_letras.render("centímetros recorridos: " + str(puntos), True, (0, 0, 0))
#             puntosRect = score.get_rect()
#             puntosRect.center = (fondo_ancho // 2, fondo_altura // 2 + 50)
#             pantalla.blit(score, puntosRect)
#         textoRect = texto.get_rect()
#         textoRect.center (fondo_ancho // 2, fondo_altura // 2)
#         pantalla.blit(texto, textoRect)
#         pantalla.blit(correr[0], (fondo_altura // 2 - 20, fondo_ancho // 2 - 140))
#         pygame.display.update()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 correr = False
#             if event.type == pygame.KEYDOWN:
#                 main()

# screen()
# main()
# fondo()
# puntos()
# menu(contador_de_veces_perdidas = 0)

# raton.draw(pantalla)
# # ratoncito.update(userInput)