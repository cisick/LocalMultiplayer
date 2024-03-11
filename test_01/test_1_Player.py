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

# Rechteck initialisieren
rect_width = 50
rect_height = 50
rect_x = window_width // 2 - rect_width // 2
rect_y = window_height // 2 - rect_height // 2

# Controller initialisieren
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
if joystick_count < 1:
    print("Kein Joystick gefunden. Stelle sicher, dass dein PS4-Controller verbunden ist.")
    pygame.quit()
    sys.exit()
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

# Hauptschleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Eingaben vom Controller verarbeiten
    axis_x = joystick.get_axis(0)
    axis_y = joystick.get_axis(1)

    # Rechteck bewegen
    rect_x += int(axis_x * 5)
    rect_y += int(axis_y * 5)

    # Begrenze die Position des Rechtecks innerhalb des Fensters
    rect_x = max(0, min(rect_x, window_width - rect_width))
    rect_y = max(0, min(rect_y, window_height - rect_height))

    # Bildschirm zeichnen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()

    # Bildschirm aktualisieren
    clock.tick(60)

pygame.quit()
