
import pygame
from pygame.locals import *
from time import time
import sys
import os

x = int(sys.argv[1])
y = int(sys.argv[2])
red = int(sys.argv[3])
green = int(sys.argv[4])
blue = int(sys.argv[5])
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

pygame.init()
surf = pygame.display.set_mode((10,10), pygame.NOFRAME)
surf.fill((red,green,blue))
pygame.display.flip()

t0 = time()
while True:
    e = pygame.event.wait()
    if e.type == pygame.MOUSEBUTTONDOWN:
        break

print int((time() - t0)*1000)
sys.stdout.flush()
sys.exit()
