import pygame

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SPEED = 1.3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("Pygame HowTo")


sprite_butterfly = pygame.image.load("images/butterfly.png")
sprite_butterfly = pygame.transform.scale(sprite_butterfly, (32, 32))

sprite_butterfly_width = sprite_butterfly.get_width()
sprite_butterfly_height = sprite_butterfly.get_height()

screen.fill((0, 0, 0))
game_over = False

x, y = (0, 0)

clock = pygame.time.Clock()

while not game_over:
    dt = clock.tick(300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True

        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            x -= sprite_butterfly_width / 2
            y -= sprite_butterfly_height / 2

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= SPEED * dt
    if pressed[pygame.K_DOWN]:
        y += SPEED * dt
    if pressed[pygame.K_LEFT]:
        x -= SPEED * dt
    if pressed[pygame.K_RIGHT]:
        x += SPEED * dt
    if pressed[pygame.K_SPACE]:
        x = 0
        y = 0
    if pressed[pygame.K_F1]:
        SPEED = 1
    if pressed[pygame.K_F2]:
        SPEED = 2

    if x > (screen.get_width() + sprite_butterfly_width):
        x = 0 - sprite_butterfly_width

    if x < 0 - sprite_butterfly_width:
        x = screen.get_width() - sprite_butterfly_width

    if y < 0 - sprite_butterfly_width:
        y = screen.get_height() + sprite_butterfly_height

    if y > screen.get_height() + sprite_butterfly_height:
        y = 0 - sprite_butterfly_height

    screen.fill((0, 0, 0))
    screen.blit(
        sprite_butterfly,
        (x, y),
    )

    pygame.display.update()

pygame.quit()
