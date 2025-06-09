import pygame
pygame.init()

screen = pygame.display.set_mode((1240,720),0,32)
screen.fill((0,0,0))
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()