import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 60
width  = 1200
height = 900
screen = pygame.display.set_mode((width, height))
tick = 0 # отсчеты для изменения скорости странного шарика
score = 0 # счетчик очков
font = pygame.font.Font(None, 50)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def create_new_ball():
    '''
    рисуем шарик
    x, y - координаты центра шарика
    r - радиус шарика
    vx, vy - проекции скоростей на оси x, y
    color - цвет шарика
    '''
    x = randint(100, 1100)
    y = randint(100, 900)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    r = randint(20, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    return {            
        'vx': vx,
        'vy': vy,
        'x': x,
        'y': y,            
        'r': r,
        'color': color
        }
def create_strange_ball():
    '''
    рисуем странный шарик
    x, y - координаты центра шарика
    r - радиус шарика
    vx, vy - проекции скоростей на оси x, y
    color - цвет шарика
    '''
    x = randint(100, 1100)
    y = randint(100, 900)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    r = randint(30, 50)
    circle(screen, WHITE, (x, y), r)
    circle(screen, BLACK, (x,y), r-15)
    return {
        'vx': vx,
        'vy': vy,
        'x': x,
        'y': y,
        'r': r
        }

balls = [create_new_ball() for i in range(10)]
strange_balls = [create_strange_ball() for i in range(2)]

pygame.display.update()
clock = pygame.time.Clock()
screen.fill(BLACK)
finished = False

while not finished:
    clock.tick(FPS)
    for ball in balls:
        # изменяем координаты шарика
        circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])
        ball['x'] += ball['vx']
        ball['y'] += ball['vy']
        # отражение от стенок
        if ball['x'] >= width or ball['x'] <= 0:
            ball['vx'] = randint (-10,10)
        if ball['y'] >= height or ball['y'] <= 0:
            ball['vy'] = randint (-10,10)
        # изменяем координаты странного шарика
        for strange_ball in strange_balls:
            for i in range(strange_ball['r']):
                circle(screen, WHITE, (strange_ball['x'], strange_ball['y']), strange_ball['r'] )
                circle(screen, BLACK, (strange_ball['x'], strange_ball['y']), strange_ball['r'] -15)
            strange_ball['x'] += strange_ball['vx']
            strange_ball['y'] += strange_ball['vy']
            tick += 1  
        # меняем скорость странного шарика
        if tick/2 > FPS :
            strange_ball['vx'] = randint(-1, 1)
            strange_ball['vy'] = randint(-1, 1)
            tick = 0
        # отражение странного шарика от стенок 
        if strange_ball['x'] >= width or strange_ball['x'] <= 0:
           strange_ball['vx'] = randint(-5,5)
        if strange_ball['y'] >= height or strange_ball['y'] <= 0:
            strange_ball['vy'] = randint(-5,5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # начисление очков при уничтожении обычного шарика
                mouse_x, mouse_y = event.pos
                for i, ball in enumerate(balls):
                    if (ball['x'] - mouse_x) ** 2 + (ball['y'] - mouse_y) ** 2 <= ball['r'] ** 2:
                        balls[i] = create_new_ball()
                        score += 1
                 # начисление очков при уничтожении странного шарика
                for i, strange_ball in enumerate(strange_balls):
                    if (strange_ball['x'] - mouse_x) ** 2 + (strange_ball['y'] - mouse_y) ** 2 <= strange_ball['r'] ** 2:
                        strange_balls[i] = create_strange_ball()
                        score += 5

        text = font.render('Score: ' + str(score), 1, (255, 255, 255))
        screen.blit(text, (0, 30))

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()