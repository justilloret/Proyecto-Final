# import pygame
# import random
# pygame.init()
# from Fondo import velocidad_del_juego, fondo_altura, fondo_ancho

# gato = pygame.image.load(r"C:\Users\salta\Downloads\GATO PARA TP DE PYTHON.png")

# class obstáculos:
#     def __init__(self,imagen, tipo):
#      self.imagen = imagen
#      self.tipo = tipo
#      self.rect = self.imagen[self.type].get_rect()
#      self.rect.x = fondo_ancho
#      self.type = random.randint(0, 2)
#      super().__init__(imagen, self.type)
#      self.rect.y = 300

#     def update(self):
#         self.rect.x -= velocidad_del_juego
#         if self.rect.x < -self.rect.width:
#             obstáculos.pop()

#     def dibujar(self,pantalla):
#      pantalla.blit(self.imagen[self.tipo], self.rect)
