import pygame

# Initialize Pygame
pygame.init()

# Define the window size
width = 800
height = 600

# Create the window
window = pygame.display.set_mode((width, height))

# Set the window title
pygame.display.set_caption("My Pygame Window")

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        # Check if the window has been closed
        if event.type == pygame.QUIT:
            running = False

    # Update the window
    pygame.display.update()

# Quit Pygame
pygame.quit()
