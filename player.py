import pygame
from tileset import Tileset

class Player:
    def __init__(self, player_pos):
        self.speed = 120
        self.player_pos = player_pos
        self.tileset = Tileset("assets/tilemaps/character_walking.png", (16,32))

    def move(self, dt):
        
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_d] and keys[pygame.K_s]:
            self.player_pos.x += self.speed * dt / 1.4
            self.player_pos.y += self.speed * dt / 1.4
        
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            self.player_pos.x -= self.speed * dt / 1.4
            self.player_pos.y += self.speed * dt / 1.4

        elif keys[pygame.K_d] and keys[pygame.K_w]:
            self.player_pos.x += self.speed * dt / 1.4
            self.player_pos.y -= self.speed * dt / 1.4
        
        elif keys[pygame.K_a] and keys[pygame.K_w]:
            self.player_pos.x -= self.speed * dt / 1.4
            self.player_pos.y -= self.speed * dt / 1.4
        
        elif keys[pygame.K_w]:
            self.player_pos.y -= self.speed * dt
        
        elif keys[pygame.K_s]:
            self.player_pos.y += self.speed * dt
        
        elif keys[pygame.K_a]:
            self.player_pos.x -= self.speed * dt
        
        elif keys[pygame.K_d]:
            self.player_pos.x += self.speed * dt

    def draw(self, screen):
        #pygame.draw.circle(screen, "black", self.player_pos, 40)

        screen.blit(self.tileset.tiles[0], (self.player_pos.x-16/2, self.player_pos.y-32/2))