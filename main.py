from pygame import *

# Constants
FPS = 60

# Main settings
window = display.set_mode((700, 500))
display.set_caption("Caught")
clock = time.Clock()

# Images
background = transform.scale(image.load("images/08-05-23 19.png"), (700, 500))
tomato = transform.scale(image.load("images/tomate.png"), (200, 150))

# Game cycle
game = True
while game:
    window.blit(background, (0, 0))
    window.blit(image.load("images/16-05-23 23.png"), (1, 0))
    window.blit(tomato, (500, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
