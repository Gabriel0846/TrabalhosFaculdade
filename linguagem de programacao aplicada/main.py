import pygame
import sys
from menu import show_menu
from game import game_loop

def main():
    print("Inicializando Pygame...")
    pygame.init()
    pygame.mixer.init()
    print("Pygame inicializado!")
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Shooter - Demo")
    
    while True:
        action = show_menu(screen)
        print(f"Ação do menu: {action}")  # Debug
        
        if action == "start":
            result = game_loop(screen)
            if result == "quit":
                break
        elif action == "quit":
            break
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()