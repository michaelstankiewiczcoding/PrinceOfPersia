import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Prince of Persia 2D")

# Main game loop
def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill((0, 0, 0))  # Fill the window with black color
        pygame.display.flip()  # Update the display
        clock.tick(60)  # Cap the frame rate at 60 FPS

if __name__ == "__main__":
    main()