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

tile_size = 40

def Lines_on_screen():
    for i in range(0, 250):
        pygame.draw.line(window, (255,255,255), (0, i * tile_size), (full_width, i * tile_size))
        pygame.draw.line(window, (255,255,255), (i * tile_size, 0), (i * tile_size, full_height))

world_data = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
              [1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1]
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

        Background = pygame.image.load("images/background.png")
        window.blit(Background, (0, 0))

        Ground = pygame.image.load("images/wall.png")
        sky = pygame.image.load("images/sky.png")
        sky2 = pygame.image.load("images/sky2.png")
        sky3 = pygame.image.load("images/sky3.png")
        tree = pygame.image.load("images/tree.png")
        tree.set_colorkey((255, 255, 255))

        row_count = 0
        for row in world_map:
            col_count = 0
            for col in row:
                if col == 1:

                    Transforme_Image = pygame.transform.scale(Ground, (tile_size, tile_size))
                    img_rect = Ground.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (Ground, img_rect)
                    self.tile_list.append(tile)

                if col == 2:
                    Transforme_Image = pygame.transform.scale(sky, (tile_size, tile_size))
                    img_rect = sky.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (sky, img_rect)
                    self.tile_list.append(tile)

                if col == 3:
                    Transforme_Image = pygame.transform.scale(sky2, (tile_size, tile_size))
                    img_rect = sky2.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (sky2, img_rect)
                    self.tile_list.append(tile)

                if col == 4:
                    Transforme_Image = pygame.transform.scale(sky3, (tile_size, tile_size))
                    img_rect = sky3.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (sky3, img_rect)
                    self.tile_list.append(tile)

                if col == 5:
                    Transforme_Image = pygame.transform.scale(tree, (tile_size, tile_size))
                    img_rect = tree.get_rect()
                    img_rect.x = col_count * tile_size - 100
                    img_rect.y = row_count * tile_size - 180
                    tile = (tree, img_rect)
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
    #Character.Character_walk()
    window.blit(Character.rect, (Character.x, Character.y))

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

