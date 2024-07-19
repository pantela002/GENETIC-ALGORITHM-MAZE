from Info import *
import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self,simulation):
        super().__init__()
        self.simulation = simulation
        self.image = pygame.Surface(get_wall_size(self.simulation))  
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.center = get_wall_position(self.simulation)







