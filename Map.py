import pygame
from tkinter import *
# root = Tk()
#
# full_height = root.winfo_screenheight()
# full_width = root.winfo_screenwidth()
#
# window = pygame.display.set_mode((800, 520))

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
    def World_map(self, world_map, display):
        Ground = pygame.image.load("images/wall.png")
        sky = pygame.image.load("images/sky.png")
        sky2 = pygame.image.load("images/sky2.png")
        sky3 = pygame.image.load("images/sky3.png")
        tree = pygame.image.load("images/tree.png")
        tree.set_colorkey((255, 255, 255))

        TILE_SIZE = 40
        tile_rects = []
        y = 0
        for row in world_map:
            x = 0
            for tile in row:
                if tile == 1:
                    display.blit(Ground, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == 2:
                    display.blit(sky, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == 3:
                    display.blit(sky2, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == 4:
                    display.blit(sky3, (x * TILE_SIZE, y * TILE_SIZE))
                # if tile == 5:
                #     Transforme_Image = pygame.transform.scale(tree, (TILE_SIZE, TILE_SIZE))
                #     display.blit(Transforme_Image, (x * TILE_SIZE, y * TILE_SIZE))
                if tile != 0:
                    tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                x += 1
            y += 1

    #self.tile_list = []
    #     row_count = 0
    #     for row in world_map:
    #         col_count = 0
    #         for col in row:
    #             if col == 1:
    #
    #                 Transforme_Image = pygame.transform.scale(Ground, (tile_size, tile_size))
    #                 img_rect = Ground.get_rect()
    #                 img_rect.x = col_count * tile_size
    #                 img_rect.y = row_count * tile_size
    #                 tile = (Ground, img_rect)
    #                 self.tile_list.append(tile)
    #
    #             if col == 2:
    #                 Transforme_Image = pygame.transform.scale(sky, (tile_size, tile_size))
    #                 img_rect = sky.get_rect()
    #                 img_rect.x = col_count * tile_size
    #                 img_rect.y = row_count * tile_size
    #                 tile = (sky, img_rect)
    #                 self.tile_list.append(tile)
    #
    #             if col == 3:
    #                 Transforme_Image = pygame.transform.scale(sky2, (tile_size, tile_size))
    #                 img_rect = sky2.get_rect()
    #                 img_rect.x = col_count * tile_size
    #                 img_rect.y = row_count * tile_size
    #                 tile = (sky2, img_rect)
    #                 self.tile_list.append(tile)
    #
    #             if col == 4:
    #                 Transforme_Image = pygame.transform.scale(sky3, (tile_size, tile_size))
    #                 img_rect = sky3.get_rect()
    #                 img_rect.x = col_count * tile_size
    #                 img_rect.y = row_count * tile_size
    #                 tile = (sky3, img_rect)
    #                 self.tile_list.append(tile)
    #
    #             if col == 5:
    #                 Transforme_Image = pygame.transform.scale(tree, (tile_size, tile_size))
    #                 img_rect = tree.get_rect()
    #                 img_rect.x = col_count * tile_size - 100
    #                 img_rect.y = row_count * tile_size - 180
    #                 tile = (tree, img_rect)
    #                 self.tile_list.append(tile)
    #
    #             col_count += 1
    #         row_count += 1
    # def draw(self, window):
    #     for tile in self.tile_list:
    #         window.blit(tile[0], tile[1])

    # def Lines_on_screen(self, window):
    #     for i in range(0, 250):
    #         pygame.draw.line(window, (255, 255, 255), (0, i * tile_size), (full_width, i * tile_size))
    #         pygame.draw.line(window, (255, 255, 255), (i * tile_size, 0), (i * tile_size, full_height))