import pygame

class Camera:
    def __init__(self, camera_pos):
        self.speed = 120
        self.position = camera_pos
        self.following = True

    def move(self, dt):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            self.position.x += self.speed * dt / 1.4
            self.position.y += self.speed * dt / 1.4
            self.following = False
        
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            self.position.x -= self.speed * dt / 1.4
            self.position.y += self.speed * dt / 1.4
            self.following = False

        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            self.position.x += self.speed * dt / 1.4
            self.position.y -= self.speed * dt / 1.4
            self.following = False
        
        elif keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            self.position.x -= self.speed * dt / 1.4
            self.position.y -= self.speed * dt / 1.4
            self.following = False
        
        elif keys[pygame.K_UP]:
            self.position.y -= self.speed * dt
            self.following = False
        
        elif keys[pygame.K_DOWN]:
            self.position.y += self.speed * dt
            self.following = False
        
        elif keys[pygame.K_LEFT]:
            self.position.x -= self.speed * dt
            self.following = False
        
        elif keys[pygame.K_RIGHT]:
            self.position.x += self.speed * dt
            self.following = False

    def follow(self, player_pos):

        #toggle_key = pygame.event.get()

        if self.following:
            self.position.x = player_pos.x
            self.position.y = player_pos.y

    def toggle_follow(self):

        self.following = not self.following