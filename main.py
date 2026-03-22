import pygame
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
from player import Player
from slime import Slime
from camera import Camera
from tileset import Tileset

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

# Player
player_pos = pygame.Vector2(world_surface.get_width() / 2, world_surface.get_height() / 2)
player = Player(player_pos)

# Slime
slime_pos = pygame.Vector2(world_surface.get_width() / 2, world_surface.get_height() / 2 + 50)
slime = Slime(slime_pos, player)

# Camera
camera_pos = pygame.Vector2(world_surface.get_width() / 2, world_surface.get_height() / 2)
camera = Camera(camera_pos)

# UI
font = pygame.freetype.Font("assets/fonts/OpenSans-Medium.ttf", 20)

# # Noise
# noise = PerlinNoise(0.5,seed=seed)

# noise1 = PerlinNoise(octaves=0.5,seed=seed)
# noise2 = PerlinNoise(octaves=1,seed=seed)
# noise3 = PerlinNoise(octaves=2,seed=seed)
# noise4 = PerlinNoise(octaves=4,seed=seed)

# xpix = screen.get_width()
# ypix = screen.get_height()
# pic = []
# for y in range(ypix):
#     row = []
#     for x in range(xpix):
#         noise_val =         noise1([x/xpix, y/ypix])
#         # noise_val += 0.5  * noise2([i/xpix, j/ypix])
#         # noise_val += 0.25 * noise3([i/xpix, j/ypix])
#         # noise_val += 0.125* noise4([i/xpix, j/ypix])

#         row.append(noise_val)
#     pic.append(row)

# plt.imshow(pic, cmap='gray')
# plt.show()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            camera.toggle_follow()
            print("follow:", camera.following)

    # ------------------
    # LOGIC
    # ------------------

    # Move Player
    player.move(dt)

    # Update Camera
    camera.move(dt)
    camera.follow(player.player_pos)
    x_offset=((world_surface.get_width() / 2)-camera_pos.x)
    y_offset=((world_surface.get_height() / 2)-camera_pos.y)

    # Move Mobs
    slime.move(dt)

    # ------------------
    # WORLD AND PLAYER GRAPHICS
    # ------------------

    # Fill Screen
    world_surface.fill("white")

    for x in range(int(world_surface.get_width()/world_tile_size+1)):
        for y in range(int(world_surface.get_height()/world_tile_size+1)):

            world_surface.blit(world_tileset.tiles[0], (world_tile_size*x+x_offset,world_tile_size*y+y_offset))

    # Display Player
    player.draw(world_surface, x_offset, y_offset)

    # Display Mobs
    slime.draw(world_surface, x_offset, y_offset)
    
    # Scale World Surface to Screen
    scaled_world_surface = pygame.transform.scale(world_surface, (screen.get_width(),screen.get_height()))
    screen.blit(scaled_world_surface, (0,0))

    # # draw noise
    # for x in range(int(screen.get_width())):
    #     for y in range(int(screen.get_height())):
    #         #pygame.draw.circle(world_surface, "blue", (world_tile_size*x,world_tile_size*y), world_tile_size/3)

    #         noise_value = noise1([x/screen.get_width(),y/screen.get_height()])
    #         noise_value += 0.5  * noise2([x/screen.get_width(),y/screen.get_height()])
    #         noise_value += 0.25 * noise3([x/screen.get_width(),y/screen.get_height()])
    #         noise_value += 0.125* noise4([x/screen.get_width(),y/screen.get_height()])

    #         #print(noise_value)
    #         noise_value = noise_value * 4
    #         noise_value += 1.0
    #         noise_value = noise_value*255.0/2.0
    #         pygame.draw.rect(surface=screen, color=(noise_value,noise_value,noise_value),rect=(x,y,1,1))

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

    # Update the display with everything drawn
    pygame.display.flip()
    
    # delta time in seconds since last frame, used for framerate-independent physics
    dt = clock.tick(60) / 1000