import pygame, sys

pygame.init()

# Definiciones de colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
CIAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRIS = (127, 127, 127)
NARANJA = (255, 165, 0)

#Pantalla
size = (500,300)
screen = pygame.display.set_mode(size)
#FPS
clock = pygame.time.Clock()

#coordenadas
cordX = 100
cordY = 50
#Velocidad
speedX = 4
speedY = 4

#Loop principal
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    #-----------Logica-----------#
    if (cordX > 450 or cordX < 0):
        speedX *= -1

    if (cordY > 250 or cordY < 0):
        speedY *= -1

    cordX += speedX
    cordY += speedY

    #-----------Logica-----------#

    #Rellenar pantalla
    screen.fill(NARANJA)

    #-----------Draw Zone--------------#

    pygame.draw.rect(screen, AZUL, (cordX,cordY, 50,50))

    #-----------Draw Zone--------------#
    pygame.display.flip()
    clock.tick(60)