import pygame
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class ResourceManager:
    """Gerencia carregamento de imagens e sons"""
    
    @staticmethod
    def load_image(path, size=None):
        full_path = os.path.join(BASE_DIR, path)
        if os.path.exists(full_path):
            try:
                img = pygame.image.load(full_path)
                if size:
                    img = pygame.transform.scale(img, size)
                return img, True
            except Exception as e:
                print(f"Erro ao carregar imagem {full_path}: {e}")
                return None, False
        return None, False
    
    @staticmethod
    def load_sound(path, volume=0.3):
        full_path = os.path.join(BASE_DIR, path)
        if os.path.exists(full_path):
            try:
                # Para MP3, usa mixer.Sound
                sound = pygame.mixer.Sound(full_path)
                sound.set_volume(volume)
                print(f"Som carregado: {full_path}")
                return sound, True
            except Exception as e:
                print(f"Erro ao carregar som {full_path}: {e}")
                return None, False
        print(f"Som não encontrado: {full_path}")
        return None, False

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 5
        self.lives = 3
        self.invincible_timer = 0
        self.shoot_timer = 0
        self.double_shot = False
        self.double_shot_timer = 0
        
        self.image, self.has_image = ResourceManager.load_image("assets/images/player.png", (self.width, self.height))
        
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < 750:
            self.x += self.speed
            
        if self.invincible_timer > 0:
            self.invincible_timer -= 1
            
        if self.double_shot_timer > 0:
            self.double_shot_timer -= 1
        else:
            self.double_shot = False
            
    def shoot(self, shoot_sound):
        if self.shoot_timer <= 0:
            self.shoot_timer = 15
            if shoot_sound:
                shoot_sound.play()
            bullets = []
            if self.double_shot:
                bullets.append(Bullet(self.x + 10, self.y, "player"))
                bullets.append(Bullet(self.x + 40, self.y, "player"))
            else:
                bullets.append(Bullet(self.x + 25, self.y, "player"))
            return bullets
        return []
    
    def hit(self, death_sound=None):
        if self.invincible_timer <= 0:
            self.lives -= 1
            self.invincible_timer = 60
            if death_sound and self.lives > 0:
                death_sound.play()
            return True
        return False
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        if self.has_image:
            if self.invincible_timer > 0 and self.invincible_timer % 6 < 3:
                return
            screen.blit(self.image, (self.x, self.y))
        else:
            if self.invincible_timer > 0 and self.invincible_timer % 6 < 3:
                return
            pygame.draw.polygon(screen, (0, 255, 0), [
                (self.x + 25, self.y),
                (self.x + 10, self.y + 40),
                (self.x + 25, self.y + 30),
                (self.x + 40, self.y + 40)
            ])

class Bullet:
    def __init__(self, x, y, shooter):
        self.x = x
        self.y = y
        self.width = 4
        self.height = 10
        self.speed = 8 if shooter == "player" else 5
        self.shooter = shooter
        self.image, self.has_image = ResourceManager.load_image("assets/images/bullet.png", (self.width, self.height))
        
    def move(self):
        if self.shooter == "player":
            self.y -= self.speed
        else:
            self.y += self.speed
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        if self.has_image:
            screen.blit(self.image, (self.x, self.y))
        else:
            color = (255, 255, 0) if self.shooter == "player" else (255, 0, 0)
            pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))

class Enemy:
    def __init__(self, x, y, enemy_type="normal"):
        self.x = x
        self.y = y
        self.enemy_type = enemy_type
        
        enemy_config = {
            "normal": {"width": 40, "height": 40, "speed": 2, "lives": 1, "image": "assets/images/enemy_normal.png"},
            "fast": {"width": 30, "height": 30, "speed": 4, "lives": 1, "image": "assets/images/enemy_fast.png"},
            "tank": {"width": 50, "height": 50, "speed": 1, "lives": 3, "image": "assets/images/enemy_tank.png"}
        }
        
        config = enemy_config.get(enemy_type, enemy_config["normal"])
        self.width = config["width"]
        self.height = config["height"]
        self.speed = config["speed"]
        self.lives = config["lives"]
        
        self.image, self.has_image = ResourceManager.load_image(config["image"], (self.width, self.height))
        
    def move(self):
        self.y += self.speed
        
    def hit(self):
        self.lives -= 1
        return self.lives <= 0
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        if self.has_image:
            screen.blit(self.image, (self.x, self.y))
        else:
            colors = {"normal": (255, 0, 0), "fast": (255, 100, 0), "tank": (150, 0, 150)}
            pygame.draw.rect(screen, colors.get(self.enemy_type, (255, 0, 0)), (self.x, self.y, self.width, self.height))

