import Main_character
import pygame
from tkinter import *

root = Tk()

full_height = root.winfo_screenheight()
full_width = root.winfo_screenwidth()

Character = Main_character.Charecter()

def keyboard():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and Main_character.Charecter.x >= 0:
        Main_character.Charecter.x -= Main_character.Charecter.speed
    if keys[pygame.K_d] and Main_character.Charecter.x <= full_width - 40:
        Main_character.Charecter.x += Main_character.Charecter.speed
    if keys[pygame.K_w] and Main_character.Charecter.y >= 0:
        Main_character.Charecter.y -= Main_character.Charecter.speed
    if keys[pygame.K_s] and Main_character.Charecter.y <= full_height - 40:
        Main_character.Charecter.y += Main_character.Charecter.speed

    if keys[pygame.K_ESCAPE]:
        pygame.QUIT()