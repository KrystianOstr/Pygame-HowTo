import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breakin' Bricks")

# bat
bat = pygame.image.load("images/paddle.png").convert_alpha()
bat_rect = bat.get_rect()
bat_rect[1] = screen.get_height() - 100

# ball
ball = pygame.image.load("images/football.png").convert_alpha()
ball_rect = ball.get_rect()
ball_start = (200,200)
ball_speed = (3.0,3.0)
ball_served = False
sx, sy = ball_speed
ball_rect.topleft = ball_start

# brick

brick = pygame.image.load("images/brick.png").convert_alpha()
brick_rect = brick.get_rect()

bricks = []
brick_rows = 5
brick_gap = 10
brick_cols = screen.get_width() // (brick_rect[2] + brick_gap)
side_gap = (
    screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap
) // 2


for y in range(brick_rows):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX, brickY))


clock = pygame.time.Clock()
run = True
x = 0

while run:
    dt = clock.tick(50)
    screen.fill((0, 0, 0))

    for b in bricks:
        screen.blit(brick, b)

    screen.blit(bat, bat_rect)
    screen.blit(ball, ball_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -= 1 * dt
    if pressed[pygame.K_RIGHT]:
        x += 1 * dt
    if pressed[pygame.K_SPACE]:
        ball_served = True


    # if ball_rect.bottom >= bat_rect.top and \
    # ball_rect.top < bat_rect.top and \
    # ball_rect.right >= bat_rect.left and \
    # ball_rect.left <= bat_rect.right:
    #     sy *= -1

    if bat_rect[0] + bat_rect.width >= ball_rect[0] >= bat_rect[0] and \
    ball_rect[1] + ball_rect.height >= bat_rect[1] and \
    sy > 0:
        sy *= -1
        continue
    
    #screen restriction  
    if ball_rect.top <= 0:
        sy *=-1
    if ball_rect.bottom >= screen.get_height():
        sy *=-1
    if ball_rect.left <= 0:
        sx*=-1  
    if ball_rect.right >= screen.get_width():
        sx*=-1



    bat_rect[0] = x
    if ball_served:
        ball_rect[0] += sx
        ball_rect[1] += sy
 

    pygame.display.update()

pygame.quit()
