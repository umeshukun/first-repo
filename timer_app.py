import customtkinter as ctk

# --- 設定 ---
ctk.set_appearance_mode("Dark")  # ダークモード設定 ("Light" に変更も可能)
ctk.set_default_color_theme("blue")  # テーマカラー ("green", "dark-blue" も選択可)

class PomodoroTimer(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ウィンドウの基本設定
        self.title("ポモドーロタイマー")
        self.geometry("350x400")
        self.resizable(False, False)

        # 変数の初期化
        self.time_left = 25 * 60  # 25分（秒単位）
        self.is_running = False
        self.timer_id = None

        # --- UI（見た目）の作成 ---
        # タイトル
        self.title_label = ctk.CTkLabel(
            self, text="🎯 集中タイム", font=("メイリオ", 22, "bold")
        )
        self.title_label.pack(pady=(30, 10))

        # タイマー表示 (00:00)
        self.time_label = ctk.CTkLabel(
            self, text="25:00", font=("メイリオ", 48, "bold")
        )
        self.time_label.pack(pady=20)

        # スタート / パラメータボタン
        self.start_button = ctk.CTkButton(
            self,
            text="スタート",
            font=("メイリオ", 16, "bold"),
            height=40,
            command=self.toggle_timer,
        )
        self.start_button.pack(pady=10)

        # リセットボタン
        self.reset_button = ctk.CTkButton(
            self,
            text="リセット",
            font=("メイリオ", 14),
            fg_color="gray",
            hover_color="#555555",
            command=self.reset_timer,
        )
        self.reset_button.pack(pady=5)

    def update_timer(self):
        """1秒ごとにカウントダウンする処理"""
        if self.time_left > 0:
            self.time_left -= 1
            mins, secs = divmod(self.time_left, 60)
            # 分と秒を2桁の文字列に整形 (例: 05:09)
            self.time_label.configure(text=f"{mins:02d}:{secs:02d}")
            # 1000ミリ秒(1秒)後に再度この関数を呼び出す
            self.timer_id = self.after(1000, self.update_timer)
        else:
            self.is_running = False
            self.title_label.configure(text="🎉 お疲れ様でした！")
            self.start_button.configure(text="再スタート")

    def toggle_timer(self):
        """スタート / 一時停止の切り替え"""
        if not self.is_running:
            self.is_running = True
            self.start_button.configure(
                text="一時停止", fg_color="#E53935", hover_color="#C62828"
            )
            self.update_timer()
        else:
            self.is_running = False
            self.start_button.configure(
                text="再開", fg_color="#1f538d", hover_color="#14375e"
            )
            if self.timer_id:
                self.after_cancel(self.timer_id)

    def reset_timer(self):
        """リセット処理"""
        if self.timer_id:
            self.after_cancel(self.timer_id)
        self.is_running = False
        self.time_left = 25 * 60
        self.time_label.configure(text="25:00")
        self.title_label.configure(text="🎯 集中タイム")
        self.start_button.configure(
            text="スタート", fg_color="#1f538d", hover_color="#14375e"
        )


if __name__ == "__main__":
    app = PomodoroTimer()
    app.mainloop()