import random
import time

# 画面を埋め尽くす文字のセット
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*"

print("\033[32m") # ターミナルの文字色を「緑色」に設定

try:
    while True:
        # ランダムな長さの文字列を作成
        line = "".join(random.choice(chars) if random.random() > 0.3 else " " for _ in range(80))
        print(line)
        time.sleep(0.05) # 速度の調整
except KeyboardInterrupt:
    print("\033[0m\nプログラムを終了しました。") # 色を元に戻す