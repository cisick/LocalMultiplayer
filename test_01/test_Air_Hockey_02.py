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

# Spieler initialisieren
num_players = 2
players = []
for i in range(num_players):
    player_width = 50
    player_height = 50
    player_x = window_width // 2 - player_width // 2 + i * 100
    player_y = window_height // 2 - player_height // 2
    players.append(pygame.Rect(player_x, player_y, player_width, player_height))

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
if joystick_count < num_players:
    print(f"Nicht genügend Joysticks gefunden. Du benötigst mindestens {num_players} PS4-Controller.")
    pygame.quit()
    sys.exit()
else:
    joysticks = [pygame.joystick.Joystick(i) for i in range(num_players)]
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

        # Spieler bewegen
        players[i].x += int(axis_x * 5)
        players[i].y += int(axis_y * 5)

        # Begrenze die Position des Spielers innerhalb des Fensters
        players[i].x = max(0, min(players[i].x, window_width - players[i].width))
        players[i].y = max(0, min(players[i].y, window_height - players[i].height))

        # Kollisionserkennung und Reaktion
        dist = distance(ball_x, ball_y, players[i].centerx, players[i].centery)
        if dist < ball_radius + max(players[i].width, players[i].height) / 2:
            # Berechne die Richtung des Stoßes
            dx = ball_x - players[i].centerx
            dy = ball_y - players[i].centery
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
    for player in players:
        pygame.draw.rect(screen, WHITE, player)
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)
    pygame.display.flip()

    # Bildschirm aktualisieren
    clock.tick(60)

pygame.quit()
