import pygame

class Tileset:
    def __init__(self, file, single_tile_size=(16,16)):
        self.file = file
        self.single_tile_size = single_tile_size
        self.image = pygame.image.load(file)
        self.image_rectangle = self.image.get_rect()
        self.tiles = []
        self.load()

    def load(self):
        self.tiles = []
        width, height = self.image_rectangle.size
        xStepWidth = self.single_tile_size[0]
        yStepWidth = self.single_tile_size[1]

        for x in range(0,width,xStepWidth):
            for y in range(0, height,yStepWidth):
                tile = pygame.Surface(self.single_tile_size, pygame.SRCALPHA)
                # tile = tile.convert_alpha()
                tile.blit(self.image, (0,0), (x,y,self.single_tile_size[0],self.single_tile_size[1]))
                self.tiles.append(tile)

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile size:{self.single_tile_size}'