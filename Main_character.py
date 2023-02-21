import pygame
class Charecter():
    player_skin = pygame.image.load("images/player.png")
    player_skin.set_colorkey((255, 255, 255))
    player_location = [30, 30]

    rect = pygame.Rect(player_location[0], player_location[1], player_skin.get_width(), player_skin.get_height())
    speed = 2

    # def Character_walk(self):
    #     self.rect.blit(self.star, (self.star_x-160, self.star_y))
    #     self.star_x += 40
    #     if self.star_x >= 160:
    #         self.star_x = 0