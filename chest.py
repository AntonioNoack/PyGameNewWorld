import pygame
import random
from tileset import Tileset
import math

class Chest:
    def __init__(self, chest_pos, player):
        self.mimicProbability = 0.5
        self.position = chest_pos
        self.tileset = Tileset("assets/tilemaps/Mimic Sprite Sheet2.png", (256 // 8,352 // 11))
        #tileset from https://elthen.itch.io/2d-pixel-art-mimic-sprites
        #and combined a bit with https://retroviralgames.itch.io/gold-piles-variable-size but changed some things
        self.anim = 0
        self.player = player
        self.open = False
        self.mimic = self.mimicProbability < random.random()
        self.distanceToPlayer = 1000
        
    def draw(self, screen, x_offset, y_offset):
        if self.mimic and self.open:
            tile = self.tileset.tiles[math.floor(self.anim * 10) % 2 + 33]
        if not self.open:
            tile = self.tileset.tiles[0]
        if not self.mimic and self.open:
            tile = self.tileset.tiles[44]
        screen.blit(tile, ((self.position.x-256//8/2)+x_offset, (self.position.y-352//11/2)+y_offset))

    def interact(self):
        if self.distanceToPlayer < 40:
            self.open = not self.open
    
    def move(self, dt):
        self.anim += dt
        self.distanceToPlayer = math.sqrt(math.pow(self.position.x-self.player.position.x,2)+math.pow(self.position.y-self.player.position.y,2))