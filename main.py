from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Caught")
background = transform.scale(image.load("images/08-05-23 19.png"), (700, 500))

window.blit(background, (0, 0))