class PowerUp:
    def __init__(self, x, y, power_type):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.speed = 3
        self.power_type = power_type
        
        image_map = {
            "double": "assets/images/powerup_double.png",
            "life": "assets/images/powerup_life.png",
            "speed": "assets/images/powerup_speed.png"
        }
        self.image, self.has_image = ResourceManager.load_image(image_map.get(power_type, ""), (self.width, self.height))
        
    def move(self):
        self.y += self.speed
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        if self.has_image:
            screen.blit(self.image, (self.x, self.y))
        else:
            colors = {"double": (0, 255, 255), "life": (255, 0, 255), "speed": (0, 255, 0)}
            pygame.draw.rect(screen, colors.get(self.power_type, (255, 255, 255)), (self.x, self.y, self.width, self.height))

class Boss:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.lives = 20
        self.max_lives = 20
        self.speed = 1
        self.direction = 1
        self.shoot_timer = 0
        
        self.image, self.has_image = ResourceManager.load_image("assets/images/boss.png", (self.width, self.height))
        
    def move(self):
        self.x += self.speed * self.direction
        if self.x <= 50 or self.x >= 650:
            self.direction *= -1
            self.y += 30
            
    def shoot(self, shoot_sound):
        if self.shoot_timer <= 0:
            self.shoot_timer = 60
            if shoot_sound:
                shoot_sound.play()
            return Bullet(self.x + 50, self.y + 80, "boss")
        return None
        
    def hit(self):
        self.lives -= 1
        return self.lives <= 0
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        bar_width = 200
        bar_height = 15
        life_percent = self.lives / self.max_lives
        
        pygame.draw.rect(screen, (100, 0, 0), (self.x + 50 - bar_width//2, self.y - 25, bar_width, bar_height))
        pygame.draw.rect(screen, (0, 255, 0), (self.x + 50 - bar_width//2, self.y - 25, bar_width * life_percent, bar_height))
        
        if self.has_image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, (200, 0, 0), (self.x, self.y, self.width, self.height))

def play_music(music_type):
    """Toca música do jogo (MP3)"""
    music_files = {
        "boss": "assets/sounds/boss_music.mp3",
        "victory": "assets/sounds/victory_music.mp3",
        "game": "assets/sounds/menu_music.mp3",
        "gameover": "assets/sounds/gameover.mp3"  # <--- ADICIONE ESTA LINHA
    }
    
    file = music_files.get(music_type)
    if file:
        full_path = os.path.join(BASE_DIR, file)
        if os.path.exists(full_path):
            try:
                pygame.mixer.music.load(full_path)
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)
                print(f"Tocando música: {file}")
            except Exception as e:
                print(f"Erro na música {file}: {e}")

def stop_music():
    pygame.mixer.music.stop()

def game_loop(screen):
    clock = pygame.time.Clock()
    
    print("=== CARREGANDO SONS ===")
    
    # Mude de .wav para .mp3:
    shoot_sound, _ = ResourceManager.load_sound("assets/sounds/shoot.mp3", 0.3)
    enemy_shoot_sound, _ = ResourceManager.load_sound("assets/sounds/enemy_shoot.mp3", 0.3)
    death_sound, _ = ResourceManager.load_sound("assets/sounds/death.mp3", 0.5)
    powerup_sound, _ = ResourceManager.load_sound("assets/sounds/powerup.mp3", 0.4)
    explosion_sound, _ = ResourceManager.load_sound("assets/sounds/explosion.mp3", 0.5)
    
    # Testa se os sons carregaram
    print(f"Shoot sound: {shoot_sound is not None}")
    print(f"Enemy shoot: {enemy_shoot_sound is not None}")
    print(f"Death sound: {death_sound is not None}")
    print(f"Powerup sound: {powerup_sound is not None}")
    print(f"Explosion sound: {explosion_sound is not None}")
    
    player = Player(375, 520)
    bullets = []
    enemies = []
    powerups = []
    enemy_bullets = []
    boss = None
    
    score = 0
    enemies_to_spawn = 10
    game_state = "playing"
    paused = False
    death_played = False
    
    font = pygame.font.Font(None, 36)
    font_big = pygame.font.Font(None, 72)
    
    # Toca música do jogo
    play_music("game")
    
    # Spawn inicial
    for i in range(5):
        enemy_type = random.choice(["normal", "fast", "tank"])
        enemies.append(Enemy(random.randint(50, 750), random.randint(-200, -50), enemy_type))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_music()
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stop_music()
                    return "menu"
                if event.key == pygame.K_p:
                    paused = not paused
                if game_state == "victory" or game_state == "gameover":
                    if event.key == pygame.K_r:
                        stop_music()
                        return "start"
                    if event.key == pygame.K_ESCAPE:
                        stop_music()
                        return "menu"
        
        if paused:
            pause_text = font_big.render("PAUSED", True, (255, 255, 255))
            screen.blit(pause_text, (800//2 - pause_text.get_width()//2, 300))
            pygame.display.flip()
            clock.tick(60)
            continue
        
        keys = pygame.key.get_pressed()
        player.move(keys)
        
        # Atirar
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            new_bullets = player.shoot(shoot_sound)
            bullets.extend(new_bullets)
        
        if player.shoot_timer > 0:
            player.shoot_timer -= 1
        
        for bullet in bullets[:]:
            bullet.move()
            if bullet.y < 0 or bullet.y > 600:
                bullets.remove(bullet)
        
        if game_state == "playing":
            if len(enemies) < 5 and enemies_to_spawn > 0:
                enemy_type = random.choice(["normal", "fast", "tank"])
                enemies.append(Enemy(random.randint(50, 750), random.randint(-200, -50), enemy_type))
                enemies_to_spawn -= 1
            
            if len(enemies) == 0 and enemies_to_spawn == 0:
                game_state = "boss"
                boss = Boss(350, 50)
                play_music("boss")
                death_played = False
            
            for enemy in enemies[:]:
                enemy.move()
                if enemy.y > 650:
                    enemies.remove(enemy)
                
                for bullet in bullets[:]:
                    if bullet.shooter == "player" and enemy.get_rect().colliderect(bullet.get_rect()):
                        bullets.remove(bullet)
                        if enemy.hit():
                            enemies.remove(enemy)
                            score += 10
                            if explosion_sound:
                                explosion_sound.play()
                                print("Explosão!")  # Debug
                            if random.random() < 0.3:
                                power_type = random.choice(["double", "life", "speed"])
                                powerups.append(PowerUp(enemy.x, enemy.y, power_type))
                        break
                
                if player.get_rect().colliderect(enemy.get_rect()):
                    player.hit(death_sound if player.lives > 1 else None)
                    if player.lives <= 0:
                        game_state = "gameover"
                    enemies.remove(enemy)
        
        elif game_state == "boss":
            if boss:
                boss.move()
                
                boss_bullet = boss.shoot(enemy_shoot_sound)
                if boss_bullet:
                    enemy_bullets.append(boss_bullet)
                if boss.shoot_timer > 0:
                    boss.shoot_timer -= 1
                
                for bullet in bullets[:]:
                    if bullet.shooter == "player" and boss.get_rect().colliderect(bullet.get_rect()):
                        bullets.remove(bullet)
                        if boss.hit():
                            game_state = "victory"
                            score += 100
                            play_music("victory")
                            if explosion_sound:
                                explosion_sound.play()
                        break
                
                if player.get_rect().colliderect(boss.get_rect()):
                    player.hit(death_sound if player.lives > 1 else None)
                    if player.lives <= 0:
                        game_state = "gameover"
        
        for power in powerups[:]:
            power.move()
            if power.y > 600:
                powerups.remove(power)
            elif player.get_rect().colliderect(power.get_rect()):
                if powerup_sound:
                    powerup_sound.play()
                    print("Power-up coletado!")  # Debug
                if power.power_type == "double":
                    player.double_shot = True
                    player.double_shot_timer = 600
                elif power.power_type == "life":
                    player.lives = min(player.lives + 1, 5)
                elif power.power_type == "speed":
                    player.speed = min(player.speed + 1, 8)
                powerups.remove(power)
        
        for ebullet in enemy_bullets[:]:
            ebullet.move()
            if ebullet.y > 600:
                enemy_bullets.remove(ebullet)
            elif player.get_rect().colliderect(ebullet.get_rect()):
                enemy_bullets.remove(ebullet)
                player.hit(death_sound if player.lives > 1 else None)
                if player.lives <= 0:
                    game_state = "gameover"
        
        screen.fill((0, 0, 30))
        
        for _ in range(100):
            pygame.draw.circle(screen, (100, 100, 150), (random.randint(0, 800), random.randint(0, 600)), 1)
        
        player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        for power in powerups:
            power.draw(screen)
        for ebullet in enemy_bullets:
            ebullet.draw(screen)
        if boss:
            boss.draw(screen)
        
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {player.lives}", True, (255, 255, 255))
        
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))
        
        if player.double_shot:
            power_text = font.render("DOUBLE SHOT!", True, (0, 255, 255))
            screen.blit(power_text, (10, 90))
        
        if game_state == "victory":
            victory_text = font_big.render("VICTORY!", True, (255, 255, 0))
            restart_text = font.render("Press R to restart or ESC to menu", True, (255, 255, 255))
            screen.blit(victory_text, (800//2 - victory_text.get_width()//2, 250))
            screen.blit(restart_text, (800//2 - restart_text.get_width()//2, 350))
        
        if game_state == "gameover":
            if not death_played and death_sound:
                death_sound.play()
                death_played = True
                pygame.mixer.music.stop()  # <--- Para a música atual
                play_music("gameover")      # <--- Toca música de game over
            
            gameover_text = font_big.render("GAME OVER", True, (255, 0, 0))
            restart_text = font.render("Press R to restart or ESC to menu", True, (255, 255, 255))
            screen.blit(gameover_text, (800//2 - gameover_text.get_width()//2, 250))
            screen.blit(restart_text, (800//2 - restart_text.get_width()//2, 350))
        
        pygame.display.flip()
        clock.tick(60)