from curses import KEY_LEFT
import pygame

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

while run:
    dt = clock.tick(50)
    screen.fill((0, 0, 0))

    for b in bricks:
        screen.blit(brick, b)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        bat_rect[0] -= 1
    if pressed[pygame.K_RIGHT]:
        bat_rect[0] += 1

    screen.blit(bat, (screen.get_width() // 2, bat_rect[1]))
    pygame.display.update()

pygame.quit()
