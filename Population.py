import math
import random
from Dot import Dot, Red_dot
import pygame
from Info import *
from Brain import Brain
from Wall import Wall
from Maze import Maze


class Population:
    def __init__(self, size, simulation):
        self.simulation = simulation
        self.size = get_population(self.simulation)
        self.make_dots()
        self.red_dot = Red_dot(simulation)
        self.wall = Wall(self.simulation)
        self.maze = [ Maze(self.simulation,i) for i in range(26)]
        self.all_sprites = pygame.sprite.Group()
        self.add_sprites()
        self.fit=0
        self.loss=0


    def make_dots(self):
        self.dots = []
        for i in range(self.size):
            self.dots.append(Dot(self.simulation))

    def add_sprites(self):
        self.all_sprites.add(self.dots)
        self.all_sprites.add(self.red_dot)
        self.all_sprites.add(self.wall) if self.simulation != 1 and self.simulation !=8 else None
        self.all_sprites.add(self.maze) if self.simulation == 8 else None


    def get_all_sprites(self):
        return self.all_sprites
    
    def fitness(self):
        
        for dot in self.dots:
            if self.simulation >4 and self.simulation != 8:
                if dot.hit_wall:
                    dot.fitness = 0
                else:
                    distance = math.sqrt((dot.rect.x - self.red_dot.rect.x) ** 2 + (dot.rect.y - self.red_dot.rect.y) ** 2)
                    dot.fitness = 1 / (distance ** 2 + epsilon)
                    #dot.fitness *= 0.9 if dot.hit else 1
            else:
                distance = math.sqrt((dot.rect.x - self.red_dot.rect.x) ** 2 + (dot.rect.y - self.red_dot.rect.y) ** 2)
                dot.fitness = 1 / (distance ** 2 + epsilon)
            if self.simulation == 8:
                distance = math.sqrt((dot.rect.x - self.red_dot.rect.x) ** 2 + (dot.rect.y - self.red_dot.rect.y) ** 2)
                dot.fitness = 1 / (distance ** 2 + epsilon)
                if dot.hit_wall:
                    dot.fitness=0
                elif dot.hit:
                    dot.fitness = dot.fitness/100
            self.fit += dot.fitness
            self.loss += math.sqrt((dot.rect.x - self.red_dot.rect.x) ** 2 + (dot.rect.y - self.red_dot.rect.y) ** 2)
        self.fit /= self.size
        self.loss /= self.size
        return self.fit,self.loss
    def are_dead(self):
        for dot in self.dots:
            if not dot.get_hit_over():
                return False
        return True    
    
    def cross_over(self, index):
        random1= random.randint(0, get_max_sample(self.simulation))
        random2= random.randint(0, get_max_sample(self.simulation))

        parent1 = self.dots[random1].brain
        parent2 = self.dots[random2].brain

        child = Brain(parent1.step_count)

        midpoint = random.randint(0, parent1.step_count)
        for i in range(parent1.step_count):
            if i > midpoint:
                child.directions[i] = parent1.directions[i].copy()
            else:
                child.directions[i] = parent2.directions[i].copy()
        self.dots[index].brain.directions = child.directions.copy()


    def sample(self,index):
        random1 = random.randint(0, self.size//5)
        self.dots[index].brain.directions = self.dots[random1].brain.directions.copy()
        
    def add_steps(self,index):
        self.dots[index].brain.add_steps(self.simulation)