import random
import time
import streamlit as st

# ページ基本設定
st.set_page_config(
    page_title="伝説のバイクガチャ & カスタム", page_icon="🎰", layout="wide"
)

# 派手なCSSスタイル
st.markdown(
    """
    <style>
    .stApp { background-color: #0d1117; color: #f0f6fc; }
    .neon-title {
        font-size: 2.8rem; font-weight: bold; text-align: center;
        color: #fff; text-shadow: 0 0 10px #ff0055, 0 0 20px #ff0055;
    }
    .gacha-card {
        background: #161b22; border: 2px solid #30363d;
        border-radius: 12px; padding: 20px; text-align: center;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- データベース（排出されるバイクのリスト） ---
BIKE_DATABASE = [
    {
        "name": "NR-999 サイバーファントム",
        "rarity": "SSR 🌟🌟🌟",
        "color": "#ff0055",
        "hp": 210,
        "speed": 340,
        "img": "https://images.unsplash.com/photo-1558981806-ec527fa84c39?w=600",
    },
    {
        "name": "GSX-R 1000 レジェンド",
        "rarity": "SSR 🌟🌟🌟",
        "color": "#00ffff",
        "hp": 202,
        "speed": 310,
        "img": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?w=600",
    },
    {
        "name": "ナイトストライカー 400",
        "rarity": "SR 🌟🌟",
        "color": "#ffaa00",
        "hp": 53,
        "speed": 180,
        "img": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?w=600",
    },
    {
        "name": "ストリートクラシック 250",
        "rarity": "R 🌟",
        "color": "#00ff66",
        "hp": 26,
        "speed": 140,
        "img": "https://images.unsplash.com/photo-1558981359-219d6364c9c8?w=600",
    },
]

# --- セッション状態の初期化 ---
if "my_garage" not in st.session_state:
    st.session_state.my_garage = []  # 所持バイク
if "coins" not in st.session_state:
    st.session_state.coins = 1000  # 初期所持金

# --- ヘッダー ---
st.markdown(
    "<h1 class='neon-title'>🎰 伝説のバイクガチャ & GARAGE 🏍️</h1>",
    unsafe_allow_html=True,
)

# 所持金とガレージ数の表示
col_info1, col_info2 = st.columns(2)
col_info1.metric("💰 所持コイン", f"{st.session_state.coins} G")
col_info2.metric("🏍️ 所持マシン数", f"{len(st.session_state.my_garage)} 台")

st.divider()

# --- メイン画面：タブ切り替え ---
tab1, tab2 = st.tabs(["🎰 ガチャを回す", " garage ガレージ & カスタム"])

# ==================== TAB 1: ガチャ画面 ====================
with tab1:
    st.subheader("🔥 1回 100G でガレージを強化せよ！")

    if st.button("🎰 100Gでガチャを回す！", use_container_width=True):
        if st.session_state.coins < 100:
            st.error("コインが足りません！")
        else:
            st.session_state.coins -= 100

            # 演出（カウントダウン）
            status = st.empty()
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.015)
                progress.progress(i + 1)
                if i == 30:
                    status.warning("エンジン始動...")
                elif i == 70:
                    status.info("高回転限界突破...！！")

            progress.empty()
            status.empty()

            # 重み付け抽選（SSR:15%, SR:35%, R:50%）
            drawn_bike = random.choices(
                BIKE_DATABASE, weights=[5, 10, 35, 50], k=1
            )[0].copy()

            # ガレージに追加
            st.session_state.my_garage.append(drawn_bike)

            # SSR当たりの演出！
            if "SSR" in drawn_bike["rarity"]:
                st.balloons()
                st.success("🎉✨【超激レア】SSRマシン降臨！！！✨🎉")
            else:
                st.info("マシンを獲得しました！")

            # 当たったマシンの表示
            st.markdown(
                f"""
                <div class='gacha-card' style='border-color: {drawn_bike["color"]};'>
                    <h2 style='color: {drawn_bike["color"]};'>{drawn_bike["rarity"]}</h2>
                    <h3>{drawn_bike["name"]}</h3>
                    <p>馬力: {drawn_bike["hp"]} PS / 最高速: {drawn_bike["speed"]} km/h</p>
                </div>
            """,
                unsafe_allow_html=True,
            )
            st.image(drawn_bike["img"], use_container_width=True)

# ==================== TAB 2: ガレージ画面 ====================
with tab2:
    st.subheader("🛠️ 所持マシン一覧 & チューニング")

    if not st.session_state.my_garage:
        st.write("まだマシンを持っていません。ガチャを回してゲットしよう！")
    else:
        # ドロップダウンで手持ちのバイクを選択
        bike_names = [
            f"{i+1}. {b['name']} ({b['rarity']})"
            for i, b in enumerate(st.session_state.my_garage)
        ]
        selected_idx = st.selectbox("カスタムするマシンを選択", range(len(bike_names)), format_func=lambda x: bike_names[x])

        selected_bike = st.session_state.my_garage[selected_idx]

        col_g1, col_g2 = st.columns(2)

        with col_g1:
            st.image(selected_bike["img"], use_container_width=True)

        with col_g2:
            st.write(f"### {selected_bike['name']}")
            st.write(f"レア度: **{selected_bike['rarity']}**")

            # カスタムパーツ（ステータス上昇）
            st.write("#### 🔧 カスタムパーツ装着")

            if st.button("🚀 ターボキット装着 (+50 PS / +30 km/h)"):
                selected_bike["hp"] += 50
                selected_bike["speed"] += 30
                selected_bike["name"] += " [TURBO]"
                st.success("ターボを装着しました！スペックアップ！")
                st.rerun()

            st.metric("現在の馬力", f"{selected_bike['hp']} PS")
            st.metric("現在の最高速", f"{selected_bike['speed']} km/h")
