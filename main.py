import pygame, sys, random
pygame.init
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)

imagesizex = 146
imagesizey = 64
img1 = pygame.image.load("variables/1.png")
img2 = pygame.image.load("variables/2.png")
img3 = pygame.image.load("variables/3.png")
img4 = pygame.image.load("variables/4.png")
img5 = pygame.image.load("variables/5.png")
img6 = pygame.image.load("variables/6.png")
img7 = pygame.image.load("variables/7.png")
DVDIMG = random.randint(1, 7)
DVDX = 427-imagesizex
DVDY = 240-imagesizey
DVDX_velocity = 0.15
DVDY_velocity = 0.15


def call_dvd(image, x, y,):
    screen.blit(image, (x, y))

running = True
while running:
    DVDX += DVDX_velocity
    DVDY += DVDY_velocity
    
    if DVDIMG == 1:
        DVDIMG = img1
    if DVDIMG == 2:
        DVDIMG = img2
    if DVDIMG == 3:
        DVDIMG = img3
    if DVDIMG == 4:
        DVDIMG = img4
    if DVDIMG == 5:
        DVDIMG = img5
    if DVDIMG == 6:
        DVDIMG = img6
    if DVDIMG == 7:
        DVDIMG = img7
    
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        running = False
    
    call_dvd(DVDIMG, DVDX, DVDY)
    
    if DVDX >= 1280-146:
        DVDX = 1280-146
        DVDX_velocity *= -1
        DVDIMG = random.randint(1, 7)
    
    if DVDX <= 0:
        DVDX = 0
        DVDX_velocity *= -1
        DVDIMG = random.randint(1, 7)
        
    if DVDY <= 0:
        DVDY = 0
        DVDY_velocity *= -1
        DVDIMG = random.randint(1, 7)
    
    if DVDY >= 720-64:
        DVDY = 720-64
        DVDY_velocity *= -1
        DVDIMG = random.randint(1, 7)
    
    pygame.display.update()