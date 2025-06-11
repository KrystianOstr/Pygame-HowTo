import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

square = pygame.Rect(100, 100, 80, 80)
dragging = False
offset_x = 0
offset_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if square.collidepoint(event.pos):
                dragging = True
                mouse_x, mouse_y = event.pos
                offset_x = square.x - mouse_x
                offset_y = square.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x, mouse_y = event.pos
                square.x = mouse_x + offset_x
                square.y = mouse_y + offset_y

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 200, 100), square)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()