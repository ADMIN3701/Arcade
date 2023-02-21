from tkinter import *
import pygame
pygame.init()

import Main_character
import Control
import Collision
import Map

root = Tk()
other_rect = pygame.Rect(230, 50, 60, 40)

######################## параметры окна #####################3
full_height = root.winfo_screenheight()
full_width = root.winfo_screenwidth()
window_size = (800, 520)
window = pygame.display.set_mode((window_size)) # для полного экранна используй pygame.FULLSCREEN
pygame.display.set_caption("Walking")
display = pygame.Surface((320, 192))

######## кол-во кадров/сек #######
clock = pygame.time.Clock()

############# обьекты ###################
World = Map.MAP()
Character = Main_character.Charecter()


################ Коллизия ##################
def colllision():
    collision_toleranse = 5
    if Character.rect.colliderect(other_rect):
        if abs(other_rect.top - Character.rect.bottom) < collision_toleranse:
            Control.DOWN = False
        if abs(other_rect.bottom - Character.rect.top) < collision_toleranse:
            Control.UP = False
        if abs(other_rect.right - Character.rect.left) < collision_toleranse:
            Control.LEFT = False
        if abs(other_rect.left - Character.rect.right) < collision_toleranse:
            Control.RIGHT = False
    else:
        Control.LEFT = True
        Control.RIGHT = True
        Control.UP = True
        Control.DOWN = True


################ события, функции и т.д. ##############
done = True
while done:
    #Character.rect, collisions = Collision.move(Character.rect, player_movement, tile_rects)

    surf = pygame.transform.scale(display, window_size)
    window.blit(surf, (0, 0))

    colllision()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
########### управление ###############################
    Control.keyboard()

############## отображение обьектов ###################
    display.fill((146,244,255))# закрашивание экрана
    World.World_map(Map.world_data, display)# карта
    #pygame.draw.rect(display, (255, 255, 255), Character.rect)# квадрат персонажа
    display.blit(Character.player_skin, (Character.player_location))# текстура персонажа
    pygame.draw.rect(display, (30, 30, 30), other_rect)# тестовый квадрат
    pygame.display.flip()# обновляет экран


#######################################################
    clock.tick(60)
pygame.quit()

