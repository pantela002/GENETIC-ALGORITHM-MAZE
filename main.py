import pygame
import sys
from Population import Population
from Info import *
import time
import matplotlib.pyplot as plt
from argparse import ArgumentParser
  
    
    

if __name__ == "__main__":


    simulation = 1   # CHANGE THIS TO CHANGE THE SIMULATION
    speed = 100      # CHANGE THIS TO CHANGE THE SPEED OF THE SIMULATION


    accuracy = []
    loss = []
    pygame.init()
    screen = pygame.display.set_mode(get_width_height(simulation))
    pygame.display.set_caption("Flying Dots")


    population = Population(get_population(simulation),simulation)
    all_sprites=population.get_all_sprites()

    x=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(accuracy)
                print(loss)
                pygame.quit()
                sys.exit()

        all_sprites.update(population.wall,population.maze)
        
        over = population.are_dead()

        if over==True:
            fitt,los = population.fitness()    
            accuracy.append(fitt)
            loss.append(los)
            population.dots.sort(key=lambda x: x.fitness, reverse=True)
            print(population.dots[0].fitness)
            print(population.dots[0].brain.step_count)
            print(population.dots[1].fitness)
            print(population.dots[1].brain.step_count)
            print(population.dots[2].fitness)
            print(population.dots[2].brain.step_count)


            for i in range(population.size//100 if simulation==8 else population.size//10, population.size):
                #population.sample(i)
                population.cross_over(i)
            for i in range(population.size):
                population.dots[i].brain.mutate()
            for i in range(population.size):
                population.dots[i].reset()    
            population.fit=0        
            for i in range(population.size):
                population.add_steps(i)


        screen.fill(white)

        all_sprites.draw(screen)

        
        pygame.display.flip()

        pygame.time.Clock().tick(speed)


