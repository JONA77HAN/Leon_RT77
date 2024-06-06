import pygame
import random

# Inicialización de Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Definir dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Arañas")

# Definir clase para el personaje principal (Dubo)
class Dubo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
    
    def update(self):
        # Mover el Dubo con las teclas de flecha
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Definir clase para las arañas
class Araña(pygame.sprite.Sprite):
    def __init__(self, color, resistencia):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
        self.speedx = random.choice([-3, -2, 2, 3])
        self.speedy = random.choice([-3, -2, 2, 3])
        self.resistencia = resistencia

    def update(self):
        # Mover la araña
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Rebotar cuando alcanza los bordes de la pantalla
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speedx *= -1
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.speedy *= -1

# Definir clase para el proyectil
class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedy = -5

    def update(self):
        self.rect.y += self.speedy
        # Eliminar el proyectil si sale de la pantalla
        if self.rect.bottom < 0:
            self.kill()

# Crear grupos de sprites
all_sprites = pygame.sprite.Group()
aranhas = pygame.sprite.Group()
proyectiles = pygame.sprite.Group()

# Crear el Dubo
dubo = Dubo()
all_sprites.add(dubo)

# Crear arañas normales
for _ in range(5):
    araña = Araña(BLACK, 1)  # Resistencia 1 para las arañas normales
    all_sprites.add(araña)
    aranhas.add(araña)

# Crear araña azul
araña_azul = Araña(BLUE, 5)  # Resistencia 5 para la araña azul
all_sprites.add(araña_azul)
aranhas.add(araña_azul)

# Loop del juego
running = True
clock = pygame.time.Clock()
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Disparar cuando se presiona la tecla de espacio
            if event.key == pygame.K_SPACE:
                proyectil = Proyectil(dubo.rect.centerx, dubo.rect.top)
                all_sprites.add(proyectil)
                proyectiles.add(proyectil)

    # Actualizar
    all_sprites.update()

    # Verificar colisiones entre el Dubo y las arañas
    hits = pygame.sprite.spritecollide(dubo, aranhas, False)
    if hits:
        running = False

    # Verificar colisiones entre los proyectiles y las arañas
    for proyectil in proyectiles:
        hits = pygame.sprite.spritecollide(proyectil, aranhas, False)
        for hit in hits:
            # Reducir la resistencia de la araña azul si es alcanzada por un proyectil
            if hit == araña_azul:
                araña_azul.resistencia -= 1
                # Si la resistencia llega a cero, eliminar la araña azul
                if araña_azul.resistencia == 0:
                    araña_azul.kill()
            proyectil.kill()

    # Dibujar / Renderizar
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Controlar la velocidad de actualización
    clock.tick(60)

pygame.quit()




