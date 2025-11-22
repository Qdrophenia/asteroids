import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vector_1 = self.velocity.rotate(angle)
            vector_2 = self.velocity.rotate(0 - angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            child_asteroid_1.velocity = vector_1 * 1.2
            child_asteroid_2.velocity = vector_2 * 1.2