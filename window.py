from utils.point import Point
from utils.creature import Creature
import pygame
import sys
import math

pygame.init()

# CONSTANTEN
WIDTH = 800
HEIGHT = 500
RADIUS = 5
DISTANCE = 20
MOVE_SPEED = 1
MAX_SPEED = 4
#-----------

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
running = True

creature1 = [18,23,25,25,23,20,18,15,11,6,4,2,1]
creature2 = [18,5,20,25,25,20,5,5,5,5,5,5]

movement_x = 0
movement_y = 0

creatures = [Creature([18,23,25,25,23,20,18,15,11,6,4,2,1], WIDTH / 2, HEIGHT / 2)]
# creatures = [Creature([20,20], WIDTH / 2, HEIGHT / 2)]

while running:
    screen.fill((0,0,0))

    keys = pygame.key.get_pressed()
    movement_x *= 0.95
    movement_y *= 0.95
    movement = math.sqrt(pow(movement_x, 2) + pow(movement_y, 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # if movement < MAX_SPEED:
    #     mouse_pos = pygame.mouse.get_pos()
    #     pos_creature = creatures[0].pos_head()
    #     dx = mouse_pos[0] - pos_creature[0]
    #     dy = mouse_pos[1] - pos_creature[1]
    #     if abs(dx) > 1e-5:
    #         movement_x += math.copysign(1, dx) * MOVE_SPEED
    #     if abs(dy) > 1e-5:
    #         movement_y += math.copysign(1, dy) * MOVE_SPEED

    if keys[pygame.K_LEFT] and movement < MAX_SPEED:
        movement_x -= MOVE_SPEED
    if keys[pygame.K_RIGHT] and movement < MAX_SPEED:
        movement_x += MOVE_SPEED
    if keys[pygame.K_UP] and movement < MAX_SPEED:
        movement_y -= MOVE_SPEED
    if keys[pygame.K_DOWN] and movement < MAX_SPEED:
        movement_y += MOVE_SPEED

    for creature in creatures:
        creature.update(screen, movement_x, movement_y)

    pygame.display.flip()
    clock.tick(60)