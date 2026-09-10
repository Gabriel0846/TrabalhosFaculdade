import pygame
import sys
from menu import show_menu
from game import game_loop

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Shooter - Demo")

    while True:
        acao = show_menu(screen)
        if acao == "start":
            pygame.mixer.music.stop()
            resultado = game_loop(screen)
            if resultado == "quit":
                break
        elif acao == "quit":
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()