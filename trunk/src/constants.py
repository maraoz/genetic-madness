#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Jun 4, 2010

@author: maraoz
'''
from os import mkdir


SESSION_DIRECTORY = "drawings"
try:
    mkdir(SESSION_DIRECTORY)
except:
    pass


ALL_COLORS = WHITE, GREEN, RED, BLUE = range(4)
COLOR_NAME = {WHITE:"white", GREEN:"green", RED:"red", BLUE: "blue"}

NORTH, EAST, SOUTH, WEST = ((+0, +1), (+1, +0), (+0, -1), (-1, +0))
DEFAULT_DIRECTION = NORTH
TURN_RIGHT = {NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH}  
