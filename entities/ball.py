import pygame
import random


class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.speed_x = 5 * random.choice((1, -1))
        self.speed_y = 5 * random.choice((1, -1))

    def reset(self):
        self.rect.center = (400, 300)
        self.speed_x *= random.choice((1, -1))
        self.speed_y *= random.choice((1, -1))

    def update(self, left_paddle, right_paddle, score):
        # Di chuyển bóng
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Va chạm với cạnh trên/dưới
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1

        # Va chạm với paddle
        if self.rect.colliderect(left_paddle.rect) or self.rect.colliderect(right_paddle.rect):
            self.speed_x *= -1

        # Va chạm với biên trái/phải để ghi điểm
        if self.rect.left <= 0:
            score.right_score += 1
            self.reset()

        if self.rect.right >= 800:
            score.left_score += 1
            self.reset()

    def render(self, screen):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)
