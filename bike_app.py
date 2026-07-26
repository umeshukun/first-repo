import random
import time
import streamlit as st

# ページ基本設定（ワイドレイアウト＆ダーク基調）
st.set_page_config(
    page_title="NEON RIDER - バイクカスタム＆サウンドマシン",
    page_icon="🏍️",
    layout="wide",
)

# 派手なCSSデザインの適用（ネオンカラー・アニメーション風）
st.markdown(
    """
    <style>
    /* メイン背景とフォントの設定 */
    .stApp {
        background-color: #0b0e14;
        color: #00ffff;
    }
    /* ネオン風のタイトル */
    .neon-title {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #fff;
        text-shadow: 0 0 10px #ff007f, 0 0 20px #ff007f, 0 0 40px #ff007f;
        margin-bottom: 20px;
    }
    /* 迫力のあるメトリックカード */
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid #00ffff;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.2);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- ヘッダー ---
st.markdown(
    "<h1 class='neon-title'>🏍️ NEON RIDER SPEC & SOUND 🏁</h1>",
    unsafe_allow_html=True,
)
st.caption(
    "🔥 最強の相棒をビルドせよ！排気量とエンジンタイプでマシンを爆音カスタマイズ！"
)

st.divider()

# --- サイドバー：カスタムパネル ---
st.sidebar.header("🛠️ カスタムガレージ")

# 1. バイクのタイプ選択
bike_type = st.sidebar.selectbox(
    "1. マシンタイプを選択",
    ["スーパースポーツ (SS)", "ネイキッド", "アメリカン/クルーザー", "オフロード"],
)

# 2. 気筒数（エンジン）の選択
engine_type = st.sidebar.radio(
    "2. エンジン形式",
    ["単気筒 (Single)", "2気筒 (Twin)", "4気筒 (Inline-4)"],
    index=2,
)

# 3. 排気量スライダー
displacement = st.sidebar.slider(
    "3. 排気量 (cc)", min_value=50, max_value=1300, value=600, step=50
)

# --- メインエリア：2列レイアウト ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("⚡ マシンステータス")

    # パラメータ計算（見た目を賑やかにする演出ロジック）
    horsepower = int((displacement / 10) * (3 if "4気筒" in engine_type else 2))
    top_speed = int(100 + (displacement / 6))

    # 3つのメトリック（数値表示）を並べる
    m1, m2, m3 = st.columns(3)
    m1.metric(label="推定馬力", value=f"{horsepower} PS")
    m2.metric(label="最高速度", value=f"{top_speed} km/h")
    m3.metric(label="サウンド危険度", value="爆音 🔥" if displacement > 400 else "マイルド 🌿")

    # 派手なプログレスバー表示
    st.write("🏃‍♂️ **加速性能 (0-100km/h)**")
    accel_val = min(1.0, displacement / 1000)
    st.progress(accel_val)

    st.write("🌀 **コーナー攻め度**")
    corner_val = 0.9 if "SS" in bike_type else 0.5
    st.progress(corner_val)

with col2:
    st.subheader("🔊 サウンド＆エフェクト")

    # 選択に応じたGIF画像や演出（ダミー画像）
    st.image(
        "https://images.unsplash.com/photo-1558981806-ec527fa84c39?w=800",
        caption=f"{bike_type} - {displacement}cc Spec",
        use_column_width=True,
    )

    # アクションボタン（クリックで派手な演出）
    if st.button("🔥 アクセルを全開にする（サウンドテスト）"):
        # プログレスバーで空ぶかし演出
        st.write("💨 **REV LIMITER!**")
        rpm_bar = st.progress(0)
        sound_text = st.empty()

        sounds = {
            "単気筒 (Single)": "ドコドコドコッ！ババババッ！💥",
            "2気筒 (Twin)": "ドコドコドコ...ブォォォン！！🔥",
            "4気筒 (Inline-4)": "クォォォォーン！！！超高音フォーン！！🚀",
        }

        for i in range(100):
            time.sleep(0.01)
            rpm_bar.progress(i + 1)

        st.success(f"【サウンド】: {sounds[engine_type]}")
        st.balloons()  # 紙吹雪を散らす演出！

# --- フッター ---
st.divider()
st.info("💡 好きなバイクのジャンルに合わせて、背景色や画像URLを差し替えるとさらにカッコよくなります！")