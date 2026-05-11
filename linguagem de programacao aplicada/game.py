import pygame
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class GerenciadorRecursos:
    # carrega imagens e sons, sem firulas
    @staticmethod
    def load_image(path, size=None):
        caminho = os.path.join(BASE_DIR, path)
        if os.path.exists(caminho):
            try:
                img = pygame.image.load(caminho)
                if size:
                    img = pygame.transform.scale(img, size)
                return img, True
            except:
                return None, False
        return None, False

    @staticmethod
    def load_sound(path, volume=0.3):
        caminho = os.path.join(BASE_DIR, path)
        if os.path.exists(caminho):
            try:
                som = pygame.mixer.Sound(caminho)
                som.set_volume(volume)
                return som, True
            except:
                return None, False
        return None, False

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 50
        self.altura = 50
        self.velocidade = 5
        self.vidas = 3
        self.invencivel_timer = 0
        self.tiro_timer = 0
        self.tiro_duplo = False
        self.tiro_duplo_timer = 0

        self.imagem, self.tem_imagem = GerenciadorRecursos.load_image("assets/images/player.png", (self.largura, self.altura))

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.x < 750:
            self.x += self.velocidade

        if self.invencivel_timer > 0:
            self.invencivel_timer -= 1
        if self.tiro_duplo_timer > 0:
            self.tiro_duplo_timer -= 1
        else:
            self.tiro_duplo = False

    def atirar(self, som_tiro):
        if self.tiro_timer <= 0:
            self.tiro_timer = 15
            if som_tiro:
                som_tiro.play()
            balas = []
            if self.tiro_duplo:
                balas.append(Bullet(self.x + 10, self.y, "player"))
                balas.append(Bullet(self.x + 40, self.y, "player"))
            else:
                balas.append(Bullet(self.x + 25, self.y, "player"))
            return balas
        return []

    def sofrer_dano(self, som_morte=None):
        if self.invencivel_timer <= 0:
            self.vidas -= 1
            self.invencivel_timer = 60
            if som_morte and self.vidas > 0:
                som_morte.play()
            return True
        return False

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, tela):
        if self.tem_imagem:
            if self.invencivel_timer > 0 and self.invencivel_timer % 6 < 3:
                return
            tela.blit(self.imagem, (self.x, self.y))
        else:
            if self.invencivel_timer > 0 and self.invencivel_timer % 6 < 3:
                return
            # fallback: nave verde geometrica
            pygame.draw.polygon(tela, (0, 255, 0), [
                (self.x + 25, self.y),
                (self.x + 10, self.y + 40),
                (self.x + 25, self.y + 30),
                (self.x + 40, self.y + 40)
            ])

class Bullet:
    def __init__(self, x, y, atirador):
        self.x = x
        self.y = y
        self.largura = 4
        self.altura = 10
        self.velocidade = 8 if atirador == "player" else 5
        self.atirador = atirador
        self.imagem, self.tem_imagem = GerenciadorRecursos.load_image("assets/images/bullet.png", (self.largura, self.altura))

    def mover(self):
        if self.atirador == "player":
            self.y -= self.velocidade
        else:
            self.y += self.velocidade

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, tela):
        if self.tem_imagem:
            tela.blit(self.imagem, (self.x, self.y))
        else:
            cor = (255, 255, 0) if self.atirador == "player" else (255, 0, 0)
            pygame.draw.rect(tela, cor, (self.x, self.y, self.largura, self.altura))

class Enemy:
    def __init__(self, x, y, tipo="normal"):
        self.x = x
        self.y = y
        self.tipo = tipo

        config = {
            "normal": {"largura": 40, "altura": 40, "vel": 2, "vidas": 1, "img": "assets/images/enemy_normal.png"},
            "fast": {"largura": 30, "altura": 30, "vel": 4, "vidas": 1, "img": "assets/images/enemy_fast.png"},
            "tank": {"largura": 50, "altura": 50, "vel": 1, "vidas": 3, "img": "assets/images/enemy_tank.png"}
        }
        c = config.get(tipo, config["normal"])
        self.largura = c["largura"]
        self.altura = c["altura"]
        self.velocidade = c["vel"]
        self.vidas = c["vidas"]
        self.imagem, self.tem_imagem = GerenciadorRecursos.load_image(c["img"], (self.largura, self.altura))

    def mover(self):
        self.y += self.velocidade

    def tomar_dano(self):
        self.vidas -= 1
        return self.vidas <= 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, tela):
        if self.tem_imagem:
            tela.blit(self.imagem, (self.x, self.y))
        else:
            cores = {"normal": (255,0,0), "fast": (255,100,0), "tank": (150,0,150)}
            pygame.draw.rect(tela, cores.get(self.tipo, (255,0,0)), (self.x, self.y, self.largura, self.altura))

