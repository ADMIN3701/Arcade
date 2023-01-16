from tkinter import *
import pygame
pygame.init()
import Main_character
import Control

root = Tk()

full_height = root.winfo_screenheight()
full_width = root.winfo_screenwidth()

window = pygame.display.set_mode((full_width, full_height)) # для полного экранна используй pygame.FULLSCREEN
pygame.display.set_caption("AAAAAAAAAAAA")

######## кол-во кадров/сек #######
clock = pygame.time.Clock()
##################################

f1 = pygame.font.Font(None, 36)
text1 = f1.render(str(clock), True, (180, 0, 0))

tile_size = 200

def Lines_on_screen():
    for i in range(0, 250):
        pygame.draw.line(window, (255,255,255), (0, i * tile_size), (full_width, i * tile_size))
        pygame.draw.line(window, (255,255,255), (i * tile_size, 0), (i * tile_size, full_height))

world_data = [[1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1]
              ]


class MAP():
    # def __init__(self, world_map):
    #     self.tile_list = []
    #     dirt_img = pygame.image.load("Arcade.png")
    #
    #     col_count = 0
    #     for col in world_map:
    #         row_count = 0
    #         for row in col:
    #             if row == 1:
    #                 img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
    #                 img_rect = img.get_rect()
    #                 img_rect.x = col_count * tile_size
    #                 img_rect.y = row_count * tile_size
    #                 tile = (img, img_rect)
    #                 self.tile_list.append(tile)
    #             row_count += 1
    #         col_count += 1
    #
    # def Graw(self):
    #     for tile in self.tile_list:
    #         window.blit(tile[0], tile[1])

    def __init__(self, world_map):
        self.tile_list = []

        Image = pygame.image.load("wall.png")

        row_count = 0
        for row in world_map:
            col_count = 0
            for col in row:
                if col == 1:
                    Transforme_Image = pygame.transform.scale(Image, (tile_size, tile_size))
                    img_rect = Image.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (Image, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            window.blit(tile[0], tile[1])


World = MAP(world_data)

Character = Main_character.Charecter()

done = True
while done:

    World.draw()
    Character.Character_walk()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
########### управление ###########
    Control.keyboard()
##################################

    pos = pygame.mouse.get_pos()
    #window.fill((0, 0, 0))
    Lines_on_screen()
    window.blit(Character.rect, (Character.x, Character.y))
    window.blit(text1, (0, 0))
    #window.blit(MAP.Image, (50, 50))
    pygame.display.flip()

pygame.quit()