import pygame
import math
import random
from pygame import mixer

pygame.init()

# Create The Screen
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load('Background.jpg')

#background sound
mixer.music.load('background.wav')
mixer.music.play(-1)
explosion_sound = mixer.Sound('explosion.wav')


#title and Icon
pygame.display.set_caption("Space Cucks")
icon=pygame.image.load('player.png')
pygame.display.set_icon(icon)

#Player
playerX = 375
playerY = 480
playerX_change = 0

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5
enemy_switch=0
enemy_change = True
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(5, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.2)
    enemyY_change.append(40)

#sound fx
victory_fx = pygame.mixer.Sound('victory.wav')

#bouncy enemy
bounceImg = []
bounceX = []
bounceY = []
bounceX_change = []
bounceY_change = []
num_of_bounce = 2
for i in range(num_of_bounce):
    bounceImg.append(pygame.image.load('ufo.png'))
    bounceX.append(random.randint(5, 735))
    bounceY.append(random.randint(50, 150))
    bounceX_change.append(0.2)
    bounceY_change.append(0.2)

#Boss
bossX = -100
bossY = -100
bossX_change = 0.3
bossY_change = 0.3
boss_health = 25
boss_change = False

#bullet
bulletX = 0
bulletY = 450
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"
bullet_sound = mixer.Sound('laser.wav')

#laser
laserX = 0
laserY = 0
laserX_change = 0
laserY_change = 0.4
laser_state = "ready"
laser_sound = mixer.Sound('enemy_laser.wav')

#Vortex
vortexX = 0
vortexY = 0
vortexX_change = 0
vortexY_change = 0.2
vortex_state = "ready"
vortex_sound = mixer.Sound('enemy_laser.wav')

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#Timer
timerY = 550
timerX = 0
timerY_Change = 0.3

#Images
bossImg = pygame.image.load('boss.png')
playerImg = pygame.image.load('Playa.png')
vortexImg = pygame.image.load('vortex.png')
bulletImg = pygame.image.load('laser.png')
laserImg = pygame.image.load('lasere.png')


#Game Over Text
over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render("score :" + str(score_value),True, (255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER",True, (255,255,255))
    screen.blit(over_text,(200,250))

def game_win_text():
    over_text = over_font.render("Congratulation!",True, (255,255,255))
    screen.blit(over_text,(200,250))

def player(x,y):
    screen.blit(playerImg,(x,y))

def timer(x,y):
    screen.blit(playerImg,(x,y+100))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def bounce(x,y,i):
    screen.blit(bounceImg[i],(x,y))

def boss(x,y):
    screen.blit(bossImg,(x-95,y-80))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def fire_laser(x,y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserImg, (x, y))

def fire_vortex(x,y):
    global vortex_state
    vortex_state = "fire"
    screen.blit(vortexImg, (x-30, y-30))

def isCollisionE (enemyX,enemyY,bulletX,bulletY):
    distanceE = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))
    if distanceE < 27:
        return True
    else:
        return False

def isCollisionL (playerX,playerY,laserX,laserY):
    distanceL = math.sqrt(math.pow(playerX-laserX,2) + math.pow(playerY-laserY,2))
    if distanceL < 27:
        return True
    else:
        return False

def isCollisionB (bossX,bossY,bulletX,bulletY):
    distanceB = math.sqrt(math.pow(bossX-bulletX,2) + math.pow(bossY-bulletY,2))
    if distanceB < 80:
        return True
    else:
        return False

def isCollisionVortex (playerX,playerY,vortexX,vortexY):
    distanceV = math.sqrt(math.pow(playerX-vortexX,2) + math.pow(playerY-vortexY,2))
    if distanceV < 65:
        return True
    else:
        return False

def isCollisionBounce (bounceX,bounceY,bulletX,bulletY):
    distancebounce = math.sqrt(math.pow(bounceX-bulletX,2) + math.pow(bounceY-bulletY,2))
    if distancebounce < 27:
        return True
    else:
        return False

def isCollisionbounce2 (playerX,playerY,bounceX,bounceY):
    distancebounce2 = math.sqrt(math.pow(playerX-bounceX,2) + math.pow(playerY-bounceY,2))
    if distancebounce2 < 27:
        return True
    else:
        return False

