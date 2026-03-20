import pygame
from tileset import Tileset

class Player:
    def __init__(self, player_pos):
        self.speed = 120
        self.player_pos = player_pos
        self.tileset = Tileset("assets/tilemaps/character_walking.png", (16,32))
        self.orientation = "down"

    def move(self, dt):
        
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

    def draw(self, screen, x_offset, y_offset):
        #pygame.draw.circle(screen, "black", self.player_pos, 40)
        
        if self.orientation == "left":
            tile = self.tileset.tiles[3]
        elif self.orientation == "right":
            tile = self.tileset.tiles[1]
        elif self.orientation == "up":
            tile = self.tileset.tiles[2]
        elif self.orientation == "down":
            tile = self.tileset.tiles[0]

        screen.blit(tile, ((self.player_pos.x-16/2)+x_offset, (self.player_pos.y-32/2)+y_offset))