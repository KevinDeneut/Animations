from utils.point import Point
import pygame
import sys

pygame.init()

# CONSTANTEN
WIDTH = 800
HEIGHT = 500
RADIUS = 5
DISTANCE = 20
MOVE_SPEED = 1
MAX_SPEED = 5
#-----------

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
running = True

points = []
creature = [18,23,25,25,23,20,18,15,11,6,4,2,1]

for i, e in enumerate(creature):
    if i == 0:
        points.append(Point(e, WIDTH / 2, HEIGHT / 2, None, DISTANCE))
    else:
        points.append(Point(e, WIDTH / 2, HEIGHT / 2, points[i-1], DISTANCE))

movement_x = 0
movement_y = 0

while running:
    screen.fill((0,0,0))
    keys = pygame.key.get_pressed()
    movement_x *= 0.95
    movement_y *= 0.95

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                prev_point = points[-1]
                points.append(Point(RADIUS, prev_point.get_coord()[0], prev_point.get_coord()[1], prev_point, DISTANCE))
                print("Point created!")
                print(points)
                points[1].get_info()

    if keys[pygame.K_LEFT] and movement_x > -MAX_SPEED:
        movement_x -= MOVE_SPEED
    if keys[pygame.K_RIGHT] and movement_x < MAX_SPEED:
        movement_x += MOVE_SPEED
    if keys[pygame.K_UP] and movement_y > -MAX_SPEED:
        movement_y -= MOVE_SPEED
    if keys[pygame.K_DOWN] and movement_y < MAX_SPEED:
        movement_y += MOVE_SPEED

    points[0].change_coord(movement_x, movement_y)


    points[0].draw_point(screen)
    if len(points) > 1:
        for point in points[1:]:
            point.update()
            point.draw_point(screen)
            # point.get_info()

    pygame.display.flip()
    clock.tick(60)