'''
Created on Aug 4, 2010

@author: maraoz
'''


from ga import FreeForAllGeneticAlgorithm
from random import randint, random, choice
from math import sqrt, sin, cos, pi
import pygame, subprocess, threading, os, sys
from time import sleep

pygame.init()
info = pygame.display.Info()
ch, cw = info.current_h, info.current_w
info = pygame.image.load("info.jpg")

class Spawner(threading.Thread):
    def __init__(self, window):
        threading.Thread.__init__(self) 
        self.window = window

    def run(self):
        process = subprocess.Popen(["python", "zerg.py", str(self.window.x), str(self.window.y),
                  str(self.window.r), str(self.window.g), str(self.window.b)],
                  stdout=subprocess.PIPE, shell=False)
        
        dt = process.stdout.read()
        self.window.fitness = int(dt or 0)
                
class Window():
    
    def __init__(self, (x, y), (r, g, b)):
        self.x, self.y = x, y
        self.color = self.r, self.g, self.b = r, g, b
        self.fitness = None
        
    def spawn(self):
        s = Spawner(self)
        s.start()
    
    def __repr__(self):
        return "creature at position (%d,%d) with color (%d,%d,%d)" % \
                   (self.x, self.y, self.r, self.g, self.b)
                
def fitness_function(window_list):
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)
    surf = pygame.display.set_mode((200,200), pygame.NOFRAME)
    surf.fill((255,255,255))
    surf.blit(info, (0,0))
    pygame.display.flip()
    
    while True:
        e = pygame.event.wait()
        if e.type == pygame.MOUSEBUTTONDOWN:
            break
        elif e.type == pygame.KEYDOWN:
            sys.exit(0)
    pygame.display.quit()
    sleep(1)
    
    buffer = []
    for window in window_list:
        coords = window.x, window.y
        while coords in buffer:
            window.x = randint(0, cw - 1)
            window.y = randint(0, cw - 1)
            coords = window.x, window.y
        buffer.append(coords)
        window.spawn()
    
    while threading.activeCount() > 1:
        print "Still waiting for %d threads to stop" % (threading.activeCount() - 1)
        sleep(3)
    print [w.fitness for w in window_list]
    return [w.fitness for w in window_list]
    
def random_chromosome_function():
    return Window((randint(0, cw - 1), randint(0, ch - 1)),
               (randint(0, 255), randint(0, 255), randint(0, 255)))
    

def mating_function(father, mother):
    r = randint(0, 3)
    new_clr = None
    if r is 0:
        new_clr = mother.color
    elif r is 1:
        new_clr = father.r, mother.g, mother.b
    elif r is 2:
        new_clr = father.r, father.g, mother.b
    else:
        new_clr = father.color
    x = father.x
    y = father.y
    if randint(0, 1) == 0:
        x = father.x
        y = mother.y
        
    return Window((x, y), new_clr)

def mutation_function(window):
    x, y, r, g, b = window.x, window.y, window.r, window.g, window.b
    if random() < 0.05:
        x = randint(0, cw - 1)
    if random() < 0.05:
        y = randint(0, ch - 1)
    if random() < 0.05:
        r = randint(0, 255)
    if random() < 0.05:
        g = randint(0, 255)
    if random() < 0.05:
        b = randint(0, 255)
    return Window((x, y), (r, g, b))

def generation_callback(window, fitness):
    print window, fitness

if __name__ == "__main__":
    algo = FreeForAllGeneticAlgorithm(fitness_function, random_chromosome_function,
                 mating_function, mutation_function, generation_callback, max_generations=100000,
                 population_size=15)
    t, f = algo.run()
    
    print "Done!"
    raw_input("Press enter to terminate.")
