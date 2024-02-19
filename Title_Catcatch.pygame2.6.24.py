import pygame
from pygame.locals import *
import random

class MainTitle:
    def __init__(self, text="Catch Catch"):
        self.surface = pygame.Surface((800, 600))
        self.surface.fill((255, 200, 200))
        font = pygame.font.Font(None, 50)
        text_rendered = font.render(text, True, (0, 128, 128))
        text_rect = text_rendered.get_rect(center=self.surface.get_rect().center)
        self.surface.blit(text_rendered, text_rect)

def create_squares():
    squares = []
    for _ in range(4):
        square = pygame.Surface((25, 25))
        square.fill((0, 128, 128))
        squares.append(square)
    return squares

def update_square_positions(squares):
    for square in squares:
        speed = random.randint(1, 5)
        direction = random.choice(['left', 'right', 'up', 'down'])
        if direction == 'left':
            square.move_ip(-speed, 0)
        elif direction == 'right':
            square.move_ip(speed, 0)
        elif direction == 'up':
            square.move_ip(0, -speed)
        elif direction == 'down':
            square.move_ip(0, speed)

pygame.init()
screen = pygame.display.set_mode((800, 600))
main_title = MainTitle()
squares = create_squares()
game_on = True

clock = pygame.time.Clock()

while game_on:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_BACKSPACE:
            game_on = False
        elif event.type == QUIT:
            game_on = False

    update_square_positions(squares)

    screen.fill((255, 200, 200))
    screen.blit(main_title.surface, (0, 0))

    positions = [(40, 40), (40, 530), (700, 40), (700, 530)]
    for i in range(4):
        screen.blit(squares[i], positions[i])

    screen_width, screen_height = screen.get_size()
    screen.blit(main_title.surface, main_title.surface.get_rect(center=(screen_width // 2, screen_height // 2)))

    pygame.display.update()

    clock.tick(30)  # Limit frames per second to 30

pygame.quit()
