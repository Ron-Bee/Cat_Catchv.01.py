
import pygame
from pygame.locals import *

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect()
        self.rect.centerx = 100
        
pygame.init()

screen = pygame.display.set_mode((800, 600))

square1.rect.topleft = ()
square2.rect.topright = ()  
square3.rect.bottomleft = ()
square4.rect.bottomright = ()

gameon = True

while gameon:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.k_BACKSPACE:
                gameon = False

        elif event.type == QUIT:
            running = False

screen.blit(square1.surf, (40, 40))
screen.blit(square2.surf, (40, 530))
screen.blit(square3.surf, (700, 40))
screen.blit(square4.surf, (700, 530))

pygame.display.flip()