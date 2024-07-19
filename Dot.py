import pygame
import math
import random
from Brain import Brain
from Info import *
from Wall import Wall

class Red_dot(pygame.sprite.Sprite):
    def __init__(self,simulation):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (get_red_dot_position(simulation))
        self.simulation = simulation




# Dot class
class Dot(pygame.sprite.Sprite):
    def __init__(self,simulation):
        super().__init__()
        self.simulation = simulation
        self.image = pygame.Surface((4, 4))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.center = get_center_dots(self.simulation)         
        self.brain = Brain(get_step_count(self.simulation))
        self.hit = False
        self.over = False
        self.step = 0
        self.fitness = 0
        self.hit_wall = False
        self.right_8=False
    def update(self,wall,maze):
        if not self.hit and not self.over and not (self.hit_wall and self.simulation != 1):
            self.rect.x += self.brain.directions[self.step][0]
            self.rect.y += self.brain.directions[self.step][1]
            self.step += 1

            if self.step == len(self.brain.directions)-1:
                self.over = True


            if self.rect.x < 10:
                self.rect.x = 10  # Set position to the right edge
                self.hit = True

            elif self.rect.x > get_width_height(self.simulation)[0] - 10:
                self.rect.x = get_width_height(self.simulation)[0] - 10
                self.hit = True

            elif self.rect.y < 10:
                self.rect.y = 10
                self.hit = True

            elif self.rect.y > get_width_height(self.simulation)[1] - 10:
                self.rect.y = get_width_height(self.simulation)[1] - 10
                self.hit = True

            if self.simulation!= 1 and self.simulation!= 8 and self.rect.colliderect(wall.rect):
                self.hit_wall = True

            if self.simulation == 8:
                for m in maze:
                    if self.rect.colliderect(m.rect):
                        self.hit_wall = True
                        break

            if  self.rect.x>get_wall_position(self.simulation)[0] and self.rect.y==get_width_height(self.simulation)[1]-10:
                self.hit_wall = True

    def reset(self):
        self.rect.center = get_center_dots(self.simulation)
        self.hit = False
        self.over = False
        self.step = 0
        self.hit_wall = False


    def get_hit_over(self):
        return self.hit or self.over or self.hit_wall
    

    def set_brain(self, directions):
        self.directions = directions.copy()

