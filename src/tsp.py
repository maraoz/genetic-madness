'''
Created on Aug 3, 2010

@author: maraoz
'''


from ga import CrossoverGeneticAlgorithm
from random import randint, random, choice
from math import sqrt, sin, cos, pi
import pygame

X = 0
Y = 1

CITY_N = 30
SWAP_N = 500
CROSSOVER_P = 0.8
MUTATION_P = 0.0005


class Map(object):
    def __init__(self, n=10):
        self.n = n
        self.cities = []
        for i in xrange(n):
            #self.cities.append((randint(0,640), randint(0,480)))
            self.cities.append((320+200*cos(i*2*pi/n), 240+200*sin(i*2*pi/n)))
    
    def distance(self, i, j):
        city_i = self.cities[i]
        city_j = self.cities[j]
        return sqrt((city_i[X]-city_j[X])**2 + (city_i[Y] - city_j[Y])**2)

m = Map(CITY_N)

            
class Tour(object):
    def __init__(self, swaps):
        self.swaps = swaps
        self.data = []
        for i in xrange(CITY_N):
            self.data.append(i)
        for (a, b) in swaps:
            self.data[a], self.data[b] = self.data[b], self.data[a]
    def __repr__(self):
        return str(self.data)
        

def fitness_function(circuit):
    distance = 0
    for i in xrange(CITY_N-1):
        distance += m.distance(circuit.data[i], circuit.data[i+1])
    distance += m.distance(circuit.data[CITY_N-1], circuit.data[0])
    return 1/distance
    
def random_chromosome_function():
    swaps = []
    for _ in xrange(SWAP_N):
        a = randint(0, CITY_N - 1)
        b = randint(0, CITY_N - 1)
        swaps.append((a, b))
    return Tour(swaps) 

def mating_function(father, mother):
    r = random()
    if r < CROSSOVER_P:
        crossover_point = randint(0, len(father.swaps) - 1)
        new_genes = father.swaps[:crossover_point] + mother.swaps[crossover_point:]
        return Tour(new_genes)
    return choice([father, mother])

def mutation_function(tour):
    swaps = []
    for a, b in tour.swaps:
        if random() < MUTATION_P:
            a = randint(0, CITY_N - 1)
        if random() < MUTATION_P:
            b = randint(0, CITY_N - 1)
        swaps.append((a, b))
    return Tour(swaps)

screen = pygame.display.set_mode((640,480))
first_time = True
def generation_callback(tour, fitness):
    screen.fill((0,0,0))
    color = (255,255,255)
    path = []
    for index in tour.data:
        x,y = m.cities[index][X], m.cities[index][Y]
        pygame.draw.circle(screen, color, (x,y), 3)
        path.append((x,y))
    pygame.draw.lines(screen, (255,0,0), True, path)
    pygame.display.flip()
    global first_time
    if first_time is True:
        first_time = False
        raw_input("comfirm you could screenshot")
    print tour, 1/fitness

if __name__ == "__main__":
    algo = CrossoverGeneticAlgorithm(fitness_function, random_chromosome_function,
                 mating_function, mutation_function, generation_callback, max_generations=100000,
                 population_size=100)
    t, f =  algo.run()
        
    
    print "Done!"
    #print t, 1/f
    raw_input("Press enter to terminate.")
