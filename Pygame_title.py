import pygame
from pygame.locals import *

class main_title():
    def __init__(self):
        self.title_surf = pygame.Surface((800, 600))
        self.title_surf.fill((255, 200, 200))
        font = pygame.font.Font(None, 50)
        text = font.render("Catch Catch", True, (0, 128, 128)) 
        text_rect = text.get_rect(center=self.surf.get_rect().center)
        self.surf.blit(text, text_rect)

        self.title_surf.blit(self.surf, (0, 0))


class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 128, 128))
        self.rect = self.surf.get_rect()
        self.rect.centerx = 100

def create_squares():
    square1 = Square()
    square2 = Square()
    square3 = Square()
    square4 = Square()
    return square1, square2, square3, square4



pygame.init()
title_screen = main_title()
screen = pygame.display.set_mode((800, 600))
main_title_surf = main_title()

squares = create_squares()

gameon = True


while gameon:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.k_BACKSPACE:
                gameon = False

        elif event.type == pygame.QUIT:
            running = False


screen.fill((255, 200, 200))
screen.blit(title_screen.title_surf, (0, 0))
screen.blit(main_title_surf)
screen.blit(squares[0].surf, (40, 40))
screen.blit(squares[1].surf, (40, 530))
screen.blit(squares[2].surf, (700, 40))
screen.blit(squares[3].surf, (700, 530))
screen_width, screen_height = screen.get_size()
screen.blit(main_title_surf, main_title_surf.get_rect(center_x=screen_width//2, center_y=screen_height//2))

    
   
pygame.display.update()

   

pygame.quit()