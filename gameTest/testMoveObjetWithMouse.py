import pygame,sys
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
pygame.mouse.set_visible(0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mousePos = pygame.mouse.get_pos()
    x = mousePos[0]
    y = mousePos[1]

    screen.fill(BLANCO)

    pygame.draw.rect(screen, ROJO, (x, y ,10, 10))

    pygame.display.flip()
    clock.tick(60)