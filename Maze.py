from Info import *
import pygame

class Maze(pygame.sprite.Sprite):
    def __init__(self,simulation,index):
        super().__init__()
        self.index = index
        self.simulation = simulation
        self.make_maze(index)


    def make_maze(self,index):
        if index == 0:
            area=(12,300)
        elif index == 1:
            area=(12,200)
        elif index == 2:
            area=(12,100)
        elif index == 3:
            area=(12,200)
        elif index == 4:
            area=(12,100)
        elif index == 5:
            area=(12,200)
        elif index == 6:
            area=(12,300)
        elif index == 7:
            area=(12,200)
        elif index == 8:
            area=(12,300)
        elif index == 9:
            area=(12,200)
        elif index == 10:
            area=(12,200)
        elif index == 11:
            area=(12,200)
        elif index == 12:
            area=(12,200)
        elif index == 13:
            area=(12,100)
        elif index == 14:
            area=(12,100)

        elif index == 15:
            area=(200,12)
        elif index == 16:
            area=(100,12)
        elif index == 17:
            area=(300,12)
        elif index == 18:
            area=(200,12)
        elif index == 19:
            area=(100,12)
        elif index == 20:
            area=(200,12)
        elif index == 21:
            area=(200,12)
        elif index == 22:
            area=(200,12)
        elif index == 23:
            area=(200,12)
        elif index == 24:
            area=(100,12)
        elif index == 25:
            area=(100,12)

        


        self.image = pygame.Surface(area)  
        self.image.fill(blue)
        self.rect = self.image.get_rect()

        if index == 0:
            self.rect.center = (100,550)
        elif index == 1:
            self.rect.center = (100,100)
        elif index == 2:
            self.rect.center = (200,750)
        elif index == 3:
            self.rect.center = (200,400)
        elif index == 4:
            self.rect.center = (200,150)
        elif index == 5:
            self.rect.center = (300,700)
        elif index == 6:
            self.rect.center = (300,250)
        elif index == 7:
            self.rect.center = (400,600)
        elif index == 8:
            self.rect.center = (400,150)
        elif index == 9:
            self.rect.center = (500,600)
        elif index == 10:
            self.rect.center = (500,300)
        elif index == 11:
            self.rect.center = (600,700)
        elif index == 12:
            self.rect.center = (600,400)
        elif index == 13:
            self.rect.center = (700,750)
        elif index == 14:
            self.rect.center = (700,450)   
        elif index == 15:
            self.rect.center = (500,100) 
        elif index == 16:
            self.rect.center = (250,200)
        elif index == 17:
            self.rect.center = (650,200)
        elif index == 18:
            self.rect.center = (100,300)
        elif index == 19:
            self.rect.center = (650,300)
        elif index == 20:
            self.rect.center = (400,400)
        elif index == 21:
            self.rect.center = (300,500)
        elif index == 22:
            self.rect.center = (600,500)
        elif index == 23:
            self.rect.center = (200,600)
        elif index == 24:
            self.rect.center = (650,600)
        elif index == 25:
            self.rect.center = (450,700)

        

