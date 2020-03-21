import pygame
import random
import math

#initialize pygame
pygame.init()

#create game window
screen = pygame.display.set_mode((800,600))     
pygame.display.set_caption('Python Invaders')       
icon = pygame.image.load('Python-invaders.png')     
running = True

#Window Icon
pygame.display.set_icon(icon)

#Player
playerimg = pygame.image.load('Player.png')   
playerx = 350.0
playery = 500.0
playerx_change = 0
playery_change = 0

#Enemy
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
enemies = 30

for i in range(enemies):
    enemyimg.append(pygame.image.load('Enemy.png'))
    enemyx.append(random.randint(0,736))
    enemyy.append(random.randint(50,150))
    enemyx_change.append(5)
    enemyy_change.append(40)

#Bullet
fire = False
bulletimg = pygame.image.load('Bullet.png')
bullety = playery
bullety_change = -20
bulletx = 0

#Score Display
scoretext = 0
font = pygame.font.Font('freesansbold.ttf',32)
textx = 630
texty = 20

def Player(x,y):
    screen.blit(playerimg, (x,y))

def Enemy(x,y):
    screen.blit(enemyimg[i], (x,y))

def Bullet(x,y):
    screen.blit(bulletimg, (x,y))

def ShowScore(x,y):
    score = font.render("Score: " + str(scoretext),True,(255,255,255))
    screen.blit(score, (x,y))

def Collision_Detection(BX,BY,EX,EY):
    Dist = math.sqrt(math.pow(EX - BX,2) + (math.pow(EY - BY,2)))
    if Dist < 50:
        return True



#Event Loop
while running :

    #Background
    Background = pygame.image.load('Background.png')
    screen.blit(Background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Controls
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_UP:
                playery_change = -5
            if event.key == pygame.K_DOWN:
                playery_change = 5
            if event.key == pygame.K_SPACE:
                fire = True
                bulletx = playerx
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:   
                playerx_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:   
                playery_change = 0

    #Player Movement
    playerx += playerx_change
    playery += playery_change

    #Enemy Movement
    for i in range(enemies):
        enemyx[i] += enemyx_change[i]
        if enemyy[i] >= 536:
            GameOver = pygame.image.load('Game_Over.png')
            screen.blit(Background,(0,0))
            screen.blit(GameOver,(250,150))


    #Bullet Movement
    if fire:
        Bullet(bulletx,bullety)
        bullety += bullety_change
    if bullety <= 0: 
        fire = False
        bullety = playery
        

    #Player Boundaries Reset
    if playerx <=0:
        playerx = 0
    elif playerx >=736:
        playerx = 736
    if playery <= 0:
        playery = 0
    if playery >= 536:
        playery = 536

    #Enemy Boundaries Reset
    for i in range(enemies):
        if enemyx[i] <=0:
            enemyx_change[i] = 5
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >=736:
            enemyx_change[i] = -5
            enemyy[i] += enemyy_change[i]


    #Spawning
    Player(playerx,playery)
    ShowScore(textx,texty)
    for i in range(enemies):
        Enemy(enemyx[i],enemyy[i])

    #Collision Detection
    for i in range(enemies):
        col = Collision_Detection(bulletx,bullety,enemyx[i],enemyy[i])
        if col:
           fire = False
           bullety = playery
           scoretext += 1
           enemyx[i] = random.randint(0,736)
           enemyy[i] = random.randint(50,150)
        

    #Screen Refreshing
    pygame.display.update()