import pygame

from player import Player

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('New World')

game_is_running = True
clock = pygame.time.Clock()
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while game_is_running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False

    # LOGIC
    # ...

    screen.fill("white")

    # GRAPHICS
    # ...

    # Create Player
    player = Player(player_pos)

    pygame.draw.circle(screen, "black", player_pos, 40)

    # Move Player
    player.move(dt)
   
    # Display Player Position
    font = pygame.freetype.Font("assets/fonts/OpenSans-Medium.ttf", 24)
    font_surface, _ = font.render(f"Player Position: ({player_pos.x:.0f}, {player_pos.y:.0f})", "black")
    screen.blit(font_surface, (10, 10))


    # Update the display with everything drawn
    pygame.display.flip()
    
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()