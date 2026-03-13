import pygame

class Player:
    def __init__(self, player_pos):
        self.speed = 500
        self.player_pos = player_pos

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