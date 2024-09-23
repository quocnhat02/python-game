import pygame


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.is_jumping = False
        self.jump_velocity = 10
        self.gravity = 0.5
        self.is_moving = False
        self.is_facing_right = True
        self.bullets = []
        self.can_shoot = True
        self.is_shooting = False
        self.current_image = 0
        self.frame_count = 0
        self.animation_speed = 0.2

        # Tầm bắn (khoảng cách tối đa mà viên đạn có thể bay)
        self.bullet_range = 400

        # Tải hình ảnh
        self.run_images = [pygame.transform.scale(
            pygame.image.load(f'Run-{i}.png'), (50, 50)) for i in range(1, 4)]
        self.run_shoot_images = [pygame.transform.scale(
            pygame.image.load(f'RunShoot-{i}.png'), (50, 50)) for i in range(1, 4)]
        self.shoot_images = [pygame.transform.scale(
            pygame.image.load(f'Shoot-{i}.png'), (50, 50)) for i in range(1, 4)]
        self.idle_image = pygame.transform.scale(
            pygame.image.load('idle-1.png'), (50, 50))
        self.bullet_image = pygame.transform.scale(
            pygame.image.load('Bullet.png'), (20, 10))

    def jump(self):
        if not self.is_jumping:
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.is_jumping = True
        else:
            if self.jump_velocity >= -10:
                self.y -= self.jump_velocity
                self.jump_velocity -= self.gravity
            else:
                self.is_jumping = False
                self.jump_velocity = 10

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
            self.frame_count += self.animation_speed
            self.is_moving = True
            self.is_facing_right = False
        elif keys[pygame.K_RIGHT] and self.x < 750:
            self.x += self.speed
            self.frame_count += self.animation_speed
            self.is_moving = True
            self.is_facing_right = True
        else:
            self.is_moving = False

    def shoot(self):
        if self.can_shoot:
            self.is_shooting = True
            self.can_shoot = False
            bullet_x = self.x + (50 if self.is_facing_right else 0)
            bullet_y = self.y + 25
            bullet_dir = 1 if self.is_facing_right else -1
            # Thêm start_x để theo dõi vị trí ban đầu của viên đạn
            self.bullets.append([bullet_x, bullet_y, bullet_dir, bullet_x])

    def update_bullets(self):
        for bullet in self.bullets:
            bullet[0] += 10 * bullet[2]  # Di chuyển đạn
            # Xóa viên đạn nếu nó đã vượt quá tầm bắn
            if abs(bullet[0] - bullet[3]) > self.bullet_range:
                self.bullets.remove(bullet)

    def draw(self, screen):
        if self.is_shooting:
            self.frame_count += self.animation_speed
            current_image = int(self.frame_count) % len(self.shoot_images)
            img = self.shoot_images[current_image]
        elif self.is_moving:
            current_image = int(self.frame_count) % len(self.run_images)
            img = self.run_images[current_image]
        else:
            img = self.idle_image

        if not self.is_facing_right:
            img = pygame.transform.flip(img, True, False)

        screen.blit(img, (self.x, self.y))

        # Vẽ các viên đạn
        for bullet in self.bullets:
            screen.blit(self.bullet_image, (bullet[0], bullet[1]))

        if not pygame.key.get_pressed()[pygame.K_SPACE]:
            self.is_shooting = False


# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Di chuyển nhân vật với bắn")

# Tốc độ khung hình
clock = pygame.time.Clock()

# Khởi tạo nhân vật
player = Player(375, 525)

# Vòng lặp game chính
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Kiểm tra nhảy
    player.jump()

    # Di chuyển nhân vật
    player.move(keys)

    # Bắn
    if keys[pygame.K_SPACE]:
        player.shoot()
    if not keys[pygame.K_SPACE]:
        player.can_shoot = True

    # Cập nhật viên đạn
    player.update_bullets()

    # Xóa màn hình trước khi vẽ lại
    screen.fill((255, 255, 255))  # Màu nền trắng

    # Vẽ nhân vật
    player.draw(screen)

    # Cập nhật màn hình
    pygame.display.flip()

    # Giới hạn tốc độ khung hình (60 FPS)
    clock.tick(60)

# Thoát Pygame
pygame.quit()
