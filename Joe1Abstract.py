# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 15:34:02 2022

@author: Shourabh Verma
"""
def game(player,screen, playerImgHeight,playerImgWidth,door,win_surf,pygame,player_surf,cloud,cloud1X,screen_width,cloud2X,cloud3X):
    if(player.colliderect(door)):
        screen.blit(win_surf,[220,100]) 
        playerImgHeight=int(playerImgHeight*0.99)
        playerImgWidth=int(playerImgWidth*0.99)
        player_surf=pygame.transform.scale(player_surf,(playerImgWidth,playerImgHeight) )
        player.x=door.centerx
        player.midbottom=door.midbottom
    
    screen.blit(cloud, (cloud1X, 50))
    if cloud1X < -100:
        cloud1X = screen_width
    else:
        cloud1X -= 2

    screen.blit(cloud, (cloud2X, 75))
    if cloud2X < -50:
        cloud2X = screen_width
    else:
        cloud2X -= 1

    screen.blit(cloud, (cloud3X, 100))
    if cloud3X < 0:
        cloud3X = screen_width
    else:
        cloud3X -= 2    
    
    return cloud1X,cloud2X,cloud3X