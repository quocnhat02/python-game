from entities.base_entity import BaseEntity


class Paddle(BaseEntity):
    def __init__(self, x, y):
        super().__init__(x, y, 20, 100)

    def move(self, keys, up_key, down_key):
        if keys[up_key] and self.rect.top > 0:
            super().move(0, -5)
        if keys[down_key] and self.rect.bottom < 600:
            super().move(0, 5)
