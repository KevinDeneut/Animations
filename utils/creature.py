from utils.point import Point
import pygame

class Creature:
    def __init__(self, body, x, y):
        DISTANCE = 20
        self.body = body
        self.x = x
        self.y = y

        self.points = []
        for i, e in enumerate(body):
            if i == 0:
                self.points.append(Point(e, self.x / 2, self.y / 2, None, DISTANCE))
            else:
                self.points.append(Point(e, self.x / 2, self.y / 2, self.points[i-1], DISTANCE))
    
    def update(self, screen, movement_x, movement_y):
        self.points[0].change_coord(movement_x, movement_y)

        for point in self.points:
            point.update()
            point.draw_point(screen)
            # point.get_info()
    
    def pos_head(self):
        return self.points[0].get_coord()