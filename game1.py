import random

def guess_game():
    target = random.randint(1, 100)
    attempts = 0
    
    print("=== 1から100までの数字を当てるゲーム ===")
    
    while True:
        try:
            guess = int(input("予想した数字を入力してください: "))
            attempts += 1
            
            if guess < target:
                print("もっと大きい数字です！ ⬆️")
            elif guess > target:
                print("もっと小さい数字です！ ⬇️")
            else:
                print(f"🎉 正解！ {attempts}回目で当たりました！")
                break
        except ValueError:
            print("半角の数字を入力してくださいね。")

if __name__ == "__main__":
    guess_game()