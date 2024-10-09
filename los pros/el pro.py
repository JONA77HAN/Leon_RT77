import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Controlador W A S D')

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Posición del objeto
x, y = screen_width // 2, screen_height // 2
speed = 5

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener el estado de las teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= speed  # Mover hacia arriba
    if keys[pygame.K_s]:
        y += speed  # Mover hacia abajo
    if keys[pygame.K_a]:
        x -= speed  # Mover hacia la izquierda
    if keys[pygame.K_d]:
        x += speed  # Mover hacia la derecha

    # Limitar el movimiento dentro de la ventana
    x = max(0, min(x, screen_width))
    y = max(0, min(y, screen_height))

    # Dibujar
    screen.fill(black)  # Limpiar la pantalla
    pygame.draw.rect(screen, white, (x, y, 50, 50))  # Dibujar el objeto
    pygame.display.flip()  # Actualizar la pantalla

    # Controlar la velocidad de los cuadros
    pygame.time.Clock().tick(60)

# Cerrar pygame
pygame.quit()
sys.exit()