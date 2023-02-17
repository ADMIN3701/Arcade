import pygame
class Charecter():
    star = pygame.image.load("images/star_sprite.png")
    star.set_colorkey((255, 255, 255))
    star_x = 0
    star_y = 0

    rect = pygame.Rect(200, 200, 40, 40)
    #rect.fill((255, 255, 255))
    #rect.set_colorkey((255, 255, 255))
    speed = 5

    def Character_walk(self):
        self.rect.blit(self.star, (self.star_x-160, self.star_y))
        self.star_x += 40
        if self.star_x >= 160:
            self.star_x = 0