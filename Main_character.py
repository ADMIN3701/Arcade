import time
import pygame
class Charecter():
    star = pygame.image.load("star_sprite.png")
    star_x = 0
    star_y = 0
    curentframe = 0

    rect = pygame.Surface((40, 40))
    rect.fill((0, 255, 255))
    speed = 0.5
    x = 200
    y = 200

    def Character_walk(self):
        self.curentframe += 0000.1
        if self.curentframe == 10:
             self.curentframe == 0
        self.rect.blit(self.star, (self.star_x - self.curentframe, self.star_y))