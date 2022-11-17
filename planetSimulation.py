import pygame
import math

pygame.init() # inicializacion
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # configura la ventana del programa
pygame.display.set_caption("Planet Simulation")

WHITE = (255,255,255) # valor rgb del blanco
YELLOW = (255, 255, 0)
BLUE = (0,32,255)
RED = (161,40,48)
DARK_GREY = (105,105,105)

# distancia de los planetas al sol
FONT = pygame.font.SysFont("comicsans", 16)

# planetas y sus fisicas
class Planet: 

    AU = 149.6e6 * 1000 #astronomical unit: equivale a la distancia entre la tierra y el sol, nos ayudará a calcular
    #la distancia entre el planeta especifico y el sol ( en metros)

    G = 6.67428e-11 # constante gravitacional  =! de la aceleracion de la gravedad, es la capacidad de atraccion
    SCALE = 250 / AU # (1AU = 100 pixels) representacion de distancias por pixeles en nuestro programa
    TIMESTEP = 3600*24 # tiempo de simulacion real, representa un día por segundo

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass # en kilogramos

        # caracteristicas especificas de los planetas
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        # velocidades para generar las orbitas
        self.x_vel = 0
        self.y_vel = 0
    
    # dibujado de los planetas
    def draw(self, win):
        # distancias en metros a escala de los pixeles 
        # tambien hacemos que el dibujado sea en el centro de la ventana
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        # dibujado de la orbita
        if (len(self.orbit)) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                # estos hacen referencia al centro del circulo
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x,y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        # mapeo del planeta
        pygame.draw.circle(win, self.color, (x, y), self.radius)
        if not self.sun: # si no es el sol entones muestra la distancia
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2)) # dibuja la distancia en el centro del circulo

    # metodo que calcuola la fuerza de atraccion
    def attraction(self, other): # other = otro planeta
        # calculamos la distancia entre dos objetos, distancia relativa
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        
        # hallamos la distancia entre un planeta a otro (pitagoras)
        distance = math.sqrt(distance_x **2 + distance_y**2)
        if other.sun:
            self.distance_to_sun = distance

        # calculamos la fuerza de atraccion
        force = self.G * self.mass * other.mass / distance ** 2

        # hallamos el angulo y los lados del triangulo generado
        teta = math.atan2(distance_y, distance_x)
        force_x = math.cos(teta) * force
        force_y = math.sin(teta) * force
        return force_x, force_y

    # calculamos la velocidad de cada planeta respecto a los otros
    # entre más cerca del sol menos velocidad tiene
    def update_position(self, planets): # iteramos por cada planeta y calculamos sus velocidcades
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet) # con los valores de retorno se define su fuerza
            total_fx += fx # las velocidades van aumentando segun la distancia de los planetas
            total_fy += fy

        # aumenta la velocidad por la aceleracion multiplicada por el tiempo
        # estructura: a = fuerza / masa * tiempo
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        # aumentamos x e y segun el tiempo
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))


# loop que mantenga la ejecucion de la ventana
def main():
    run = True
    clock = pygame.time.Clock()# setea el valor del framerate

    # dibujado del planetas, las velocidades en y son necesarias para trazar los movimientos elipticos
    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True
    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.972 * 10**24)
    earth.y_vel = 29.783 * 1000
    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000
    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000
    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    # lista de planetas
    planets =[sun, earth, mars, mercury, venus]

    while run:
        clock.tick(75)
        WIN.fill((0,0,0))
        
        #pygame.display.update() # con esto hacemos que actualice los cambios para dibujar en pantalla
        for event in pygame.event.get(): # event.get() es una lista de los eventos que suceden
            if event.type == pygame.QUIT:
                run = False
        # bucle para el dibujado de planetas
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()
    
    
    
    # solamente hemos agregado un evento que cuando le demos a la x cierre el loop
    pygame.quit()

main()