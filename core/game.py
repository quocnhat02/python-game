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

        # Xác định số điểm để chiến thắng
        self.win_score = 2

        # Biến để kiểm soát trạng thái trò chơi
        self.running = True

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.left_paddle.move(keys, pygame.K_w, pygame.K_s)
        self.right_paddle.move(keys, pygame.K_UP, pygame.K_DOWN)

    def update(self):
        paddles = [self.left_paddle, self.right_paddle]
        self.ball.update(paddles, self.score)

        # Kiểm tra điều kiện chiến thắng
        if self.score.left_score >= self.win_score:
            print("Người chơi bên trái chiến thắng!")
            self.running = False  # Đặt biến dừng
        elif self.score.right_score >= self.win_score:
            print("Người chơi bên phải chiến thắng!")
            self.running = False  # Đặt biến dừng

    def render(self):
        self.screen.fill((0, 0, 0))  # Màu nền đen

        self.left_paddle.render(self.screen)
        self.right_paddle.render(self.screen)
        self.ball.render(self.screen)
        self.score.render(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(60)
