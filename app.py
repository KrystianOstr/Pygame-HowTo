import pygame
pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)


sprite_butterfly = pygame.image.load('images/butterfly.png')
sprite_butterfly = pygame.transform.scale(sprite_butterfly, (32,32))

sprite_butterfly_width = sprite_butterfly.get_width()
sprite_butterfly_height = sprite_butterfly.get_height()

pygame.display.set_caption('Pygame HowTo')
screen.fill((0,0,0))
game_over = False

x,y = (0,0)

clock = pygame.time.Clock()

while not game_over:
    dt = clock.tick(300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y-=1*dt
    if pressed[pygame.K_DOWN]:
        y+=1*dt
    if pressed[pygame.K_LEFT]:
        x-=1*dt
    if pressed[pygame.K_RIGHT]:
        x+=1*dt
    if pressed[pygame.K_SPACE]:
        x = 0
        y = 0
            

    if x > (screen.get_width() +sprite_butterfly_width):
        x = 0 - sprite_butterfly_width

    if x < 0 - sprite_butterfly_width:
        x = screen.get_width()-sprite_butterfly_width

    if y < 0 - sprite_butterfly_width:
        y = screen.get_height() + sprite_butterfly_height

    if y > screen.get_height() + sprite_butterfly_height:
        y = 0 - sprite_butterfly_height

    screen.fill((0,0,0))
    screen.blit(sprite_butterfly, (x, y))

    pygame.display.update()

pygame.quit()