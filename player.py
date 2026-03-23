import pygame
from tileset import Tileset
import math

class Player:
    def __init__(self, player_pos):
        self.speed = 120
        self.player_pos = player_pos
        self.tileset = Tileset("assets/tilemaps/character_walking.png", (16,32))
        self.orientation = "down"
        self.anim = 0

    def move(self, dt):
        self.anim += dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and keys[pygame.K_s]:
            self.player_pos.x += self.speed * dt / 1.4
            self.player_pos.y += self.speed * dt / 1.4
            self.orientation = "down"
        
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            self.player_pos.x -= self.speed * dt / 1.4
            self.player_pos.y += self.speed * dt / 1.4
            self.orientation = "down"

        elif keys[pygame.K_d] and keys[pygame.K_w]:
            self.player_pos.x += self.speed * dt / 1.4
            self.player_pos.y -= self.speed * dt / 1.4
            self.orientation = "up"
        
        elif keys[pygame.K_a] and keys[pygame.K_w]:
            self.player_pos.x -= self.speed * dt / 1.4
            self.player_pos.y -= self.speed * dt / 1.4
            self.orientation = "up"
        
        elif keys[pygame.K_w]:
            self.player_pos.y -= self.speed * dt
            self.orientation = "up"
        
        elif keys[pygame.K_s]:
            self.player_pos.y += self.speed * dt
            self.orientation = "down"
        
        elif keys[pygame.K_a]:
            self.player_pos.x -= self.speed * dt
            self.orientation = "left"
        
        elif keys[pygame.K_d]:
            self.player_pos.x += self.speed * dt
            self.orientation = "right"

        else:
            self.anim = 0

    def draw(self, screen, x_offset, y_offset):
        #pygame.draw.circle(screen, "black", self.player_pos, 40)

        if self.orientation == "left":
            tile = 3
        elif self.orientation == "right":
            tile = 1
        elif self.orientation == "up":
            tile = 2
        elif self.orientation == "down":
            tile = 0

        tile += (math.floor(self.anim*10) % 4 * 4)

        screen.blit(self.tileset.tiles[tile], ((self.player_pos.x-16/2)+x_offset, (self.player_pos.y-32/2)+y_offset))