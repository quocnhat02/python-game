import pygame

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Di chuyển nhân vật")

# Tốc độ khung hình
clock = pygame.time.Clock()

# Tạo danh sách chứa 3 ảnh của nhân vật
run_images = [
    pygame.image.load('Run-1.png'),
    pygame.image.load('Run-2.png'),
    pygame.image.load('Run-3.png')
]

# Tạo ảnh của nhân vật khi đứng yên
idle_image = pygame.image.load('robot-1.png')

# Tỷ lệ kích thước các ảnh của nhân vật (nếu cần)
run_images = [pygame.transform.scale(img, (50, 50)) for img in run_images]
idle_image = pygame.transform.scale(idle_image, (50, 50))

# Khởi tạo vị trí của nhân vật
player_x = 375  # Vị trí giữa màn hình (800/2 - 50/2)
player_y = 525  # Vị trí gần đáy màn hình
player_speed = 5  # Tốc độ di chuyển của nhân vật

# Biến dùng để điều khiển animation
current_image = 0  # Ảnh hiện tại (0, 1, 2)
animation_speed = 0.2  # Tốc độ thay đổi ảnh
frame_count = 0  # Biến đếm khung hình
is_moving = False  # Biến kiểm tra nhân vật có di chuyển hay không
# Biến kiểm tra hướng của nhân vật (true nếu nhân vật quay phải)
is_facing_right = True

# Nhảy
is_jumping = False
jump_velocity = 10  # Tốc độ nhảy ban đầu
gravity = 0.5       # Trọng lực để kéo nhân vật xuống sau khi nhảy

# Cờ để kiểm tra vòng lặp chạy
running = True

# Vòng lặp game chính
while running:
    # Kiểm tra các sự kiện đầu vào từ người dùng
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Nhận phím nhấn từ bàn phím
    keys = pygame.key.get_pressed()

    # Di chuyển nhân vật trái hoặc phải
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
        frame_count += animation_speed  # Tăng biến đếm frame để thay đổi ảnh
        is_moving = True  # Đặt cờ khi di chuyển
        is_facing_right = False  # Nhân vật quay sang trái
    # 800 (chiều rộng màn hình) - 50 (kích thước hình ảnh)
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

    # Logic nhảy khi nhấn Space
    if not is_jumping:
        if keys[pygame.K_SPACE]:  # Nếu nhấn phím Space và không nhảy
            is_jumping = True  # Bắt đầu nhảy
            jump_velocity = 10  # Khởi tạo tốc độ nhảy

    if is_jumping:
        # Nhân vật di chuyển lên trên
        player_y -= jump_velocity
        jump_velocity -= gravity  # Giảm tốc độ nhảy (do trọng lực)

        # Khi tốc độ nhảy âm và chạm đất, kết thúc nhảy
        if player_y >= 525:  # Vị trí đáy màn hình
            player_y = 525  # Đảm bảo nhân vật không rơi qua đáy
            is_jumping = False  # Kết thúc nhảy

    # Xóa màn hình trước khi vẽ lại
    screen.fill((255, 255, 255))  # Màu nền trắng (R,G,B)

    # Vẽ nhân vật với ảnh tương ứng
    if is_moving:
        # Lật ảnh khi nhân vật quay sang trái
        if is_facing_right:
            screen.blit(run_images[current_image], (player_x, player_y))
        else:
            flipped_image = pygame.transform.flip(
                run_images[current_image], True, False)
            screen.blit(flipped_image, (player_x, player_y))
    else:
        # Lật ảnh đứng yên nếu nhân vật đang quay trái
        if is_facing_right:
            screen.blit(idle_image, (player_x, player_y))
        else:
            flipped_idle = pygame.transform.flip(idle_image, True, False)
            screen.blit(flipped_idle, (player_x, player_y))

    # Cập nhật màn hình
    pygame.display.flip()

    # Giới hạn tốc độ khung hình (60 FPS)
    clock.tick(60)

# Thoát Pygame
pygame.quit()
