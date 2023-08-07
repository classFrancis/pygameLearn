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

size = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coordX = 10
coordY = 10

speedX = 0
speedY = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            speedX = -3
        if event.key == pygame.K_RIGHT:
            speedX = 3
        if event.key == pygame.K_UP:
            speedY = -3
        if event.key == pygame.K_DOWN:
            speedY = 3
    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
           speedX = 0
        if event.key == pygame.K_RIGHT:
            speedX = 0
        if event.key == pygame.K_UP:
            speedY = 0
        if event.key == pygame.K_DOWN:
            speedY = 0
        
    
    screen.fill(BLANCO)

    coordX += speedX
    coordY += speedY

    pygame.draw.rect(screen, NARANJA,(coordX,coordY, 50, 50))

    pygame.display.flip()
    clock.tick(60)