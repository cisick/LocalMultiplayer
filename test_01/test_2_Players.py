import pygame
from pygame.locals import *
import pygame.joystick
import sys

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

# Rechtecke initialisieren
num_rectangles = 2
rectangles = []
for i in range(num_rectangles):
    rect_width = 50
    rect_height = 50
    rect_x = window_width // 2 - rect_width // 2 + i * 100
    rect_y = window_height // 2 - rect_height // 2
    rectangles.append(pygame.Rect(rect_x, rect_y, rect_width, rect_height))

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

    # Bildschirm zeichnen
    screen.fill(BLACK)
    for rectangle in rectangles:
        pygame.draw.rect(screen, WHITE, rectangle)
    pygame.display.flip()

    # Bildschirm aktualisieren
    clock.tick(60)

pygame.quit()
