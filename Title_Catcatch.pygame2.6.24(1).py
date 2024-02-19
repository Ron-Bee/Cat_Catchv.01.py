import pygame
from pygame.locals import *
import random
import sys

class MainTitle:
    def __init__(self, text="Cat Catch"):
        self.surface = pygame.Surface((800, 600))
        self.surface.fill((255, 200, 200))
        font = pygame.font.Font(None, 50)
        text_rendered = font.render(text, True, (0, 128, 128))
        text_rect = text_rendered.get_rect(center=self.surface.get_rect().center)
        self.surface.blit(text_rendered, text_rect)

def create_squares():
    squares = []
    for _ in range(4):
        square = pygame.Rect(random.randint(50, 725), random.randint(50, 525), 25, 25)
        squares.append(square)
    return squares

def update_square_positions(squares):
    for square in squares:
        if isinstance(square, pygame.Rect):
            speed = random.randint(1, 5)
            direction = random.choice(['left', 'right', 'up', 'down'])
            if direction == 'left' and square.left > 0:
                square.x -= speed
            elif direction == 'right' and square.right < 800:
                square.x += speed
            elif direction == 'up' and square.top > 0:
                square.y -= speed
            elif direction == 'down' and square.bottom < 600:
                square.y += speed

pygame.init()
screen = pygame.display.set_mode((800, 600))
main_title = MainTitle()
squares = create_squares()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                pygame.quit()
                sys.exit()
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    update_square_positions(squares)

    screen.fill((255, 200, 200))
    
    for square in squares:
        if isinstance(square, pygame.Rect):
            pygame.draw.rect(screen, (0, 178, 178), square)  # Light teal color

    screen.blit(main_title.surface, (0, 0))

    pygame.display.update()

    clock.tick(30)  # Limit frames per second to 30

    # Debugging: Print square positions
    print([square.topleft for square in squares])

