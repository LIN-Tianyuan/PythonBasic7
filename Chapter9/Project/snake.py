import pygame
import sys

# 初始化游戏
pygame.init()

# 窗口的长和宽（x轴和y轴）
window_x = 720
window_y = 480

# 窗口
game = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake")

snake_position = [100, 50]

snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]


while True:
    # 处理关闭事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 画蛇
    pygame.draw.rect(game, (0, 255, 0), pygame.Rect(snake_position[0], snake_position[1], 10, 10))
    # 屏幕刷新
    pygame.display.flip()
