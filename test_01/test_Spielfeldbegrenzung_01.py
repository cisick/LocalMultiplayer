import pygame
import sys

# Initialisierung von Pygame
pygame.init()

# Definieren einiger Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definieren der Bildschirmgröße
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Erstellen des Bildschirms
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Spielfeldbegrenzung")

# Funktion zum Zeichnen der Begrenzungen
def draw_boundaries():
    # Zeichnen von Rechtecken
    pygame.draw.rect(screen, WHITE, (50, 50, 700, 500), 2)  # Äußeres Rechteck
    pygame.draw.rect(screen, WHITE, (150, 150, 500, 300), 2)  # Inneres Rechteck

    # Zeichnen von Kreisen
    pygame.draw.circle(screen, WHITE, (400, 300), 200, 2)  # Großer Kreis
    pygame.draw.circle(screen, WHITE, (400, 300), 100, 2)  # Kleiner Kreis

# Hauptfunktion des Spiels
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)  # Bildschirm mit Schwarz füllen
        draw_boundaries()   # Begrenzungen zeichnen
        pygame.display.flip()  # Bildschirm aktualisieren

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
