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
        Rect.x -= Character.speed
    if keys[pygame.K_d] and Rect.x <= 800 - 40 and RIGHT:
        Rect.x += Character.speed
    if keys[pygame.K_w] and Rect.y >= 0 and UP:
        Rect.y -= Character.speed
    if keys[pygame.K_s] and Rect.y <= 520 - 40 and DOWN:
        Rect.y += Character.speed

    if keys[pygame.K_ESCAPE]:
        pygame.QUIT()