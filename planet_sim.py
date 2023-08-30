import pygame
import math
pygame.init() # initializes module

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # creates the pygame window
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255) # define color white

class Planet:
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self. radius = radius
        self.color = color
        self.mass = mass

        self.x_vel = 0
        self.y_vel = 0

def main():
    run = True
    clock = pygame.time.Clock() 

    while run: 
        clock.tick(60) # update screen max 60 times/sec
        #WIN.fill(WHITE) 
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

main()
