#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Jun 4, 2010

@author: maraoz
'''

from brain import Sensor, Motor
from brain import random_brain

from constants import WHITE, GREEN, RED, BLUE, DEFAULT_DIRECTION, TURN_RIGHT, COLOR_NAME

class ColorSensor(Sensor):
    def __init__(self, creature, environment, color=WHITE, *args, **kwargs):
        Sensor.__init__(self, *args, **kwargs)
        
        self.environment = environment
        self.creature = creature
        self.color = color
        
        self.name = COLOR_NAME[self.color] + "_sensor"
        
    def read_value(self):
        x = self.creature.x
        y = self.creature.y
        return self.color in self.environment.get_colors(x, y)
        

class MovementMotor(Motor):
    def __init__(self, environment, creature):
        self.creature = creature
        self.environment = environment
        
class ForwardMovementMotor(MovementMotor):
    name = "forward"
    def activate(self):
        x = self.creature.x
        y = self.creature.y
        self.creature.move_forward()
        self.environment.move(self.creature, x, y)

class RotationMovementMotor(MovementMotor):
    name = "rotate"
    def activate(self):
        self.creature.rotate()
        

class Creature(object):
    
    def __init__(self, environment, x, y, direction=DEFAULT_DIRECTION):
        
        self.environment = environment
        self.x = x
        self.y = y
        self.direction = direction
        
        self.sensors = [ColorSensor(self, environment, color) \
                        for color in (GREEN, RED, BLUE)]
        
        self.motors = [ForwardMovementMotor(environment, self), \
                       RotationMovementMotor(environment, self)]
        
        self.brain = random_brain(self.sensors, self.motors)
    
    def move_forward(self):
        dx, dy = self.direction
        self.x += dx
        self.y += dy
        print "Moving forward to position (%d, %d)." % (self.x, self.y)
    
    def rotate(self):
        print "Rotating"
        self.direction = TURN_RIGHT[self.direction]
    
    def get_position(self):
        return self.x, self.y

    def act(self):
        self.brain.think()
    
    def brain_scan(self, suffix=""):
        self.brain.draw(True, suffix)


