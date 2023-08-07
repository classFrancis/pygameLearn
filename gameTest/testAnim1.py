import pygame,sys,random
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

coordList = []
for i in range(60):
    x = random.randint(0,800)
    y = random.randint(0,500)
    coordList.append([x,y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLANCO)

    for coord in coordList:
        pygame.draw.circle(screen, NARANJA, coord, 2)
        coord[1] += 1
        if coord[1] > 600:
            coord[1] = 0

    pygame.display.flip()
    clock.tick(60)