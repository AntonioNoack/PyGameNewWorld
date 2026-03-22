import pygame
from tileset import Tileset
import math

class Slime:
    def __init__(self, slime_pos):
        self.slime_pos = slime_pos
        self.tileset = Tileset("assets/tilemaps/slimes_green.png", (276 // 6,198 // 6))
        self.anim = 0

    def move(self, dt):
        self.anim += dt

    def draw(self, screen, x_offset, y_offset):
        tile = self.tileset.tiles[math.floor(self.anim * 10) % 6 * 6]
        screen.blit(tile, ((self.slime_pos.x-276//6/2)+x_offset, (self.slime_pos.y-198//6/2)+y_offset))