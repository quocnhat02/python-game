import pygame


class Score:
    def __init__(self):
        self.font = pygame.font.Font(None, 74)
        self.left_score = 0
        self.right_score = 0

    def render(self, screen):
        left_text = self.font.render(
            str(self.left_score), True, (255, 255, 255))
        right_text = self.font.render(
            str(self.right_score), True, (255, 255, 255))

        screen.blit(left_text, (250, 10))
        screen.blit(right_text, (520, 10))
