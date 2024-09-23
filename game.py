import pygame

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Di chuyển nhân vật với bắn")

# Tốc độ khung hình
clock = pygame.time.Clock()

# Tạo danh sách chứa 3 ảnh của nhân vật khi chạy
run_images = [
    pygame.image.load('Run-1.png'),
    pygame.image.load('Run-2.png'),
    pygame.image.load('Run-3.png')
]

# Tạo danh sách chứa 3 ảnh của nhân vật khi chạy và bắn
run_shoot_images = [
    pygame.image.load('RunShoot-1.png'),
    pygame.image.load('RunShoot-2.png'),
    pygame.image.load('RunShoot-3.png')
]

# Tạo danh sách chứa 3 ảnh của nhân vật khi đứng yên và bắn
shoot_images = [
    pygame.image.load('Shoot-1.png'),
    pygame.image.load('Shoot-2.png'),
    pygame.image.load('Shoot-3.png')
]

# Tạo ảnh của nhân vật khi đứng yên
idle_image = pygame.image.load('robot-1.png')

# Ảnh viên đạn
bullet_image = pygame.image.load('Bullet.png')

# Tỷ lệ kích thước các ảnh của nhân vật (nếu cần)
run_images = [pygame.transform.scale(img, (50, 50)) for img in run_images]
run_shoot_images = [pygame.transform.scale(
    img, (50, 50)) for img in run_shoot_images]
shoot_images = [pygame.transform.scale(img, (50, 50)) for img in shoot_images]
idle_image = pygame.transform.scale(idle_image, (50, 50))
bullet_image = pygame.transform.scale(bullet_image, (20, 10))

# Khởi tạo vị trí của nhân vật
player_x = 375
player_y = 225
player_speed = 5

# Biến dùng để điều khiển animation
current_image = 0  # Ảnh hiện tại (0, 1, 2)
animation_speed = 0.2  # Tốc độ thay đổi ảnh
frame_count = 0  # Biến đếm khung hình
is_moving = False  # Biến kiểm tra nhân vật có di chuyển hay không
is_facing_right = True  # Biến kiểm tra hướng của nhân vật

# Nhảy
is_jumping = False
jump_velocity = 10  # Tốc độ nhảy ban đầu
gravity = 0.5       # Trọng lực để kéo nhân vật xuống sau khi nhảy

# Bắn
is_shooting = False  # Biến kiểm tra trạng thái bắn
can_shoot = True  # Biến kiểm tra xem có thể bắn không (bắn từng viên một)
bullets = []  # Danh sách viên đạn
bullet_speed = 10  # Tốc độ di chuyển viên đạn

# Vòng lặp game chính
running = True

while running:
    # Kiểm tra các sự kiện đầu vào từ người dùng
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Nhận phím nhấn từ bàn phím
    keys = pygame.key.get_pressed()

    # Kiểm tra nhảy
    if not is_jumping:
        if keys[pygame.K_UP]:  # Nhấn phím lên để nhảy
            is_jumping = True
    else:
        if jump_velocity >= -10:
            neg = 1 if jump_velocity < 0 else -1
            # player_y += (jump_velocity ** 2) * 0.5 * \
            #     neg  # Tính toán vị trí nhảy
            player_y -= jump_velocity
            jump_velocity -= 0.5
        else:
            is_jumping = False
            jump_velocity = 10  # Reset lại tốc độ nhảy

    # Di chuyển nhân vật trái hoặc phải
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
        frame_count += animation_speed  # Tăng biến đếm frame để thay đổi ảnh
        is_moving = True  # Đặt cờ khi di chuyển
        is_facing_right = False  # Nhân vật quay sang trái
    elif keys[pygame.K_RIGHT] and player_x < 750:
        player_x += player_speed
        frame_count += animation_speed  # Tăng biến đếm frame để thay đổi ảnh
        is_moving = True  # Đặt cờ khi di chuyển
        is_facing_right = True  # Nhân vật quay sang phải
    else:
        is_moving = False  # Nếu không có phím di chuyển thì cờ là False

    # Thay đổi ảnh dựa trên frame_count (chỉ sử dụng 3 ảnh)
    if is_moving:
        current_image = int(frame_count) % len(run_images)
    else:
        current_image = -1  # Đặt giá trị này để hiển thị ảnh đứng yên

    # Bắn đạn khi nhấn phím Space (bắn một viên mỗi lần nhấn Space)
    if keys[pygame.K_SPACE] and can_shoot:
        is_shooting = True  # Đặt cờ bắn
        can_shoot = False  # Không thể bắn thêm viên nào cho đến khi thả phím
        if is_facing_right:
            bullet_x = player_x + 50  # Vị trí đầu của viên đạn (sát nhân vật)
            bullet_y = player_y + 25
            bullet_dir = 1  # Hướng viên đạn (phải)
        else:
            bullet_x = player_x  # Vị trí đầu của viên đạn (trái nhân vật)
            bullet_y = player_y + 25
            bullet_dir = -1  # Hướng viên đạn (trái)

        # Thêm viên đạn vào danh sách
        bullets.append([bullet_x, bullet_y, bullet_dir])

    # Khi thả phím Space, có thể bắn viên tiếp theo
    if not keys[pygame.K_SPACE]:
        can_shoot = True

    # Di chuyển các viên đạn
    for bullet in bullets:
        bullet[0] += bullet_speed * bullet[2]  # Di chuyển đạn theo hướng

    # Xóa các viên đạn ra khỏi màn hình nếu đã bắn quá màn hình
    bullets = [bullet for bullet in bullets if 0 < bullet[0] < 800]

    # Xóa màn hình trước khi vẽ lại
    screen.fill((255, 255, 255))  # Màu nền trắng

    # Vẽ nhân vật với ảnh tương ứng
    if is_moving and is_shooting:
        # Nếu đang di chuyển và bắn, sử dụng ảnh chạy và bắn
        if is_facing_right:
            screen.blit(run_shoot_images[current_image], (player_x, player_y))
        else:
            flipped_image = pygame.transform.flip(
                run_shoot_images[current_image], True, False)
            screen.blit(flipped_image, (player_x, player_y))
    elif is_moving:
        # Nếu chỉ di chuyển
        if is_facing_right:
            screen.blit(run_images[current_image], (player_x, player_y))
        else:
            flipped_image = pygame.transform.flip(
                run_images[current_image], True, False)
            screen.blit(flipped_image, (player_x, player_y))
    elif is_shooting:
        # Nếu đứng yên và bắn
        if is_facing_right:
            screen.blit(shoot_images[current_image], (player_x, player_y))
        else:
            flipped_shoot = pygame.transform.flip(
                shoot_images[current_image], True, False)
            screen.blit(flipped_shoot, (player_x, player_y))
    else:
        # Lật ảnh đứng yên nếu nhân vật đang quay trái
        if is_facing_right:
            screen.blit(idle_image, (player_x, player_y))
        else:
            flipped_idle = pygame.transform.flip(idle_image, True, False)
            screen.blit(flipped_idle, (player_x, player_y))

    # Vẽ các viên đạn
    for bullet in bullets:
        screen.blit(bullet_image, (bullet[0], bullet[1]))

    # Cập nhật màn hình
    pygame.display.flip()

    # Giới hạn tốc độ khung hình (60 FPS)
    clock.tick(60)

# Thoát Pygame
pygame.quit()
