import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)

# Definir la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Aparecer Cubos Verdes")

# Clase para el cubo verde
class Cubo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()

# Función para dibujar los cubos verdes
def dibujar_cubos(cantidad):
    todos_los_sprites = pygame.sprite.Group()
    for i in range(cantidad):
        cubo = Cubo()
        cubo.rect.x = 50 + 70 * i
        cubo.rect.y = 300
        todos_los_sprites.add(cubo)
    todos_los_sprites.draw(pantalla)
    pygame.display.flip()

# Bucle principal del juego
def main():
    cantidad = 0
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    # Al presionar Enter, dibujar los cubos
                    dibujar_cubos(cantidad)
                elif evento.key == pygame.K_BACKSPACE:
                    # Al presionar Retroceso, borrar el número
                    cantidad = 0
                elif evento.unicode.isdigit():
                    # Si es un número, construir el número
                    cantidad = cantidad * 10 + int(evento.unicode)
        pantalla.fill(NEGRO)
        # Mostrar la cantidad actual
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render("Cantidad: " + str(cantidad), True, VERDE)
        pantalla.blit(texto, [10, 10])
        pygame.display.flip()

if __name__ == "__main__":
    main()

