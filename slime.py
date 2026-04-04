import pygame
from tileset import Tileset
import math

class Slime:
    def __init__(self, slime_pos, player):
        self.speed = 120
        self.position = slime_pos
        self.tileset = Tileset("assets/tilemaps/slimes_green.png", (276 // 6,198 // 6))
        self.anim = 0
        self.orientation = "down"
        self.player = player
        self.distance_goal = 60
        self.orientation_offset = 0
        self.isFar = False
        self.distance_to_player = 1000

    def move(self, dt):
        self.anim += dt
        dx = self.position.x-self.player.position.x
        dy = self.position.y-self.player.position.y
        self.distance_to_player = math.sqrt(pow(dx,2)+pow(dy,2))
        near = 20
        isFar = self.isFar = self.distance_to_player > self.distance_goal
        if dy>0 and -near < dx < near:
            self.orientation = "up"
            if isFar:
                self.position.y -= self.speed * dt
        elif dy<0 and -near < dx < near:
            self.orientation = "down"
            if isFar:
                self.position.y += self.speed * dt
        elif dy<0 and dx>0:
            self.orientation = "leftdown"
            if isFar:
                self.position.y += self.speed * dt / 1.4
                self.position.x -= self.speed * dt / 1.4
        elif dy<0 and dx<0:
            self.orientation = "rightdown"
            if isFar:
                self.position.y += self.speed * dt / 1.4
                self.position.x += self.speed * dt / 1.4
        elif dy>0 and dx>0:
            self.orientation = "leftup"
            if isFar:
                self.position.y -= self.speed * dt / 1.4
                self.position.x -= self.speed * dt / 1.4
        elif dy>0 and dx<0:
            self.orientation = "rightup"
            if isFar:
                self.position.y -= self.speed * dt / 1.4
                self.position.x += self.speed * dt / 1.4

    def draw(self, screen, x_offset, y_offset):
        if self.orientation == "up":
            self.orientation_offset = 3
        elif self.orientation == "down":
            self.orientation_offset = 0
        elif self.orientation == "leftdown":
            self.orientation_offset = 1
        elif self.orientation == "rightdown":
            self.orientation_offset = 2
        elif self.orientation == "leftup":
            self.orientation_offset = 4
        elif self.orientation == "rightup":
            self.orientation_offset = 5
        
        tile = self.tileset.tiles[(math.floor(self.anim * 10) % 6 * 6)+self.orientation_offset]
        screen.blit(tile, ((self.position.x-276//6/2)+x_offset, (self.position.y-198//6/2)+y_offset))