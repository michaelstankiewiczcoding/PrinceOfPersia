import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Prince of Persia 2D")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = pygame.Vector2(0, 0)

    def update(self, platforms):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = 5
        else:
            self.velocity.x = 0

        if keys[pygame.K_UP]:
            self.velocity.y = -5
        elif keys[pygame.K_DOWN]:
            self.velocity.y = 5
        else:
            self.velocity.y = 0

        # Move the player rect
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Check for collisions and adjust position
        self.collide(platforms)

    def collide(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity.x > 0:  # Moving right
                    self.rect.right = platform.rect.left
                elif self.velocity.x < 0:  # Moving left
                    self.rect.left = platform.rect.right
                if self.velocity.y > 0:  # Moving down
                    self.rect.bottom = platform.rect.top
                elif self.velocity.y < 0:  # Moving up
                    self.rect.top = platform.rect.bottom

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Main game loop
def main():
    clock = pygame.time.Clock()
    player = Player(100, 100)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    platforms = pygame.sprite.Group()
    platform1 = Platform(200, 400, 200, 20)
    platforms.add(platform1)
    all_sprites.add(platform1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update player with platform collision detection
        player.update(platforms)

        window.fill(BLACK)
        all_sprites.draw(window)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()