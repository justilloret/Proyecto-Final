import pygame
import random
pygame.init()

fondo_altura= 600
fondo_ancho = 1100
pantalla = pygame.display.set_mode(int(fondo_altura), int(fondo_ancho))

ratoncito = pygame.image.load(r"C:\Users\salta\Downloads\raton.png")
gato = pygame.image.load(r"C:\Users\salta\Downloads\GATO PARA TP DE PYTHON.png")
fondo = pygame.image.load(r"C:\Users\salta\Downloads\cocina.jpg")

class personaje_del_juego:
    posición_y = 310
    posición_x = 80
    salto_velocidad = 8.5
    velocidad_del_juego = 20

    def __init__(self, correr, saltar):
        self.correr_imagen = correr
        self.saltar_imagen = saltar
        self.correr = True
        self.saltar = False

        self.step_index = 0
        self.imagen = self.correr.imagen [0]
        self.raton_rect = self.image.get_rect()
        self.raton_rect.y = self.posición_y
        self.raton_rect.x = self.posición_x
        self.salto_velocidad = self.salto_velocidad
 
    
    def update (self, userInput):
        if self.raton_correr:
            self.correr()
        if self.raton_saltar:
            self.saltar()

        if self.step_index >= 10: 
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.raton_saltar:
            self.raton_correr = False
            self.raton_saltar = True
        elif not (self.raton_saltar or userInput[pygame.K_DOWN]):
            self.raton_correr = True
            self.raton_saltar = False

    def correr(self):
            self.raton_rect = self.imagen.get_rect()
            self.raton_rect.x = self.posicion_x
            self.raton_rect.y = self.posicion_y
            self.step_index += 1

    def saltar(self):
        if self.raton_saltar:
            self.raton_rect.y -= self.salto_velocidad * 4
            self.salto_velocidad -= 0.8
        if self.salto_velocidad < - self.salto_velocidad:
            self.raton_saltar = False

    def dibujar(self, fondo):
        fondo.blit(self.image, (self.raton_rect.x, self.raton_rect.y))

class obstáculos:
    def __init__(self,imagen, tipo):
     self.imagen = imagen
     self.tipo = tipo
     self.rect = self.imagen[self.type].get_rect()
     self.rect.x = fondo_ancho
     self.type = random.randint(0, 2)
     super().__init__(imagen, self.type)
     self.rect.y = 300

    def update(self):
        self.rect.x -= velocidad_del_juego
        if self.rect.x < -self.rect.width:
            obstáculos.pop()

    def draw(self,pantalla):
     pantalla.blit(self.imagen[self.tipo], self.rect)

def main():
    global velocidad_del_juego, poosicion_x_fondo, posicion_Y_fondo, puntos, gato_obstáculo
    correr = True
    raton = personaje_del_juego()
    velocidad_del_juego = 20
    poosicion_x_fondo = 0
    posicion_Y_fondo = 380
    puntos = 0
    fuente_de_las_letras = pygame.font.Font('freesansbold.ttf', 20)
    gato_obstáculo = []
    contador_de_veces_perdidas = 0

    def puntos():
        global puntos, velocidad_del_juego
        puntos += 1
        if puntos % 100 == 0:
            velocidad_del_juego += 1

        texto = fuente_de_las_letras.render("centímetros recorridos: " + str(puntos), True, (0, 0, 0))
        textoRect = texto.get_rect()
        textoRect.center = (1000, 40)
        pantalla.blit(texto, textoRect)

    def fondo():
        global posicion_X_fondo, posicion_Y_fondo
        imagen_largo = fondo.get_width()
        pantalla.blit(fondo, (posicion_X_fondo, posicion_Y_fondo))
        pantalla.blit(fondo, (imagen_largo + posicion_X_fondo, posicion_Y_fondo))
        if posicion_X_fondo <= -imagen_largo:
            pantalla.blit(fondo, (imagen_largo + posicion_X_fondo, posicion_Y_fondo))
            posicion_X_fondo = 0
        posicion_X_fondo -= velocidad_del_juego

    while correr:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correr = False

        pantalla.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        raton.draw()
        raton.update(userInput)

        if len(obstáculos) == 0:
            if random.randint(0, 2) == 0:
                obstáculos.append(gato(gato))

        for obstáculos in obstáculos:
            obstáculos.draw(pantalla)
            obstáculos.update()
            if raton.raton_rect.colliderect(obstáculos.rect):
                pygame.time.delay(2000)
                contador_de_veces_perdidas += 1
                menu(contador_de_veces_perdidas)


   

fondo()
puntos()

pygame.display.update()


def menu(contador_de_veces_perdidas):
    global puntos
    correr = True
    while correr:
        pantalla.fill((255, 255, 255))
        fuente_de_las_letras = pygame.font.Font('freesansbold.ttf', 30)

        if contador_de_veces_perdidas == 0:
            texto = fuente_de_las_letras.render("Presciona espacio para empezar", True, (0, 0, 0))
        elif contador_de_veces_perdidas > 0:
            texto = fuente_de_las_letras.render("Preaciona espacio para seguir jugando", True, (0, 0, 0))
            score = fuente_de_las_letras.render("centímetros recorridos: " + str(puntos), True, (0, 0, 0))
            puntosRect = score.get_rect()
            puntosRect.center = (fondo_ancho // 2, fondo_altura // 2 + 50)
            pantalla.blit(score, puntosRect)
        textoRect = texto.get_rect()
        textoRect.center (fondo_ancho // 2, fondo_altura // 2)
        pantalla.blit(texto, textoRect)
        pantalla.blit(correr[0], (fondo_altura // 2 - 20, fondo_ancho // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correr = False
            if event.type == pygame.KEYDOWN:
                main()


menu(contador_de_veces_perdidas = 0)

ratoncito.draw(pantalla)
# ratoncito.update(userInput)