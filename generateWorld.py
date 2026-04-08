import pygame
from perlin_noise import PerlinNoise
from tileset import Tileset

same = True
other = False

class GenerateWorld:

    def __init__(self, seed):
        # perlin noise generator
        self.noise = PerlinNoise(octaves=3, seed=seed)

        # higher = smoother terrain, lower = more detail
        self.scale = 100
        self.cache = {}

        self.tilesets = {
            "DeepWater": Tileset("assets/tilemaps/groundTypes/DeepWater.png"),
            "NormalWater": Tileset("assets/tilemaps/groundTypes/NormalWater.png"),
            "LightGrass": Tileset("assets/tilemaps/groundTypes/LightGrass.png"),
            "DarkGrass": Tileset("assets/tilemaps/groundTypes/DarkGrass.png"),
            "RockyGround": Tileset("assets/tilemaps/groundTypes/RockyGround.png")
        }

        self.tilemaps = {
            ( other , other , same , other ): 0,
            ( same , other , other , same ): 1,
            ( other , same , other , other ): 2,
            ( other , other , other , other ): 3,
            ( other , same , other , same ): 4,
            ( other , same , same , same ): 5,
            ( same , same , other , other ): 6,
            ( other , other , other , same ): 7,
            ( same , other , same , same ): 8,
            ( same , same , same , same ): 9,
            ( same , same , other , same ): 10,
            ( other , same , same , other ): 11,
            ( other , other , same , same ): 12,
            ( same , same , same , other ): 13,
            ( same , other , same , other ): 14,
            ( same , other , other , other ): 15,
        }

        self.tile_hierarchy = { # the higher is on top
            "DeepWater": 0,
            "NormalWater": 1,
            "LightGrass": 10,
            "DarkGrass": 11,
            "RockyGround": 4
        }

    def get_noise_value(self, world_x, world_y):
        scaled_x = world_x / self.scale
        scaled_y = world_y / self.scale

        # Perlin noise output is ca. -1, 1
        value = self.noise([scaled_x, scaled_y])

        # normalized to 0, 1
        value = (value + 1) / 2
        value = value ** 1.5   # contrast boost

        return value

    def draw_terrain(self, screen, surface, tile_size, camera_pos):
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

                # debugging one tile only
                # if tile_x % 5 != 0:
                # if tile_x != 5 or tile_y != 9:
                #     continue

                # get tile position on screen
                screen_x = (tile_x * tile_size) - camera_pos.x
                screen_y = (tile_y * tile_size) - camera_pos.y

                # offset tile
                offset_tile_x = screen_x - tile_size / 2
                offset_tile_y = screen_y - tile_size / 2

                # get tiles
                top_tile, bottom_tile = self.getTilesAt(tile_x, tile_y)

                # draw tiles
                surface.blit(bottom_tile, (offset_tile_x, offset_tile_y))
                surface.blit(top_tile, (offset_tile_x, offset_tile_y))
                
    def getGroundTypeAt(self, tile_x, tile_y):

        key = (tile_x, tile_y)
        ground_type = self.cache.get(key)
        if ground_type is not None:
            return ground_type         

        # get value based on tile position
        value = self.get_noise_value(tile_x, tile_y)
        # black_white_value = int(value * 255)
        # color = (black_white_value, black_white_value, black_white_value)

        if value < 0.2:
            ground_type = "DeepWater"
        elif value < 0.3:
            ground_type = "NormalWater"
        elif value < 0.4:
            ground_type = "LightGrass"
        elif value < 0.5:
            ground_type = "DarkGrass"
        else:
            ground_type = "RockyGround"

        # # WATER
        # if value < 0.2:
        #     ground_type = ("#255786")     # deep water
        # elif value < 0.3:
        #    ground_type = ("#068fbc")     # normal water
        # # GRASS
        # elif value < 0.4:
        #     ground_type = ("#619861")    # normal grass
        # elif value < 0.5:
        #     ground_type = ("#44714d")    # dark grass
        # # MOUNTAIN
        # else:
        #     ground_type = ("#8a8276")    # rock grey

        self.cache[key] = ground_type

        return ground_type
    
    def getTilesAt(self, tile_x, tile_y):

        first_tyle_type = self.getGroundTypeAt(tile_x, tile_y)
        second_tile_type = "LightGrass"

        # 1 top-left
        t1 = same
        if self.getGroundTypeAt(tile_x, tile_y) != first_tyle_type:
            t1 = other
            second_tile_type = self.getGroundTypeAt(tile_x, tile_y)

        # 2 top-right
        t2 = same
        if self.getGroundTypeAt(tile_x + 1, tile_y) != first_tyle_type:
            t2 = other
            second_tile_type = self.getGroundTypeAt(tile_x + 1, tile_y)

        # 3 bottom-left
        t3 = same
        if self.getGroundTypeAt(tile_x, tile_y + 1) != first_tyle_type:
            t3 = other
            second_tile_type = self.getGroundTypeAt(tile_x, tile_y + 1)

        # 4 bottom-right
        t4 = same
        if self.getGroundTypeAt(tile_x + 1, tile_y + 1) != first_tyle_type:
            t4 = other
            second_tile_type = self.getGroundTypeAt(tile_x + 1, tile_y + 1)

        # |-----|-----|     1 at x,y
        # |  t1 |  t2 |     2 at x+1,y
        # |-----|-----|     3 at x,y+1
        # |  t3 |  t4 |     4 at x+1,y+1
        # |-----|-----|

        key_first = (t1, t2, t3, t4)
        first_tile_index = self.tilemaps.get(key_first)
        

        key_second = (not t1, not t2, not t3, not t4)

        second_tile_index =self.tilemaps.get(key_second)
    
        first_tile = self.tilesets[first_tyle_type].tiles[first_tile_index]
        second_tile = self.tilesets[second_tile_type].tiles[second_tile_index]


        if self.tile_hierarchy[first_tyle_type] > self.tile_hierarchy[second_tile_type]:
            return first_tile, second_tile
        else:
            return second_tile, first_tile