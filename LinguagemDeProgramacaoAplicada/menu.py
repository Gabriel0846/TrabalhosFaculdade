import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def tocar_musica_menu():
    # tenta carregar a musica do menu (formato mp3)
    caminho = os.path.join(BASE_DIR, "assets/sounds/menu_music.mp3")
    if os.path.exists(caminho):
        try:
            pygame.mixer.music.load(caminho)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        except:
            pass

def parar_musica():
    pygame.mixer.music.stop()

def show_menu(screen):
    fonte_grande = pygame.font.Font(None, 74)
    fonte_media = pygame.font.Font(None, 36)
    fonte_pequena = pygame.font.Font(None, 24)

    tocar_musica_menu()

    # fundo da tela (se existir)
    fundo = None
    bg_path = os.path.join(BASE_DIR, "assets/images/background.jpg")
    if os.path.exists(bg_path):
        try:
            fundo = pygame.image.load(bg_path)
            fundo = pygame.transform.scale(fundo, (800, 600))
        except:
            pass

    while True:
        if fundo:
            screen.blit(fundo, (0, 0))
        else:
            screen.fill((0, 0, 50))

        titulo = fonte_grande.render("SPACE SHOOTER", True, (255, 255, 255))
        screen.blit(titulo, (800//2 - titulo.get_width()//2, 100))

        texto_iniciar = fonte_media.render("1 - INICIAR JOGO", True, (255, 255, 255))
        texto_sair = fonte_media.render("2 - SAIR", True, (255, 255, 255))
        screen.blit(texto_iniciar, (800//2 - texto_iniciar.get_width()//2, 250))
        screen.blit(texto_sair, (800//2 - texto_sair.get_width()//2, 320))

        comandos = [
            "COMANDOS:",
            "<- -> - Movimentar nave",
            "Espaco ou seta cima - Atirar",
            "ESC - Voltar ao menu",
            "P - Pausar"
        ]

        y = 480
        for cmd in comandos:
            linha = fonte_pequena.render(cmd, True, (200, 200, 200))
            screen.blit(linha, (20, y))
            y += 25

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                parar_musica()
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    parar_musica()
                    return "start"
                elif event.key == pygame.K_2:
                    parar_musica()
                    return "quit"