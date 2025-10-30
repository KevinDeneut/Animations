import pygame
import math

BLACK = (0,0,0)
WHITE = (255,255,255)

class Point:
    def __init__(self, radius, x, y, predecessor, distance):
        if predecessor != None:
            self.x = predecessor.get_coord()[0] + distance
        else:
            self.x = x

        self.radius = radius
        self.y = y
        self.predecessor = predecessor
        self.distance = distance

    def get_coord(self):
        return (self.x, self.y)
    
    def get_pred(self):
        return self.predecessor
    
    def change_coord(self, x, y):
        self.x += x
        self.y += y

    def get_info(self):
        print("x= " + str(self.x) + " | y= " + str(self.y) + " | pred= " + str(self.predecessor))
        # print(self.x)

    def update(self):
        if self.predecessor == None:
            return

        (x_pred, y_pred) = self.predecessor.get_coord() 

        dx = self.x - x_pred
        dy = self.y - y_pred
        distance = math.hypot(dx, dy)

        if distance == 0:
            self.x = x_pred - self.distance
            self.y = y_pred
            return

        if abs(distance - self.distance) > 1e-5:
            self.x = (dx * self.distance / distance) + x_pred
            self.y = (dy * self.distance / distance) + y_pred
        
    def draw_point(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)