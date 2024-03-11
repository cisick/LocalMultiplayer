import pygame
from pygame.locals import *
import pygame.joystick
import sys
import math

pygame.init()
clock = pygame.time.Clock()

# Fenster einrichten
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('PS4 Controller Test')

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Rechtecke initialisieren
num_rectangles = 2
rectangles = []
for i in range(num_rectangles):
    rect_width = 50
    rect_height = 50
    rect_x = window_width // 2 - rect_width // 2 + i * 100
    rect_y = window_height // 2 - rect_height // 2
    rectangles.append(pygame.Rect(rect_x, rect_y, rect_width, rect_height))

# Ball initialisieren
ball_radius = 20
ball_x = window_width // 2
ball_y = window_height // 2
ball_speed = 5
ball_velocity_x = 0
ball_velocity_y = 0

# Controller initialisieren
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
if joystick_count < num_rectangles:
    print(f"Nicht genügend Joysticks gefunden. Du benötigst mindestens {num_rectangles} PS4-Controller.")
    pygame.quit()
    sys.exit()
else:
    joysticks = [pygame.joystick.Joystick(i) for i in range(num_rectangles)]
    for joystick in joysticks:
        joystick.init()

# Funktion zur Berechnung des Abstands zwischen zwei Punkten
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Hauptschleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Eingaben von den Controllern verarbeiten
    for i, joystick in enumerate(joysticks):
        axis_x = joystick.get_axis(0)
        axis_y = joystick.get_axis(1)

        # Rechteck bewegen
        rectangles[i].x += int(axis_x * 5)
        rectangles[i].y += int(axis_y * 5)

        # Begrenze die Position des Rechtecks innerhalb des Fensters
        rectangles[i].x = max(0, min(rectangles[i].x, window_width - rectangles[i].width))
        rectangles[i].y = max(0, min(rectangles[i].y, window_height - rectangles[i].height))

        # Kollisionserkennung und Reaktion
        dist = distance(ball_x, ball_y, rectangles[i].centerx, rectangles[i].centery)
        if dist < ball_radius + max(rectangles[i].width, rectangles[i].height) / 2:
            # Berechne die Richtung des Stoßes
            dx = ball_x - rectangles[i].centerx
            dy = ball_y - rectangles[i].centery
            angle = math.atan2(dy, dx)

            # Passe die Ballgeschwindigkeit entsprechend an
            ball_velocity_x = ball_speed * math.cos(angle)
            ball_velocity_y = ball_speed * math.sin(angle)

    # Bewege den Ball
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Begrenze die Position des Balls innerhalb des Fensters
    if ball_x - ball_radius < 0 or ball_x + ball_radius > window_width:
        ball_velocity_x *= -1
    if ball_y - ball_radius < 0 or ball_y + ball_radius > window_height:
        ball_velocity_y *= -1

    # Bildschirm zeichnen
    screen.fill(BLACK)
    for rectangle in rectangles:
        pygame.draw.rect(screen, WHITE, rectangle)
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)
    pygame.display.flip()

    # Bildschirm aktualisieren
    clock.tick(60)

pygame.quit()