class PowerUp:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.largura = 20
        self.altura = 20
        self.velocidade = 3
        self.tipo = tipo

        mapa = {
            "double": "assets/images/powerup_double.png",
            "life": "assets/images/powerup_life.png",
            "speed": "assets/images/powerup_speed.png"
        }
        self.imagem, self.tem_imagem = GerenciadorRecursos.load_image(mapa.get(tipo, ""), (self.largura, self.altura))

    def mover(self):
        self.y += self.velocidade

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, tela):
        if self.tem_imagem:
            tela.blit(self.imagem, (self.x, self.y))
        else:
            cores = {"double": (0,255,255), "life": (255,0,255), "speed": (0,255,0)}
            pygame.draw.rect(tela, cores.get(self.tipo, (255,255,255)), (self.x, self.y, self.largura, self.altura))

class Boss:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 100
        self.altura = 100
        self.vidas = 20
        self.vidas_max = 20
        self.velocidade = 1
        self.direcao = 1
        self.timer_tiro = 0
        self.imagem, self.tem_imagem = GerenciadorRecursos.load_image("assets/images/boss.png", (self.largura, self.altura))

    def mover(self):
        self.x += self.velocidade * self.direcao
        if self.x <= 50 or self.x >= 650:
            self.direcao *= -1
            self.y += 30

    def atirar(self, som_tiro):
        if self.timer_tiro <= 0:
            self.timer_tiro = 60
            if som_tiro:
                som_tiro.play()
            return Bullet(self.x + 50, self.y + 80, "boss")
        return None

    def tomar_dano(self):
        self.vidas -= 1
        return self.vidas <= 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, tela):
        # barra de vida
        largura_barra = 200
        altura_barra = 15
        percentual = self.vidas / self.vidas_max
        pygame.draw.rect(tela, (100,0,0), (self.x + 50 - largura_barra//2, self.y - 25, largura_barra, altura_barra))
        pygame.draw.rect(tela, (0,255,0), (self.x + 50 - largura_barra//2, self.y - 25, largura_barra * percentual, altura_barra))

        if self.tem_imagem:
            tela.blit(self.imagem, (self.x, self.y))
        else:
            pygame.draw.rect(tela, (200,0,0), (self.x, self.y, self.largura, self.altura))

def tocar_musica(tipo):
    """toca musica de fundo (mp3)"""
    arquivos = {
        "boss": "assets/sounds/boss_music.mp3",
        "victory": "assets/sounds/victory_music.mp3",
        "game": "assets/sounds/menu_music.mp3",
        "gameover": "assets/sounds/gameover.mp3"
    }
    caminho = arquivos.get(tipo)
    if caminho:
        completo = os.path.join(BASE_DIR, caminho)
        if os.path.exists(completo):
            try:
                pygame.mixer.music.load(completo)
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)
            except:
                pass

def parar_musica():
    pygame.mixer.music.stop()

def game_loop(tela):
    relogio = pygame.time.Clock()

    # carrega os efeitos sonoros (todos .mp3)
    som_tiro, _ = GerenciadorRecursos.load_sound("assets/sounds/shoot.mp3", 0.3)
    som_tiro_inimigo, _ = GerenciadorRecursos.load_sound("assets/sounds/enemy_shoot.mp3", 0.3)
    som_morte, _ = GerenciadorRecursos.load_sound("assets/sounds/death.mp3", 0.5)
    som_powerup, _ = GerenciadorRecursos.load_sound("assets/sounds/powerup.mp3", 0.4)
    som_explosao, _ = GerenciadorRecursos.load_sound("assets/sounds/explosion.mp3", 0.5)

    jogador = Player(375, 520)
    balas = []
    inimigos = []
    powerups = []
    balas_inimigas = []
    boss = None

    pontos = 0
    inimigos_para_spawn = 10
    estado = "playing"  # playing, boss, victory, gameover
    pausado = False
    morte_tocada = False

    fonte = pygame.font.Font(None, 36)
    fonte_grande = pygame.font.Font(None, 72)

    tocar_musica("game")

    # spawn inicial
    for _ in range(5):
        tipo = random.choice(["normal", "fast", "tank"])
        inimigos.append(Enemy(random.randint(50, 750), random.randint(-200, -50), tipo))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                parar_musica()
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    parar_musica()
                    return "menu"
                if event.key == pygame.K_p:
                    pausado = not pausado
                if estado in ("victory", "gameover"):
                    if event.key == pygame.K_r:
                        parar_musica()
                        return "start"
                    if event.key == pygame.K_ESCAPE:
                        parar_musica()
                        return "menu"

        if pausado:
            txt_pausa = fonte_grande.render("PAUSED", True, (255,255,255))
            tela.blit(txt_pausa, (800//2 - txt_pausa.get_width()//2, 300))
            pygame.display.flip()
            relogio.tick(60)
            continue

        teclas = pygame.key.get_pressed()
        jogador.mover(teclas)

        if teclas[pygame.K_SPACE] or teclas[pygame.K_UP]:
            novas_balas = jogador.atirar(som_tiro)
            balas.extend(novas_balas)

        if jogador.tiro_timer > 0:
            jogador.tiro_timer -= 1

        for b in balas[:]:
            b.mover()
            if b.y < 0 or b.y > 600:
                balas.remove(b)

        if estado == "playing":
            if len(inimigos) < 5 and inimigos_para_spawn > 0:
                tipo = random.choice(["normal", "fast", "tank"])
                inimigos.append(Enemy(random.randint(50,750), random.randint(-200,-50), tipo))
                inimigos_para_spawn -= 1

            if len(inimigos) == 0 and inimigos_para_spawn == 0:
                estado = "boss"
                boss = Boss(350, 50)
                tocar_musica("boss")
                morte_tocada = False

            for inimigo in inimigos[:]:
                inimigo.mover()
                if inimigo.y > 650:
                    inimigos.remove(inimigo)

                for bala in balas[:]:
                    if bala.atirador == "player" and inimigo.get_rect().colliderect(bala.get_rect()):
                        balas.remove(bala)
                        if inimigo.tomar_dano():
                            inimigos.remove(inimigo)
                            pontos += 10
                            if som_explosao:
                                som_explosao.play()
                            if random.random() < 0.3:
                                tipo_pw = random.choice(["double", "life", "speed"])
                                powerups.append(PowerUp(inimigo.x, inimigo.y, tipo_pw))
                        break

                if jogador.get_rect().colliderect(inimigo.get_rect()):
                    jogador.sofrer_dano(som_morte if jogador.vidas > 1 else None)
                    if jogador.vidas <= 0:
                        estado = "gameover"
                    inimigos.remove(inimigo)

        elif estado == "boss":
            if boss:
                boss.mover()
                bala_boss = boss.atirar(som_tiro_inimigo)
                if bala_boss:
                    balas_inimigas.append(bala_boss)
                if boss.timer_tiro > 0:
                    boss.timer_tiro -= 1

                for bala in balas[:]:
                    if bala.atirador == "player" and boss.get_rect().colliderect(bala.get_rect()):
                        balas.remove(bala)
                        if boss.tomar_dano():
                            estado = "victory"
                            pontos += 100
                            tocar_musica("victory")
                            if som_explosao:
                                som_explosao.play()
                        break

                if jogador.get_rect().colliderect(boss.get_rect()):
                    jogador.sofrer_dano(som_morte if jogador.vidas > 1 else None)
                    if jogador.vidas <= 0:
                        estado = "gameover"

        for pw in powerups[:]:
            pw.mover()
            if pw.y > 600:
                powerups.remove(pw)
            elif jogador.get_rect().colliderect(pw.get_rect()):
                if som_powerup:
                    som_powerup.play()
                if pw.tipo == "double":
                    jogador.tiro_duplo = True
                    jogador.tiro_duplo_timer = 600
                elif pw.tipo == "life":
                    jogador.vidas = min(jogador.vidas + 1, 5)
                elif pw.tipo == "speed":
                    jogador.velocidade = min(jogador.velocidade + 1, 8)
                powerups.remove(pw)

        for bala_inim in balas_inimigas[:]:
            bala_inim.mover()
            if bala_inim.y > 600:
                balas_inimigas.remove(bala_inim)
            elif jogador.get_rect().colliderect(bala_inim.get_rect()):
                balas_inimigas.remove(bala_inim)
                jogador.sofrer_dano(som_morte if jogador.vidas > 1 else None)
                if jogador.vidas <= 0:
                    estado = "gameover"

        # fundo
        tela.fill((0, 0, 30))
        for _ in range(100):
            pygame.draw.circle(tela, (100,100,150), (random.randint(0,800), random.randint(0,600)), 1)

        jogador.desenhar(tela)
        for b in balas:
            b.desenhar(tela)
        for inim in inimigos:
            inim.desenhar(tela)
        for pw in powerups:
            pw.desenhar(tela)
        for bi in balas_inimigas:
            bi.desenhar(tela)
        if boss:
            boss.desenhar(tela)

        # interface
        texto_pontos = fonte.render(f"Score: {pontos}", True, (255,255,255))
        texto_vidas = fonte.render(f"Lives: {jogador.vidas}", True, (255,255,255))
        tela.blit(texto_pontos, (10,10))
        tela.blit(texto_vidas, (10,50))

        if jogador.tiro_duplo:
            txt_pw = fonte.render("DOUBLE SHOT!", True, (0,255,255))
            tela.blit(txt_pw, (10,90))

        if estado == "victory":
            venceu = fonte_grande.render("VICTORY!", True, (255,255,0))
            reiniciar = fonte.render("Press R to restart or ESC to menu", True, (255,255,255))
            tela.blit(venceu, (800//2 - venceu.get_width()//2, 250))
            tela.blit(reiniciar, (800//2 - reiniciar.get_width()//2, 350))

        if estado == "gameover":
            if not morte_tocada and som_morte:
                som_morte.play()
                morte_tocada = True
                parar_musica()
                tocar_musica("gameover")

            gameover_txt = fonte_grande.render("GAME OVER", True, (255,0,0))
            reiniciar = fonte.render("Press R to restart or ESC to menu", True, (255,255,255))
            tela.blit(gameover_txt, (800//2 - gameover_txt.get_width()//2, 250))
            tela.blit(reiniciar, (800//2 - reiniciar.get_width()//2, 350))

        pygame.display.flip()
        relogio.tick(60)