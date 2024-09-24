import pygame
from entities.paddle import Paddle
from entities.ball import Ball
from entities.score import Score


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        # Tạo đối tượng paddle cho 2 người chơi
        self.left_paddle = Paddle(20, 250)
        self.right_paddle = Paddle(760, 250)

        # Tạo bóng
        self.ball = Ball(400, 300)

        # Tạo điểm số
        self.score = Score()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.left_paddle.move(keys, pygame.K_w, pygame.K_s)
        self.right_paddle.move(keys, pygame.K_UP, pygame.K_DOWN)

    def update(self):
        self.ball.update(self.left_paddle, self.right_paddle, self.score)

    def render(self):
        self.screen.fill((0, 0, 0))  # Màu nền đen

        self.left_paddle.render(self.screen)
        self.right_paddle.render(self.screen)
        self.ball.render(self.screen)
        self.score.render(self.screen)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(60)
