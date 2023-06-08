from pygame import *

# Constants
FPS = 60

# Coordinates
x1, x2 = 100, 300
y1, y2 = 300, 300

# Main settings
window = display.set_mode((700, 500))
display.set_caption("Caught")
clock = time.Clock()

# Music
mixer.init()

# Images
background = transform.scale(image.load("images/08-05-23 19.png"), (700, 500))
tomato = transform.scale(image.load("images/tomate.png"), (200, 150))

# Speed
speed = 10

# Game cycle
game = True
while game:
    window.blit(background, (0, 0))
    window.blit(image.load("images/16-05-23 23.png"), (x1, y1))
    window.blit(tomato, (x2, y2))

    # Keys
    keys_pressed = key.get_pressed()

    boom = 

    for e in event.get():
        if e.type == QUIT:
            game = False
        if keys_pressed[K_LEFT] and x1 > 5:
            x1 -= speed
        if keys_pressed[K_RIGHT] and x1 < 660:
            x1 += speed
        if keys_pressed[K_UP] and y1 > 5:
            y1 -= speed
        if keys_pressed[K_DOWN] and y1 < 640:
            y1 += speed
        if keys_pressed[K_1]:

    display.update()
    clock.tick(FPS)
