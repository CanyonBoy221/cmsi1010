# Enhancement #1
# Runway with moving centerline and stripes on sides, appears when you get close to the ground

# Enhancement #2
# Sky, really cool AI made sky

# Enhancement #3
# Trees that Unfortunately change as you move across the screen but they are still there.

# Enhancement #4
# Speed tracker that tracks the planes speed and you can move up and down

# Enhancement #5
# Altitude tracker that tracks the planes altitude

# Enhancement #6
# Added the ability to go past the max speed of 23

# Enhancement #7
# Added the plane falling out of the sky if the speed is 0

import math
import random
from dataclasses import dataclass
import pygame

WIDTH, HEIGHT = 1024, 600
SKY_COLOR = (135, 240, 255)
GRASS_COLOR = (128, 255, 100)
GRASS_HEIGHT = 100
GRASS_TOP = HEIGHT - GRASS_HEIGHT
GRASS_RECTANGLE = (0, GRASS_TOP, WIDTH, GRASS_HEIGHT)
GROUND_LEVEL = HEIGHT - (GRASS_HEIGHT // 2)
TREE_SPACING = 173
MAX_PLANE_SPEED = 23
CRUISING_ALTITUDE = 50

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plane Landing")
clock = pygame.time.Clock()
background = pygame.transform.scale(
    pygame.image.load("background.jpg"), (WIDTH, HEIGHT))
tree_images = [
    pygame.transform.scale(pygame.image.load("tree1.png"), (60, 80)),
    pygame.transform.scale(pygame.image.load("tree2.png"), (60, 80)),
    pygame.transform.scale(pygame.image.load("tree3.png"), (60, 80)),
    pygame.transform.scale(pygame.image.load("tree4.png"), (60, 80))
]
# I tried really hard to not have the trees change while they went across the screen, but I could not figure it out. So I just left them changing becuase it still looked cool
# Dictionary to store which tree type each position uses
tree_types = {}
font = pygame.font.Font(None, 36)


@dataclass
class Plane:
    x: int
    y: int
    state: str = "flying"
    speed: int = MAX_PLANE_SPEED
    rotation: int = 0
    color: tuple = (255, 255, 255)

    def draw(self):
        base_coords = [
            (-16, 0), (-13, 2), (-15, 7), (-12, 7), (-8, 2), (-1, 2),
            (-6, 6), (-5, 6), (8, 2), (16, 2), (19, -2), (8, -2),
            (-5, -8), (-6, -8), (-1, -2), (-13, -2)]
        rotated = base_coords if self.rotation == 0 else [
            (x * math.cos(self.rotation) - y * math.sin(self.rotation),
             x * math.sin(self.rotation) + y * math.cos(self.rotation))
            for x, y in base_coords]
        coords = [(WIDTH//2 + 4*x, self.y - 4*y) for x, y in rotated]
        pygame.draw.polygon(screen, self.color, coords)

    def move(self):

        if self.speed == 0 and self.y < GROUND_LEVEL and self.state not in ["stopped", "braking", "down", "touching", "crashed"]:

            self.y += 10
            if self.y >= GROUND_LEVEL:
                self.y = GROUND_LEVEL
            self.state = "crashed"
            self.color = (255, 0, 0)
            self.speed = 0

        if self.state != "stopped" and self.state != "crashed":
            self.x += self.speed % TREE_SPACING
        if self.state == "flying":
            pass
        elif self.state == "descending":
            self.y += self.speed * 0.1
            if self.y >= GROUND_LEVEL:
                self.state = "crashed"
                self.color = (255, 0, 0)
                self.speed = 0
                self.y = GROUND_LEVEL
        elif self.state == "landing":
            self.y += self.speed * 0.1
            if self.y >= GROUND_LEVEL:
                self.state = "touching"
                self.y = GROUND_LEVEL
        elif self.state == "touching":
            pass
        elif self.state == "down":
            pass
        elif self.state == "braking":
            self.speed -= 0.1
            if self.speed <= 0:
                self.speed = 0
                self.state = "stopped"
        elif self.state == "starting":
            self.y = GROUND_LEVEL
            self.speed += 0.1
            if self.speed >= MAX_PLANE_SPEED:
                self.speed = MAX_PLANE_SPEED
        elif self.state == "rising":
            self.y -= self.speed * 0.1
            if self.y <= CRUISING_ALTITUDE:
                self.y = CRUISING_ALTITUDE
                self.state = "flying"
                self.rotation = 0
        elif self.state == "crashed":

            if self.y < GROUND_LEVEL:
                self.y += 15
            else:
                self.y = GROUND_LEVEL


plane = Plane(0, y=CRUISING_ALTITUDE)


def draw_tree(x, y, world_pos):

    tree_id = f"tree_{world_pos}"

    if tree_id not in tree_types:

        tree_slot = int(world_pos) // TREE_SPACING
        tree_type = tree_slot % 4
        tree_types[tree_id] = tree_type

    tree_index = int(tree_types[tree_id])
    screen.blit(tree_images[tree_index], (x - 30, y - 80))


def draw_runway():

    altitude = GROUND_LEVEL - plane.y
    if altitude > 150:
        return

    progress = max(0, (150 - altitude) / 150)
    runway_width = int(WIDTH * progress)
    runway_y = GROUND_LEVEL - 25
    runway_height = 50

    runway_x = WIDTH - runway_width

    pygame.draw.rect(screen, (60, 60, 60),
                     (runway_x, runway_y, runway_width, runway_height))

    stripe_height = 2
    pygame.draw.rect(screen, (255, 255, 255),
                     (runway_x, runway_y, runway_width, stripe_height))
    pygame.draw.rect(screen, (255, 255, 255),
                     (runway_x, runway_y + runway_height - stripe_height, runway_width, stripe_height))

    dot_width = 20
    dot_height = 4
    dot_spacing = 40
    centerline_y = runway_y + runway_height // 2 - dot_height // 2

    offset = int(plane.x) % dot_spacing

    for i in range(-dot_spacing, WIDTH + dot_spacing, dot_spacing):
        dot_x = i - offset
        if dot_x >= runway_x and dot_x + dot_width <= runway_x + runway_width:
            pygame.draw.rect(screen, (255, 255, 0),
                             (dot_x, centerline_y, dot_width, dot_height))


def draw_scene():
    if plane.state != "stopped":
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, GRASS_COLOR, GRASS_RECTANGLE)

        altitude = GROUND_LEVEL - plane.y
        if altitude <= 250 and plane.state != "crashed":
            draw_runway()

        x = -plane.x
        tree_world_pos = ((plane.x // TREE_SPACING) - 1) * TREE_SPACING
        while x < WIDTH:
            draw_tree(x, GRASS_TOP, tree_world_pos)
            x += TREE_SPACING
            tree_world_pos += TREE_SPACING
        plane.draw()
        plane.move()

        altitude = GROUND_LEVEL - plane.y
        speed_text = font.render(
            f"Speed: {plane.speed:.1f}", True, (255, 255, 255))
        altitude_text = font.render(
            f"Altitude: {altitude:.0f}", True, (255, 255, 255))
        screen.blit(speed_text, (10, 10))
        screen.blit(altitude_text, (10, 50))

    clock.tick(60)
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and plane.state == "flying":
                plane.rotation = -0.2
                plane.state = "descending"
            elif event.key == pygame.K_UP and plane.state == "descending":
                plane.rotation = 0.2
                if plane.y < GROUND_LEVEL - 100:
                    plane.state = "rising"
                else:
                    plane.state = "landing"
            elif event.key == pygame.K_DOWN and plane.state == "touching":
                plane.rotation = 0
                plane.state = "down"
            elif event.key == pygame.K_RETURN and plane.state == "down":
                plane.state = "braking"
            elif event.key == pygame.K_RIGHT and plane.state == "stopped":
                plane.state = "starting"
            elif event.key == pygame.K_LEFT and plane.state == "flying":
                plane.speed = plane.speed - 1
            elif event.key == pygame.K_RIGHT and plane.state == "flying":
                plane.speed = plane.speed + 1
            elif event.key == pygame.K_UP and plane.state == "starting" \
                    and plane.speed == MAX_PLANE_SPEED:
                plane.rotation = 0.1
                plane.state = "rising"
    draw_scene()
