import math
import time
import os

def draw_heart():
    t = 0
    while True:
        # 画面クリア（Windows/Mac両対応）
        os.system('cls' if os.name == 'nt' else 'clear')
        
        scale = 1.0 + 0.15 * math.sin(t * 3) # ドクンドクンと脈打つ動き
        
        for y in range(12, -12, -1):
            line = ""
            for x in range(-30, 30):
                # ハートの方程式
                x_scaled = (x / 15.0) / scale
                y_scaled = (y / 8.0) / scale
                
                if (x_scaled**2 + y_scaled**2 - 1)**3 - (x_scaled**2) * (y_scaled**3) <= 0:
                    line += "❤️"
                else:
                    line += "  "
            print(line)
            
        t += 0.1
        time.sleep(0.05)

if __name__ == "__main__":
    try:
        draw_heart()
    except KeyboardInterrupt:
        print("\n終了しました！")