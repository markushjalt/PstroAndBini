import pygame
import math
pygame.init() # initializes module

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # creates the pygame window
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255) # define color white
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
BROWN = (150, 75, 0)
LIGHT_BROWN = (196, 164, 132)
LIGHT_GREEN = (144, 238, 144)
DARK_BLUE = (0, 0, 255)

FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
    AU = 149.6e6 * 1000 # 1AU in meter
    G = 6.67428e-11
    SCALE = 200 / AU # 1AU = 100 pixels
    TIMESTEP = 3600*24 # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self. radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y *self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))

        pygame.draw.circle(win, self.color, (x,y), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y 
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP 
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

#def pre_questions():
    



def main():
    print("Do you want to study the inner or outer planets?")
    ans = input("Answer with \'inner\', \'outer\' or \'all\':\n")
    if ans == "inner":
        Planet.SCALE = 200 / Planet.AU
    else:
        Planet.SCALE = 15 / Planet.AU

    run = True
    clock = pygame.time.Clock() 

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth  = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 0.330 * 10**24)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    jupiter = Planet(4.97 * Planet.AU, 0, 26, BROWN, 1.898 * 10**27)
    jupiter.y_vel = -13.06 * 1000

    saturn = Planet(9.77 * Planet.AU, 0, 20, LIGHT_BROWN, 5.683 * 10**26)
    saturn.y_vel = -9.69 * 1000

    uranus = Planet(19.8 * Planet.AU, 0, 14, LIGHT_GREEN, 8.681 * 10**25)
    uranus.y_vel = -6.79 *1000

    neptune = Planet(30 * Planet.AU, 0, 14, DARK_BLUE, 1.024 * 10**26)
    neptune.y_vel = -5.45 * 1000



    planets = [sun, earth, mars, mercury, venus, jupiter, saturn, uranus, neptune]
    planets_inner = [sun, mercury, venus, earth, mars]
    planets_outer = [sun, jupiter, saturn, uranus, neptune]

    if ans == "inner":
        planets = planets_inner
    elif ans == "outer":
        planets = planets_outer
        sun.radius = sun.radius / 2
        jupiter.radius = jupiter.radius / 2
        saturn.radius = saturn.radius / 2
        uranus.radius = uranus.radius / 2
        neptune.radius = neptune.radius / 2

    while run: 
        clock.tick(60) # update screen max 60 times/sec
        WIN.fill((0, 0, 0)) 
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()
    
    pygame.quit()

#pre_questions()
main()
# test