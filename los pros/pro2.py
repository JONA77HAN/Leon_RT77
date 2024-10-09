import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Controlador W A S D con Contador de Clics')

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Posición del objeto
x, y = screen_width // 2, screen_height // 2
speed = 5

# Contador de clics
click_count = 0
font = pygame.font.Font(None, 36)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_count += 1  # Incrementar el contador de clics

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
    x = max(0, min(x, screen_width - 50))
    y = max(0, min(y, screen_height - 50))

    # Dibujar
    screen.fill(black)  # Limpiar la pantalla
    pygame.draw.rect(screen, white, (x, y, 50, 50))  # Dibujar el objeto

    # Renderizar el texto del contador
    click_text = font.render(f'Clics: {click_count}', True, red)
    screen.blit(click_text, (10, 10))  # Dibujar el texto en la pantalla

    pygame.display.flip()  # Actualizar la pantalla

    # Controlar la velocidad de los cuadros
    pygame.time.Clock().tick(60)

# Cerrar pygame
pygame.quit()
sys.exit()