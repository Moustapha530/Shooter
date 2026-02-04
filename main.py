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
    pygame.display.flip()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()