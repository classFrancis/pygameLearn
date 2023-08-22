import pygame,random
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

#Funciones
def getRandomPosition():
    return (random.randint(0, size[0]-20), random.randint(0, size[1]-20))
def playerWidthModiFeed(width):
    width = width + 1
    return (width)
def playerSpeedModiFeed(speed):
    speed = speed + 0.2
    return (speed)

def playerWidthModiPoison(width):
    width = width - 1
    return (width)
def playerSpeedModiPoison(speed):
    speed = speed -1
    return (speed)

#Variables
size = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = False
poisonPositions = []
feedRandomPosition = getRandomPosition()
poisonRandomPosition = getRandomPosition()
playerWidth = 10
playerHeight = 10
playerCoordX = 10 
playerCoordY = 10
playerSpeedX = 5
playerSpeedY = 0

#Ciclo principal
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerSpeedY = -5
            if event.key == pygame.K_s:
                playerSpeedY = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                playerSpeedY = 0
            if event.key == pygame.K_s:
                playerSpeedY = 0  

    #Colisiones con bordes de pantalla eje X e Y
    if playerCoordX > size[0]:
        playerCoordX = 0 - playerWidth
    elif playerCoordX + playerWidth < 0:
        playerCoordX = size[0]
    if playerCoordY < 0:
        playerCoordY = 0
    if playerCoordY > size[1] - playerHeight:
        playerCoordY = size[1] - playerHeight
    
    #Relleno de pantalla
    screen.fill(NEGRO)
    #---------------DrawZone-----------------------#
    playerCoordX += playerSpeedX
    playerCoordY += playerSpeedY
        
    poison = pygame.draw.circle(screen,MAGENTA,poisonRandomPosition,5)
    feed = pygame.draw.circle(screen,VERDE,feedRandomPosition,5)
    player = pygame.draw.rect(screen,AZUL,(playerCoordX,playerCoordY,playerWidth,playerHeight))
    
    #Colisiones
    #Con efectos positivos
    if feed.colliderect(player):
        feedRandomPosition = getRandomPosition()
        poisonRandomPosition = getRandomPosition()
        playerWidth = playerWidthModiFeed(playerWidth)
        playerSpeedX = playerSpeedModiFeed(playerSpeedX)
    #Con efectos negativos    
    if poison.colliderect(player):
        feedRandomPosition = getRandomPosition()
        poisonRandomPosition = getRandomPosition()
        playerWidth = playerWidthModiPoison(playerWidth)
        playerSpeedX = playerSpeedModiPoison(playerSpeedX)
        
    #---------------DrawZone-----------------------#    
    #Actualizacion de objetos en pantalla
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

