import pygame

from pygame.locals import *


class Pygame:
    def __init__(self, background_image, size, window_caption, fps, background_colour, background_alpha):
        pass
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
    def add(self, element):
        pass
    
    def loop(self, callback):
        pass
        
class Element:
    def __init__(self, image, parent, center_position, speed):
        pass
        
background_image = "RoboCatpre.png"
size = [480, 270]
window_caption = "Cat Catch"
fps = 60
background_colour = (4, 44, 444)
background_alpha = 255

with Pygame(background_image=background_image, 
            size=size, 
            window_caption=window_caption, 
            fps=fps, 
            background_colour=background_colour,
            background_alpha=background_alpha) as pg:
            
    element = Element(image=None, 
                      parent=None, 
                      center_position=[0, 0], 
                      speed=[1, 1])
                      
    pg.add(element)
                      
    pg.loop(lambda: background_image)
