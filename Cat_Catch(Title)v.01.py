import pygame
from pygame.locals import *
import random
import sys
import os

class MainTitle:
    def __init__(self, text="Cat Catch"):
        self.surface = pygame.Surface((800, 600))
        self.surface.fill((255, 200, 200))
        font_path = os.path.abspath(r"C:\Users\Ron\Desktop\Python files misc\comic-sans-ms\ComicSansMS3.ttf")
        font = pygame.font.Font(font_path, int(87.5 * 1.75))  
        text_rendered = font.render(text, True, (0, 128, 128))
        text_rect = text_rendered.get_rect(center=self.surface.get_rect().center)
        self.surface.blit(text_rendered, text_rect)

def create_squares(num_squares):
    squares = []
    for _ in range(num_squares):
        square = pygame.Rect(random.randint(50, 750), random.randint(50, 550), 42.96875, 42.96875)  # Increase size by 25%
        squares.append(square)
    return squares

def update_square_positions(squares):
    for square in squares:
        square_speed = random.uniform(0.375, 1.875)  
        direction = random.choice(['left', 'right', 'up', 'down'])
        if direction == 'left' and square.left > 0:
            square.x -= square_speed
        elif direction == 'right' and square.right < 800:
            square.x += square_speed
        elif direction == 'up' and square.top > 0:
            square.y -= square_speed
        elif direction == 'down' and square.bottom < 600:
            square.y += square_speed

def draw_squares(screen, squares, colors):
    for square, color in zip(squares, colors):
        pygame.draw.rect(screen, color, square)

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

main_title = MainTitle()
squares = create_squares(25)
colors = [(random.randint(0, 100), random.randint(100, 200), random.randint(100, 255)) for _ in range(25)]

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    update_square_positions(squares)

    screen.fill((255, 198, 198))

    # Blit the title surface
    screen.blit(main_title.surface, (0, 0))

    # Draw all squares with fixed colors
    draw_squares(screen, squares, colors)

    pygame.display.update()
    clock.tick(60)

