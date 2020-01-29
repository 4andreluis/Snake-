import pygame
from random import randint
from pygame.locals import *


# align apple
def on_grid_random():
    x = randint(0, 59)
    y = randint(0, 59)
    return x * 10, y * 10


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


# macro definition of snake drive
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
# star screen
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption(f'Snake')
# defining the snake
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
# defining the apple
apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((randint(0, 255), randint(0, 255), randint(0, 255)))

my_direction = RIGHT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0
game_over = False
while not game_over:
    clock.tick(20)  # snake speed
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # snake movement
        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
    # collision with the mace
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
        score += 1
    # high score
    aux = open('high.txt', 'r', encoding='UTF-8')
    a = int(aux.read())
    if score > a:
        x = str(score)
        aux2 = open('high.txt', 'w', encoding='UTF-8')
        aux2.write(x)
        aux.close()
        aux2.close()
    # check if it collided with the sides
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    # check if it collided with itself
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    # update the snake body
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    # texts that appear on the screen
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    arquivo_high = open('high.txt', 'r')
    high_score_font = font.render(f'high score: {arquivo_high.read()} ', True, (255, 255, 255))
    arquivo_high.close()
    high_score_rect = high_score_font.get_rect()
    high_score_rect.topleft = (5, 560)
    screen.blit(high_score_font, high_score_rect)
    score_font = font.render(f'score: {score}', True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (5, 580)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.center = (600 / 2, 300)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()