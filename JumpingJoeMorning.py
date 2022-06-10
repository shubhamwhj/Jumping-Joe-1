import pygame, sys, random
from Joe1Abstract import game

#initializing pygame
pygame.init()
clock=pygame.time.Clock()

#Screen setup
screen_width=700
screen_height=400
screen=pygame.display.set_mode((screen_width,screen_height))

#colors
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#Images
color_surf=pygame.image.load("assets/m.jpg").convert_alpha()
background_surf=pygame.image.load("assets/environment.png").convert_alpha()
ground_surf=pygame.image.load("assets/ground.png").convert_alpha()
background_surf.set_alpha(100)

door_open_surf=pygame.image.load("assets/doorOpen.png")
win_surf=pygame.image.load("assets/winscreen.png")
player_surf1=pygame.image.load("assets/joe1.PNG") 
cloud=pygame.image.load("assets/cloud.png")
cloud.set_alpha(200)
playerImgHeight=63
playerImgWidth=40
doorHeight=100
doorWidth=100
#Image Scaling
background_surf = pygame.transform.scale(background_surf, (screen_width, screen_height-100))
color_surf = pygame.transform.scale(color_surf, (screen_width, screen_height))
door_open_surf=pygame.transform.smoothscale(door_open_surf, (100,100))
cloud = pygame.transform.scale(cloud, (100, 50))
door_surf = door_open_surf
player_surf = pygame.transform.scale(player_surf1, (playerImgWidth, playerImgHeight))
ground_surf = pygame.transform.scale(ground_surf, (screen_width, 90))

#characters
player_rect=pygame.Rect(100,screen_height-145,40,63)  
ground_rect=pygame.Rect(0,screen_height-100,screen_width,40)
door_rect=pygame.Rect(screen_width-150,screen_height-180,doorWidth,doorHeight)

cloud1X = 50
cloud2X = 300
cloud3X = 550

#Game Loop
while True:
    screen.blit(color_surf, (0, 0))
    screen.blit(background_surf, (0, 100))
    screen.blit(ground_surf, (0, screen_height-90))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()


    cloud1X,cloud2X,cloud3X=game(player_rect,screen, playerImgHeight,playerImgWidth,door_rect,win_surf,pygame,player_surf,cloud,cloud1X,screen_width,cloud2X,cloud3X)
    #display characters
    #pygame.draw.rect(screen,RED, player)
    #pygame.draw.rect(screen,GREEN, door)
    
    

    screen.blit(door_surf,door_rect)
    screen.blit(player_surf,player_rect)
    
    pygame.display.flip()
    clock.tick(30)