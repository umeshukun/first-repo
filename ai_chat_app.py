import random
import time
import streamlit as st

# ページ基本設定
st.set_page_config(
    page_title="愚痴聞きAIカウンセラー", page_icon="🤖", layout="centered"
)

st.title("🤖 愚痴聞きAIカウンセラー")
st.caption("日頃のモヤモヤや愚痴を吐き出してください。全力で共感します！")

# --- AIのキャラクター設定（ここを自由にいじれます！） ---
# 返答のバリエーション
EMPATHY_RESPONSES = [
    "それは本当に大変でしたね…！頑張りすぎていませんか？",
    "わかります、その気持ち！私だったら絶対に耐えられませんよ…！",
    "話してくれてありがとうございます。今日は美味しいものを食べて自分を労わってくださいね。",
    "それは理不尽すぎますね！あなたは何も悪くないですよ！",
    "なるほど…それはモヤモヤして当然です。どんどん吐き出していきましょう！",
]

# 挨拶用の初期メッセージ
INITIAL_MESSAGE = "今日もお疲れ様です！何か嫌なことやモヤモヤすることはありましたか？何でも聞きますよ！"

# --- チャット履歴の初期化（Streamlitのセッション状態を利用） ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": INITIAL_MESSAGE}
    ]

# 過去の会話履歴を画面に表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- ユーザーからのメッセージ入力 ---
if prompt := st.chat_input("ここに愚痴やメッセージを入力..."):
    # 1. ユーザーの入力内容を画面に表示 & 履歴に追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. AIの返答を生成（ここではランダム共感＋オウム返し）
    # ※特定のキーワードに反応するロジックも追加可能！
    if "疲れた" in prompt or "しんどい" in prompt:
        ai_reply = "本当にお疲れ様です…！無理しないで温かいお風呂に入って早めに休んでくださいね 🍵"
    elif "上司" in prompt or "会社" in prompt:
        ai_reply = "お仕事関係のお悩みですね…！組織の中で上手くやるのって本当に大変ですよね。話してスッキリしてください！"
    else:
        ai_reply = random.choice(EMPATHY_RESPONSES)

    # 3. AIの返答をタイピング風に表示 & 履歴に追加
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # 1文字ずつパラパラ表示する（演出）
        for char in ai_reply:
            full_response += char
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.05)
        message_placeholder.markdown(full_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )