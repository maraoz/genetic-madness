#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Jun 4, 2010

@author: maraoz
'''


from time import sleep
from random import randint

from creature import Creature
from constants import ALL_COLORS




class Environment(object):
    
    def __init__(self):
        self.map = {}
    
    def add_creature(self, creature):
        x, y = creature.get_position()
        self.map[(x, y)] = creature
    
    def move(self, creature, old_x, old_y):
        del self.map[(old_x, old_y)]
        self.map[(creature.x, creature.y)] = creature
    
    def get_colors(self, x, y):
        return ALL_COLORS
    
    
    def run(self):
        time = 0
        
        while(True):
            print "Time: %d" % time
            for _, creature in self.map.items():
                creature.act()
                creature.brain_scan(str(time))
            time += 1
            sleep(10)



def main():
    
    e = Environment()
    for _ in xrange(10):
        c = Creature(e, randint(1, 100), randint(1, 100))
        e.add_creature(c)
    e.run()

if __name__ == "__main__":
    main()

