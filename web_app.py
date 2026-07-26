import streamlit as st
import datetime

# ページの設定
st.set_page_config(page_title="マイ Web アプリ", page_icon="🚀")

# タイトル
st.title("🚀 はじめての Python Web アプリ")
st.write("Streamlit を使うと、Python だけで簡単に Web アプリが作れます！")

# ユーザー入力（テキストボックス）
name = st.text_input("あなたの名前を入力してください:")

if name:
    st.success(f"こんにちは、**{name}** さん！")

# インタラクティブな要素（スライダー）
st.subheader("📊 今日の調子はどうですか？")
feeling = st.slider("気分をパーセントで選択:", 0, 100, 50)
st.write(f"現在のモチベーション: **{feeling}%**")

# ボタンとアクション
if st.button("今日の日付を表示"):
    today = datetime.date.today()
    st.info(f"今日は **{today}** です！")