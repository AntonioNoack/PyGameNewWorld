import pygame
from player import Player
from slime import Slime
from camera import Camera
from tileset import Tileset
from chest import Chest
from generateWorld import GenerateWorld

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('New World')
clock = pygame.time.Clock()
dt = 0

# World
seed = 42
world_scale = 4
world_surface = pygame.Surface((screen.get_width() / world_scale, screen.get_height() / world_scale)) # 1/4th of display since we want to scale it later up by 4

world_tile_size = 16
world_tileset = Tileset("assets/tilemaps/overworld.png", (world_tile_size, world_tile_size))
print("world tileset:",world_tileset)

generated_world = GenerateWorld(seed)

# Player
player_pos = pygame.Vector2(world_surface.get_width() / 2, world_surface.get_height() / 2)
player = Player(player_pos)

# Slime
slime_pos = pygame.Vector2(world_surface.get_width() / 2, world_surface.get_height() / 2 + 50)
slime = Slime(slime_pos, player)

# Chest
chest_pos = pygame.Vector2(world_surface.get_width() / 2 + 60, world_surface.get_height() / 2 - 50)
chest = Chest(chest_pos, player)

# Camera
camera_pos = pygame.Vector2(world_surface.get_width() / 2, world_surface.get_height() / 2)
camera = Camera(camera_pos)

# UI
font = pygame.freetype.Font("assets/fonts/OpenSans-Medium.ttf", 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            camera.toggle_follow()
            print("follow:", camera.following)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
            print("k pressed")
            if slime.distance_to_player < 20:
                player.toggleMountEntity(slime)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            print("e pressed")
            chest.interact()

    # ------------------
    # LOGIC
    # ------------------

    # Move Player
    player.move(dt)

    # Update Camera
    camera.move(dt)
    camera.follow(player)
    x_offset=((world_surface.get_width() / 2)-camera_pos.x)
    y_offset=((world_surface.get_height() / 2)-camera_pos.y)

    # Move Mobs
    slime.move(dt)

    # ------------------
    # WORLD AND PLAYER GRAPHICS
    # ------------------

    # Fill Screen
    world_surface.fill("white")

    # for x in range(int(world_surface.get_width()/world_tile_size+1)):
    #     for y in range(int(world_surface.get_height()/world_tile_size+1)):

    #         world_surface.blit(world_tileset.tiles[0], (world_tile_size*x+x_offset,world_tile_size*y+y_offset))

    generated_world.draw_terrain_map(screen, world_surface, world_tile_size, camera_pos)

    # Display Player
    player.draw(world_surface, x_offset, y_offset)

    # Display Mobs
    slime.draw(world_surface, x_offset, y_offset)

    # Display Environment
    chest.draw(world_surface, x_offset, y_offset, dt)
    
    # Scale World Surface to Screen
    scaled_world_surface = pygame.transform.scale(world_surface, (screen.get_width(),screen.get_height()))
    screen.blit(scaled_world_surface, (0,0))

    # ------------------
    # UI
    # ------------------

    # Display Player Position (not scaled)
    font_surface, _ = font.render(f"Player Position: ({player_pos.x:.0f}, {player_pos.y:.0f})", "black")
    screen.blit(font_surface, (10, 10))

    if camera.following:
        font_surface, _ = font.render(f"Lazy Camera ON (press c)", "black")
    else:
        font_surface, _ = font.render(f"Lazy Camera OFF (press c)", "black")
    screen.blit(font_surface, (10, 40))

    if slime.distance_to_player < 20:
        font_surface, _ = font.render(f"Jump On/Off Slimey (press k)", "black")
        screen.blit(font_surface, (10, 70))

    if chest.distanceToPlayer < 40:
        font_surface, _ = font.render(f"Open/Close chest (press e)", "black")
        screen.blit(font_surface, (10, 100))

    # Update the display with everything drawn
    pygame.display.flip()
    
    # delta time in seconds since last frame, used for framerate-independent physics
    dt = clock.tick(60) / 1000