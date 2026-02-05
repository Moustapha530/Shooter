import pygame
from game import Game

pygame.init()

game = Game()

pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((800, 500))
background = pygame.image.load('assets/bg.jpg')

running = True

while running:
    screen.blit(background, (0, -400))
    screen.blit(game.player.image, game.player.rect)

    game.player.all_projectiles.draw(screen)

    for projectile in game.player.all_projectiles:
        projectile.move()

    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()

    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()

    pygame.display.flip()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
