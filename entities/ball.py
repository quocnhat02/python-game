from entities.base_entity import BaseEntity
import random
import pygame


class Ball(BaseEntity):
    def __init__(self, x, y):
        super().__init__(x, y, 20, 20, color=(255, 255, 255), shape_type='circle')
        self.speed_x = 5 * random.choice((1, -1))
        self.speed_y = 5 * random.choice((1, -1))

    def reset(self):
        self.rect.center = (400, 300)
        self.speed_x *= random.choice((1, -1))
        self.speed_y *= random.choice((1, -1))

    def update(self, paddles, score):
        super().move(self.speed_x, self.speed_y)

        # Va chạm với cạnh trên/dưới
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1

        # Va chạm với paddle
        for paddle in paddles:
            if self.check_collision(paddle):
                self.speed_x *= -1

        # Ghi điểm
        if self.rect.left <= 0:
            score.right_score += 1
            self.reset()
        if self.rect.right >= 800:
            score.left_score += 1
            self.reset()
