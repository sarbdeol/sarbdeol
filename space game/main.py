import pygame
from pygame.constants import QUIT
import random
import math
from pygame import mixer
# initialize
pygame.init()

# create screen 
screen= pygame.display.set_mode((800,600))

# TITLE AND ICON
pygame.display.set_caption("space Invaders")
# Background img
Background=pygame.image.load('background.png')
#Background music
mixer.music.load('background.mp3')
mixer.music.play(-1)
#icon image
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# adding image of player
playerimg=pygame.image.load('playerimg.png')
playerX=370
playerY=480
playerX_change=0


# adding image of enemy
enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(40)


# adding image of bullet
# Ready = you can't see the bullet on screen
# Fire= the bullet is
bulletimg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="Ready"
#score

score_value=0
font=pygame.font.Font("freesansbold.ttf",32)

textX=10
testY=10
#Game over text
over_font=pygame.font.Font("freesansbold.ttf",64)
def show_score(x,y):
    score=font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over():
    
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
    
    
def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulletimg,(x + 20,y + 11))
def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    else:
        return False

#Game loop
running= True
while running:
    #RGB
    screen.fill((0,0,0))
    screen.blit(Background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if event.type == pygame.ANYFORMAT:
            print('start')

    # if keystroke is pressed check wheather the its right or left       
        if event.type==pygame.KEYDOWN: #key press
            if event.key==pygame.K_LEFT:     
                playerX_change=-5
            if event.key==pygame.K_RIGHT:     
                playerX_change=5  
            if event.key==pygame.K_SPACE:
                if bullet_state == 'Ready':
                    bullet_sound=mixer.Sound('laser.wav')
                    bullet_sound.play()
                    # get the current X coordinate of spaceship
                    bulletX=playerX
                    fire_bullet(playerX,bulletY)
        if event.type==pygame.KEYUP:   #key release
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0

    playerX+=playerX_change   
    #player movement
    if playerX <=0:
        playerX=0 
    elif playerX>=736:
        playerX=736  

       
    #enemy movement
    for i in range(num_of_enemies):
        #game over
        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over()
            break
        enemyX[i]+=enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i]=.8
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-.8
            enemyY[i]+=enemyY_change[i] 
        #collision
        collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision: 
            explosion_sound=mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY=480  
            bullet_state='Ready'
            score_value+=1
            
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)
    # bullet movement
    if bulletY <=0:
        bulletY=480
        bullet_state='Ready'
    if bullet_state == 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
    
    player(playerX,playerY)
    show_score(textX,testY)
    pygame.display.update()