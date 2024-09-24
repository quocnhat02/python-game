import pygame


class BaseEntity:
    def __init__(self, x, y, width, height, color=(255, 255, 255), shape_type='rect'):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.shape_type = shape_type  # 'rect' or 'circle'

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def render(self, screen):
        if self.shape_type == 'rect':
            # Vẽ hình chữ nhật
            pygame.draw.rect(screen, self.color, self.rect)
        elif self.shape_type == 'circle':
            # Vẽ hình tròn với tọa độ tâm và bán kính
            center = self.rect.center
            radius = self.rect.width // 2  # Giả sử width == height
            pygame.draw.circle(screen, self.color, center, radius)

    def check_collision(self, other):
        return self.rect.colliderect(other.rect)
