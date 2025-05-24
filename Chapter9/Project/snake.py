import pygame
import sys
import random

# 初始化游戏
pygame.init()

# 窗口的长和宽（x轴和y轴）
window_x = 720
window_y = 480

# 窗口大小
game = pygame.display.set_mode((window_x, window_y))
# 设置标题
pygame.display.set_caption("Snake")

# 定义蛇的位置
snake_position = [100, 50]
# 定义蛇的前4块
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# 定义水果的位置
fruit_position = [random.randint(0, 720), random.randint(0, 480)]

# 当前蛇的方向
direction = 'RIGHT'
change_to = direction

while True:
    # 获取所有的事件
    for event in pygame.event.get():
        # 处理键盘事件
        if event.type == pygame.KEYDOWN:
            # 判断按的是哪个键
            # 键盘的上键
            if event.key == pygame.K_UP:
                change_to = 'UP'
            # 下
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            # 左
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            # 右
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

        # 处理关闭事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 按了上键后还要去知道蛇当前位置是否是往下，如果不是往下才可以让蛇往上走
    if change_to == 'UP' and direction != 'DOWN':
        # 蛇往上
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'RIGHT':
        # 蛇位置 x轴自增10
        snake_position[0] = snake_position[0] + 10
    if direction == 'LEFT':
        snake_position[0] = snake_position[0] - 10
    if direction == 'UP':
        snake_position[1] = snake_position[1] - 10
    if direction == 'DOWN':
        snake_position[1] = snake_position[1] + 10

    # 画蛇
    for i in range(4):
        position = snake_body[i]
        pygame.draw.rect(game, (0, 255, 0), pygame.Rect(position[0], position[1], 10, 10))
    # 画水果
    pygame.draw.rect(game, (255, 255, 255), pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    # 屏幕刷新
    pygame.display.flip()
