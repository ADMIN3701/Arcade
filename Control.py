import Main_character
import pygame
from tkinter import *

root = Tk()

full_height = root.winfo_screenheight()
full_width = root.winfo_screenwidth()

Character = Main_character.Charecter()
Rect = Character.rect

LEFT = True
RIGHT = True
UP = True
DOWN = True

def keyboard():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and Rect.x >= 0 and LEFT:
        # Rect.x -= Character.speed
        Character.player_location[0] -= Character.speed
    if keys[pygame.K_d] and Rect.x <= 320 - 12 and RIGHT:
        # Rect.x += Character.speed
        Character.player_location[0] += Character.speed
    if keys[pygame.K_w] and Rect.y >= 0 and UP:
        # Rect.y -= Character.speed
        Character.player_location[1] -= Character.speed
    if keys[pygame.K_s] and Rect.y <= 192 - 12 and DOWN:
        # Rect.y += Character.speed
        Character.player_location[1] += Character.speed

    if keys[pygame.K_ESCAPE]:
        pygame.QUIT()

    Character.rect.x = Character.player_location[0]
    Character.rect.y = Character.player_location[1]