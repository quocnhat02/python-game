import pygame

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Di chuyển nhân vật")

# Tốc độ khung hình
clock = pygame.time.Clock()

# Tải hình ảnh nhân vật
player_image = pygame.image.load('player.jpg')
player_image = pygame.transform.scale(
    player_image, (50, 50))  # Tùy chỉnh kích thước hình ảnh

# Khởi tạo vị trí của nhân vật
player_x = 375  # Vị trí giữa màn hình (800/2 - 50/2)
player_y = 525  # Vị trí gần đáy màn hình
player_speed = 5  # Tốc độ di chuyển của nhân vật

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
    # 800 (chiều rộng màn hình) - 50 (kích thước hình ảnh)
    if keys[pygame.K_RIGHT] and player_x < 750:
        player_x += player_speed

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

    # Vẽ nhân vật
    screen.blit(player_image, (player_x, player_y))

    # Cập nhật màn hình
    pygame.display.flip()

    # Giới hạn tốc độ khung hình (60 FPS)
    clock.tick(60)

# Thoát Pygame
pygame.quit()