#Game Loop
running = True
while running:

    screen.fill((0,0,35))
    #Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound.play()
                    bulletX = playerX
                    bulletY = 480
                    fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #enemy fire
    if laser_state is "ready":
        laser_sound.play()
        laserX = enemyX[enemy_switch]
        laserY = enemyY[enemy_switch] +33
        fire_laser(enemyX[enemy_switch], laserY)

    #boss vortex
    if boss_change is True:
        if vortex_state is "ready":
            vortex_sound.play()
            vortexX = bossX
            vortexY = bossY
            fire_vortex(bossX, bossY)

    #checking for boundaries of space ship
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Enemy Movement
    for i in range(num_of_enemies):
        #Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = 0.2
        elif enemyX[i] >= 736:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = -0.2
        enemy(enemyX[i], enemyY[i], i)
        #Collision
        collisionE = isCollisionE(enemyX[i],enemyY[i],bulletX,bulletY)
        if collisionE:
            explosion_sound.play()
            bulletY = 700
            bullet_state = "ready"
            score_value += 1
            print (score_value)
            enemyX[i] = random.randint(5, 735)
            enemyY[i] = random.randint(50, 150)

    #Bounce movement
    for i in range(num_of_bounce):
        bounceX[i] += bounceX_change[i]
        bounceY[i] += bounceY_change[i]
        if bounceX[i] <= 0:
            bounceX[i] += bounceX_change[i]
            bounceX_change[i] = 0.2
        elif bounceX[i] >= 736:
            bounceX[i] += bounceX_change[i]
            bounceX_change[i] = -0.2
        if bounceY[i] <= 0:
            bounceY[i] += bounceY_change[i]
            bounceY_change[i] = 0.2
        elif bounceY[i] >= 550:
            bounceY[i] += bounceY_change[i]
            bounceY_change[i] = -0.2
        bounce(bounceX[i], bounceY[i], i)
        #Collision
        collisionbounce = isCollisionBounce(bounceX[i],bounceY[i],bulletX,bulletY)
        if collisionbounce:
            explosion_sound.play()
            bulletY = 700
            bullet_state = "ready"
            score_value += 1
            print (score_value)
            bounceX[i] = random.randint(5, 735)
            bounceY[i] = random.randint(50, 150)
        collisionbounce2 = isCollisionbounce2(playerX,playerY,bounceX[i],bounceY[i])
        if collisionbounce2:
            explosion_sound.play()
            game_over_text()
            bounceX_change = 0
            bounceY_change = 0
            laserY_change = 0
            playerX_change = 0
            break
    #collision
    collisionV = isCollisionVortex(playerX,playerY,vortexX,vortexY)
    if collisionV:
        explosion_sound.play()
        game_over_text()
        vortexY_change = 0
        playerX_change = 0
        break

    collisionL = isCollisionL(playerX,playerY,laserX,laserY)
    if collisionL:
        explosion_sound.play()
        game_over_text()
        laserY_change = 0
        playerX_change = 0
        break

    collisionB = isCollisionB(bossX,bossY,bulletX,bulletY)
    if collisionB:
        explosion_sound.play()
        bulletY = 700
        bullet_state = "ready"
        score_value += 1
        print (score_value)
        boss_health -= 1

    #Bullet Movement
    if bulletY <=0:
        bulletY = 700
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    #laser Movement
    if laser_state is "fire":
        fire_laser(laserX,laserY)
        laserY += laserY_change
    if laserY >=600:
        laser_state = "ready"
        laserY = 0
        if enemy_change is True:
            enemy_switch = enemy_switch + 1
            if enemy_switch == 5:
                enemy_switch = 0
    #vortex movement
    if vortex_state is "fire":
        fire_vortex(vortexX,vortexY)
        vortexY += vortexY_change
    if vortexY >=600:
        vortex_state = "ready"
        vortexY = 0
    #Getting rid of enemys
    if score_value >= 40:
        boss_change = True
        num_of_bounce = 1
        enemy_change = False
        enemy_switch = 0
        num_of_enemies = 2
        boss(bossX,bossY) 
        bossX += bossX_change
        bossY += bossY_change
    #Boss defeat
    if boss_health == 0:
        bossX_change = 0
        bossY_change = 0
        bossImg = pygame.image.load('explosion.png')
        vortex_state = "stop"
        timerY += timerY_Change
        pygame.mixer.music.stop()
        victory_fx.play()
        boss_health = -1
    if boss_health == -1:
        num_of_bounce = 0
        num_of_enemies = 0
        laserY_change = 0
        game_win_text()
    if bossY <= 1:
        bossY_change = 0.2
    if bossY >= 150:
        bossY_change = -0.2
    if bossX <= -60:
        bossX_change = 0.2
    if bossX >= 625:
        bossX_change = -0.2
    player(playerX, playerY)
    timer(timerX,timerY)
    show_score(textX,textY)
    pygame.display.update()
pygame.quit()