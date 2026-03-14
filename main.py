import pygame

from player import Player
from tileset import Tileset

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('New World')

game_is_running = True
clock = pygame.time.Clock()
dt = 0

# World
world_scale = 4
world_surface = pygame.Surface((screen.get_width() / world_scale, screen.get_height() / world_scale)) # 1/4th of display since we want to scale it later up by 4

world_tile_size = 16
world_tileset = Tileset("assets/tilemaps/overworld.png", (world_tile_size, world_tile_size))
print("world tileset:",world_tileset)

# Player
player_pos = pygame.Vector2(world_surface.get_width() / 2, world_surface.get_height() / 2)
player = Player(player_pos)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # ------------------
    # LOGIC
    # ------------------

    # Move Player
    player.move(dt)

    # ------------------
    # WORLD AND PLAYER GRAPHICS
    # ------------------

    # Fill Screen
    world_surface.fill("white")

    for i in range(int(world_surface.get_width()/world_tile_size+1)):
        for j in range(int(world_surface.get_height()/world_tile_size+1)):
            world_surface.blit(world_tileset.tiles[0], (world_tile_size*i,world_tile_size*j))
    
    # Display Player
    player.draw(world_surface)
    
    # Scale World Surface to Screen
    scaled_world_surface = pygame.transform.scale(world_surface, (screen.get_width(),screen.get_height()))
    screen.blit(scaled_world_surface, (0,0))

    # ------------------
    # UI
    # ------------------

    # Display Player Position (not scaled)
    font = pygame.freetype.Font("assets/fonts/OpenSans-Medium.ttf", 24)
    font_surface, _ = font.render(f"Player Position: ({player_pos.x:.0f}, {player_pos.y:.0f})", "black")
    screen.blit(font_surface, (10, 10))



    # Update the display with everything drawn
    pygame.display.flip()
    
    # delta time in seconds since last frame, used for framerate-independent physics
    dt = clock.tick(60) / 1000