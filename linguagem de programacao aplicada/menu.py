import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def play_menu_music():
    """Toca música do menu (MP3)"""
    music_path = os.path.join(BASE_DIR, "assets/sounds/menu_music.mp3")
    
    if os.path.exists(music_path):
        try:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            print(f"Tocando música do menu: {music_path}")
        except Exception as e:
            print(f"Erro ao carregar música: {e}")
    else:
        print(f"Música não encontrada: {music_path}")

def stop_music():
    pygame.mixer.music.stop()

def show_menu(screen):
    font_large = pygame.font.Font(None, 74)
    font_medium = pygame.font.Font(None, 36)
    font_small = pygame.font.Font(None, 24)
    
    # Toca música do menu
    play_menu_music()
    
    # Tenta carregar fundo
    background = None
    bg_path = os.path.join(BASE_DIR, "assets/images/background.jpg")
    if os.path.exists(bg_path):
        try:
            background = pygame.image.load(bg_path)
            background = pygame.transform.scale(background, (800, 600))
        except:
            pass
    
    while True:
        if background:
            screen.blit(background, (0, 0))
        else:
            screen.fill((0, 0, 50))
        
        title = font_large.render("SPACE SHOOTER", True, (255, 255, 255))
        screen.blit(title, (800//2 - title.get_width()//2, 100))
        
        start_text = font_medium.render("1 - INICIAR JOGO", True, (255, 255, 255))
        quit_text = font_medium.render("2 - SAIR", True, (255, 255, 255))
        screen.blit(start_text, (800//2 - start_text.get_width()//2, 250))
        screen.blit(quit_text, (800//2 - quit_text.get_width()//2, 320))
        
        commands = [
            "COMANDOS:",
            "← → - Movimentar nave",
            "Espaço ou ↑ - Atirar",
            "ESC - Voltar ao menu",
            "P - Pausar"
        ]
        
        y_offset = 480
        for cmd in commands:
            cmd_surface = font_small.render(cmd, True, (200, 200, 200))
            screen.blit(cmd_surface, (20, y_offset))
            y_offset += 25
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_music()
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    stop_music()  # Para a música do menu
                    return "start"
                elif event.key == pygame.K_2:
                    stop_music()
                    return "quit"