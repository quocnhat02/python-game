import pygame


class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 100)
        self.speed = 5

    def move(self, keys, up_key, down_key):
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < 600:
            self.rect.y += self.speed

    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
