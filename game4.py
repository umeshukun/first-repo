import os
import sys
import time
import random

if os.name == 'nt':
    import msvcrt
    def get_key():
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8', errors='ignore').lower()
            return key
        return None
else:
    import select, tty, termios
    def get_key():
        # Mac/Linux用のキー入力取得処理（Windowsでは通りません）
        pass

WIDTH = 30
HEIGHT = 15

paddle_x = WIDTH // 2 - 2
paddle_w = 5

ball_x = WIDTH // 2
ball_y = HEIGHT - 3
ball_dx = random.choice([-1, 1])
ball_dy = -1

# ブロックの配置 (3行分)
blocks = [[True for _ in range(WIDTH)] for _ in range(3)]

score = 0

print("=== ブロック崩し (A: 左移動 / D: 右移動) ===")
time.sleep(1)

try:
    while True:
        # 入力処理
        key = get_key()
        if key == 'a' and paddle_x > 0:
            paddle_x -= 1
        elif key == 'd' and paddle_x < WIDTH - paddle_w:
            paddle_x += 1

        # ボールの移動
        new_x = ball_x + ball_dx
        new_y = ball_y + ball_dy

        # 壁との衝突判定
        if new_x <= 0 or new_x >= WIDTH - 1:
            ball_dx *= -1
            new_x = ball_x + ball_dx
        if new_y <= 0:
            ball_dy *= -1
            new_y = ball_y + ball_dy

        # ブロックとの衝突判定
        if 0 <= new_y < 3 and blocks[new_y][new_x]:
            blocks[new_y][new_x] = False
            ball_dy *= -1
            score += 10

        # パドルとの衝突判定
        if new_y == HEIGHT - 2 and paddle_x <= new_x < paddle_x + paddle_w:
            ball_dy *= -1

        # 落下判定 (ゲームオーバー)
        if new_y >= HEIGHT:
            print(f"\n🎮 GAME OVER! スコア: {score}")
            break

        ball_x, ball_y = new_x, new_y

        # 画面描画
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # 壁上部
        print("#" * (WIDTH + 2))
        
        for y in range(HEIGHT):
            row = "#"
            for x in range(WIDTH):
                if y < 3 and blocks[y][x]:
                    row += "="
                elif x == ball_x and y == ball_y:
                    row += "O"
                elif y == HEIGHT - 2 and paddle_x <= x < paddle_x + paddle_w:
                    row += "="
                else:
                    row += " "
            row += "#"
            print(row)
            
        print("#" * (WIDTH + 2))
        print(f"Score: {score} | 操作: A(左) / D(右)")
        
        time.sleep(0.08)

except KeyboardInterrupt:
    print("\n終了しました。")