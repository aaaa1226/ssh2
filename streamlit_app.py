import streamlit as st
import random

def generate_fortune():
    fortunes = [
        "しまれねばれがんばれおしきれ。今日のあなたには舞鶴魂があるので、安心してください。",
        "由々しき事態です。今のあなたには勉強が足りません。",
        "課題課題課題課題課題課題課題課題課題課題",
        "あなたは計画性がないです。計画を立てて今後の戦に備えましょう。",
        "その日は必ず来ますが、まだ先になりそうです。別のその日を迎えましょう。",
    ]
    
    
    colors = ["赤", "青", "緑"]
    year = random.randint(1, 100)
    
    fortune = random.choice(fortunes)
    color = random.choice(colors)
    return fortune, color, year

# Streamlit UI
st.title("omzh占い")
st.write("ようこそomzh占いへ。ここではあなたの運勢を、信頼できない私が占ってみせましょう。信じれば、あたります。この占いについて、悪い評価をした場合には、１０００万の罰金を科すのでご了承ください。")

if "fortune" not in st.session_state:
    st.session_state.fortune = ""
    st.session_state.color = ""
    st.session_state.year = ""

def show_fortune():
    fortune, color, year = generate_fortune()
    st.session_state.fortune = fortune
    st.session_state.color = color
    st.session_state.year = year

# 占うボタン（丸くするためにCSSを追加）
st.markdown("""
    <style>
        div.stButton > button:first-child {
            border-radius: 50px;
            width: 100px;
            height: 100px;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

if st.button("占う"):
    show_fortune()

if st.session_state.fortune:
    st.write(f"### {st.session_state.fortune}")
    st.write(f"#### 今日の学年カラー: {st.session_state.color}")
    st.write(f"#### 今日のあなたは…{st.session_state.year}回生")
    
    if st.button("もう一度占う"):
        show_fortune()
