import random
import tkinter as tk

# ボタンが押されたときの処理
def draw_omikuji():
    results = ["大吉 🌟", "中吉 😊", "小吉 🙂", "吉 🌿", "凶 😅"]
    # ランダムに運勢を選んでラベルの文字を書き換える
    result_label.config(text=random.choice(results))

# --- 画面（ウィンドウ）の作成 ---
root = tk.Tk()
root.title("今日の運勢アプリ")
root.geometry("300x200") # ウィンドウのサイズ（幅 x 高さ）

# タイトルラベル
title_label = tk.Label(root, text="今日の運勢は？", font=("MS Gothic", 16))
title_label.pack(pady=15)

# 結果を表示するラベル
result_label = tk.Label(root, text="？？？", font=("MS Gothic", 20, "bold"), fg="crimson")
result_label.pack(pady=10)

# おみくじボタン
btn = tk.Button(root, text="おみくじを引く！", font=("MS Gothic", 12), command=draw_omikuji)
btn.pack(pady=10)

# 画面を表示し続けるメインループ
root.mainloop()