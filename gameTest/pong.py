import pygame
pygame.init()

# Definiciones de colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

size = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
gameExit = False
paused = False
playerWidth = 15
playerHeigth = 90

#Coordenadas y speed player1
player1CoordX = 50
player1CoordY = 300-45
player1SpeedY = 0

#Coordenadas y speed player2
player2CoordX = 750
player2CoordY = 300-45
player2SpeedY = 0

#Coordenadas y speed de pelota
pelotaX = 400
pelotaY = 300
pelotaSpeedX = 5
pelotaSpeedY = 5

#Manejo de eventos
while not gameExit:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            gameExit = True
    
        #Player 1    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1SpeedY = -7
            if event.key == pygame.K_s:
                player1SpeedY = 7
        #Player 2
            if event.key == pygame.K_UP:
                player2SpeedY = -7
            if event.key == pygame.K_DOWN:
                player2SpeedY = 7 
        #Player 1         
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1SpeedY = 0
            if event.key == pygame.K_s:
                player1SpeedY = 0
        #Player 2
            if event.key == pygame.K_UP:
                player2SpeedY = 0
            if event.key == pygame.K_DOWN:
                player2SpeedY = 0 
        #Pausa
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  
                paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                paused = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Se presiona la tecla "P" de nuevo
                    paused = False

    #Logica
        # Para el player1
    if player1CoordY < 0:
        player1CoordY = 0
    if player1CoordY > size[1] - playerHeigth:
        player1CoordY = size[1] - playerHeigth

    # Para el player2
    if player2CoordY < 0:
        player2CoordY = 0
    if player2CoordY > size[1] - playerHeigth:
        player2CoordY = size[1] - playerHeigth


    if pelotaY > 590 or pelotaY < 10:
        pelotaSpeedY *= -1

    if pelotaX > 800 or pelotaX <0:
        pelotaX = 400
        pelotaY = 300
        pelotaSpeedX *= -1
        pelotaSpeedY *= -1

    #Movimiento players/pelota
    player1CoordY += player1SpeedY
    player2CoordY += player2SpeedY
    pelotaX += pelotaSpeedX
    pelotaY += pelotaSpeedY
     
    screen.fill(NEGRO)

    player1 = pygame.draw.rect(screen, BLANCO,(player1CoordX,player1CoordY, playerWidth, playerHeigth))
    player2 = pygame.draw.rect(screen, BLANCO,(player2CoordX,player2CoordY, playerWidth, playerHeigth))
    pelota = pygame.draw.circle(screen, BLANCO,(pelotaX,pelotaY), 10)

    #Colisiones
    if pelota.colliderect(player1) or pelota.colliderect(player2):
        pelotaSpeedX *= -1


    pygame.display.flip()
    clock.tick(60)
pygame.quit()