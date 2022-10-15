# import pygame
# import random
# pygame.init()

# raton = pygame.image.load(r"C:\Users\salta\Downloads\raton.png")

# class personaje_del_juego:
#     posición_y = 310
#     posición_x = 80
#     salto_velocidad = 8.5
#     velocidad_del_juego = 20

#     def __init__(self, correr, saltar):
#         self.correr = correr
#         self.saltar = saltar
#         # correr = True
#         # saltar = False

#         self.pasos = 0
#         self.imagen = self.correr
#         self.raton_rect = self.imagen
#         self.raton_rect = self.posición_y
#         self.raton_rect = self.posición_x
#         self.salto_velocidad = self.salto_velocidad

#     def correr(self):
#             self.raton_rect = self.imagen.get_rect()
#             self.raton_rect.x = self.posicion_x
#             self.raton_rect.y = self.posicion_y
#             self.pasos += 1

#     def saltar(self):
#         if self.raton_saltar:
#             self.raton_rect.y -= self.salto_velocidad * 4
#             self.salto_velocidad -= 0.8
#         if self.salto_velocidad < - self.salto_velocidad:
#             self.raton_saltar = False

#     def dibujar(self, fondo):
#         fondo.blit(self.image, (self.raton_rect.x, self.raton_rect.y))

#     def update (self, userInput):
#         if self.raton_correr:
#             self.correr()
#         if self.raton_saltar:
#             self.saltar()

#         if self.pasos >= 10: 
#             self.pasos = 0

#         if userInput[pygame.K_UP] and not self.raton_saltar:
#             self.raton_correr = False
#             self.raton_saltar = True
#         elif not (self.raton_saltar or userInput[pygame.K_DOWN]):
#             self.raton_correr = True
#             self.raton_saltar = False