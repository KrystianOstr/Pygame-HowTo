import pygame as py
import random

py.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
FPS = 60

max_health = 200
current_health = 10
overheal_text_timer = 0


font_ultra_big = py.font.SysFont('Roboto', 60)
font_big = py.font.SysFont('Roboto', 40)
font_small = py.font.SysFont('Roboto', 22)

#colors
green = (0,255,0)
red = (255,0,0)
white = (255,255,255)

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Health bar")
clock = py.time.Clock()
run = True
game_state= 'running'


def get_random_value(max_value, min_value = 0):
    random_value = random.randint(min_value, max_value)
    return random_value

def draw_healthbar():
    rect_red = py.Rect(10,10,max_health,20)
    rect_green = py.Rect(10,10,current_health,20)
    py.draw.rect(screen, red, rect_red)
    py.draw.rect(screen, green, rect_green)

    text_surface = font_big.render(f"{current_health} / {max_health}", True, white)
    text_rect = text_surface.get_rect(center=(110,55))
    screen.blit(text_surface, text_rect)

def draw_death_screen():
    text_surface = font_ultra_big.render('You are dead', True, white)
    text_rect = text_surface.get_rect(center=(300,300))
    screen.blit(text_surface,text_rect)

def draw_overheal_is_not_allowed_text():
    text_surface = font_small.render("Overheal is not allowed, man!", True, white)
    text_rect = text_surface.get_rect(center=(110,85))
    screen.blit(text_surface, text_rect)

def handle_input(event):
    if event.type == py.MOUSEBUTTONDOWN:
        handle_mouse(event)
    if event.type == py.KEYDOWN:
        handle_keyboard(event)


def add_wounds():
    global game_state, current_health

    current_health -= get_random_value(20)
    current_health = max(current_health, 0)
    if current_health <= 0:
        draw_healthbar()
        py.display.update()
        py.time.delay(500)
        game_state = 'dead'

def add_healing():
    global current_health,max_health, overheal_text_timer
    if current_health >= max_health:
        overheal_text_timer = py.time.get_ticks() + 1000
        return
            
    current_health += get_random_value(20, 15)
    current_health = min(current_health,max_health)

def handle_keyboard(event):
    global game_state
    if game_state == 'running':
        if event.key == py.K_LEFT:
            add_wounds()
        if event.key == py.K_RIGHT:
            add_healing()


def handle_mouse(event):
    global game_state
    if game_state == "running":
        if event.button == 1:
            add_wounds()
                            
        if event.button == 3:
            add_healing()
                
    

while run:
    clock.tick(FPS)
    screen.fill((0,0,0))
    if py.time.get_ticks() < overheal_text_timer:
        draw_overheal_is_not_allowed_text()


    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                run = False


        handle_input(event)
    
    if game_state == "running":
        draw_healthbar()
        py.display.update()

    if game_state == 'dead':
        draw_death_screen()
        py.display.update()

    py.display.update()

py.quit()