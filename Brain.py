import random
import math
from Info import *



class Brain:
    def __init__(self, size):
        self.directions = []
        self.step_count = size
        self.speed = random.randint(3, 11)
        self.randomize()
        self.angle = 0

    def randomize(self):


        angle = random.uniform(angle_interval[0], angle_interval[1])
        for i in range(self.step_count):
            angle_change = random.uniform(change_angle[0], change_angle[1])
            self.angle = angle_change
            angle+=angle_change
            x=round(self.speed * math.cos(angle))
            y=round(self.speed * math.sin(angle))
            self.directions.append([x,y])

    def clone(self):
        clone = Brain(self.step_count)
        clone.directions = self.directions.copy()
        return clone

    def mutate(self):
        mutation_rate = 0.01
        for i in range(self.step_count):
            if random.random() < mutation_rate:
                angle = random.uniform(angle_interval[0], angle_interval[1])
                angle_change = random.uniform(change_angle[0], change_angle[1])
                angle += angle_change
                x = round(self.speed * math.cos(angle))
                y = round(self.speed * math.sin(angle))
                self.directions[i] = [x,y]

    def add_steps(self,simulation):
        steps_add = get_step_add(simulation)
        self.step_count += steps_add
        angle =self.angle+ random.uniform(angle_interval[0], angle_interval[1])
        #sangle = self.angle+random.uniform(angle_interval[0], angle_interval[1])

        for i in range(steps_add):
            angle_change = random.uniform(change_angle[0], change_angle[1])
            angle += angle_change
            x = round(self.speed * math.cos(angle))
            y = round(self.speed * math.sin(angle))
            self.directions.append([x,y])


