from pygame import *

# Constants
FPS = 60

# Coordinates
x1, x2 = 100, 300
y1, y2 = 200, 300

# Main settings
window = display.set_mode((700, 500))
display.set_caption("Caught")
clock = time.Clock()

# Music
mixer.init()
sonido_boom = mixer.Sound("music/boom.ogg")
clap_clap = mixer.Sound("music/clapclap.ogg")
auuuugh = mixer.Sound("music/aaaaaugh.ogg")

bg_sound = mixer.Sound("music/verano_azul.ogg")
mixer.Sound.play(bg_sound, -1)

# Images
background = transform.scale(image.load("images/08-05-23 19.png"), (700, 500))
player = transform.scale(image.load("images\sprites\player.png"), (50, 50)) # The pink one :)
enemy = transform.scale(image.load("images\sprites\enemy.png"), (50, 50)) # The blue one :)

# Speed
speed = 10

# Game cycle
game = True
while game:
    window.blit(background, (0, 0))
    window.blit(player, (x1, y1))
    window.blit(enemy, (x2, y2))

    # Keys
    keys_pressed = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            game = False
        
        #Movement
        if keys_pressed[K_LEFT] and x1 > 5:
            x1 -= speed
        if keys_pressed[K_RIGHT] and x1 < 650:
            x1 += speed
        if keys_pressed[K_UP] and y1 > 5:
            y1 -= speed
        if keys_pressed[K_DOWN] and y1 < 450:
            y1 += speed
        if keys_pressed[K_a] and x2 > 5:
            x2 -= speed
        if keys_pressed[K_d] and x2 < 650:
            x2 += speed
        if keys_pressed[K_w] and y2 > 5:
            y2 -= speed
        if keys_pressed[K_s] and y2 < 450:
            y2 += speed
        
        # Sounds
        if keys_pressed[K_1]: # sonido boom
            mixer.Sound.play(sonido_boom)
        if keys_pressed[K_2]: # clap
            mixer.Sound.play(clap_clap)
        if keys_pressed[K_3]: # auggh
            mixer.Sound.play(auuuugh)
    display.update()
    clock.tick(FPS)
