import pygame, sys # import statement for pygame and sys modules
from pygame.locals import *

pygame.init() # need to call init function for pygame to work
DISPLAYSURF = pygame.display.set_mode((400, 300)) # sets dimensions of window
pygame.display.set_caption('Hello World!') # caption text appears in title bar
while True: # main game loop
    for event in pygame.event.get(): # for loop iterates over list of event objects created by `pygame.event.get()`
        if event.type == QUIT:
            pygame.quit()
            sys.exit() # terminates the program
    pygame.display.update()
