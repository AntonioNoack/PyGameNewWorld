import pygame
from perlin_noise import PerlinNoise

class GenerateWorld:

    def __init__(self, seed):
        # perlin noise generator
        self.noise = PerlinNoise(octaves=3, seed=seed)

        # higher = smoother terrain, lower = more detail
        self.scale = 100

    def get_noise_value(self, world_x, world_y):
        scaled_x = world_x / self.scale
        scaled_y = world_y / self.scale

        # Perlin noise output is ca. -1, 1
        value = self.noise([scaled_x, scaled_y])

        # normalized to 0, 1
        value = (value + 1) / 2
        value = value ** 1.5   # contrast boost

        return value

    def draw_terrain_map(self, screen, surface, tile_size, camera_pos):
        # how many tiles
        number_of_tiles_x = screen.get_width() // tile_size + 2
        number_of_tiles_y = screen.get_height() // tile_size + 2

        # get top left tiles based on camera position
        start_tile_x = camera_pos.x // tile_size
        start_tile_y = camera_pos.y // tile_size

        for y in range(number_of_tiles_y):
            for x in range(number_of_tiles_x):

                # position based on tiles
                tile_x = start_tile_x + x
                tile_y = start_tile_y + y

                # get value based on tile position
                value = self.get_noise_value(tile_x, tile_y)
                # black_white_value = int(value * 255)
                # color = (black_white_value, black_white_value, black_white_value)

                # WATER
                if value < 0.2:
                    color = ("#255786")     # deep water
                elif value < 0.3:
                    color = ("#068fbc")     # normal water
                # GRASS
                elif value < 0.4:
                    color = ("#619861")    # normal grass
                elif value < 0.5:
                    color = ("#44714d")    # dark grass
                # MOUNTAIN
                elif value < 0.6:
                    color = ("#9a8a74")  # rock grey
                else:
                    color = ("#6a635a")     # dark mountain

                # get tile position on screen
                screen_x = (tile_x * tile_size) - camera_pos.x
                screen_y = (tile_y * tile_size) - camera_pos.y

                # draw tile
                rect = pygame.Rect(
                    screen_x,
                    screen_y,
                    tile_size,
                    tile_size
                )
                pygame.draw.rect(surface, color, rect)