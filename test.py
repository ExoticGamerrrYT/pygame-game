import pygame

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana del juego
window_width = 800
window_height = 600

# Crear la ventana del juego
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("RPG Movement")

# Posición inicial del personaje
player_x = 400
player_y = 300

# Tamaño del personaje
player_width = 32
player_height = 32

# Velocidad de movimiento del personaje
player_speed = 0.07

# Variable para almacenar las teclas presionadas
keys = {
    "up": False,
    "down": False,
    "left": False,
    "right": False
}

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys["up"] = True
            elif event.key == pygame.K_DOWN:
                keys["down"] = True
            elif event.key == pygame.K_LEFT:
                keys["left"] = True
            elif event.key == pygame.K_RIGHT:
                keys["right"] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys["up"] = False
            elif event.key == pygame.K_DOWN:
                keys["down"] = False
            elif event.key == pygame.K_LEFT:
                keys["left"] = False
            elif event.key == pygame.K_RIGHT:
                keys["right"] = False

    # Actualizar la posición del personaje según las teclas presionadas
    if keys["up"]:
        player_y -= player_speed
    if keys["down"]:
        player_y += player_speed
    if keys["left"]:
        player_x -= player_speed
    if keys["right"]:
        player_x += player_speed

    # Verificar límites de la ventana
    if player_x < 0:
        player_x = 0
    elif player_x > window_width - player_width:
        player_x = window_width - player_width
    if player_y < 0:
        player_y = 0
    elif player_y > window_height - player_height:
        player_y = window_height - player_height

    # Dibujar en la ventana
    window.fill((0, 0, 0))  # Limpiar la ventana
    pygame.draw.rect(window, (255, 0, 0), (player_x, player_y, player_width, player_height))  # Dibujar al personaje
    pygame.display.flip()  # Actualizar la ventana

# Salir del juego
pygame.quit()
