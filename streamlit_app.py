import streamlit as st
import random

def generate_fortune():
    fortunes = [
        "しまれがんばれねばれおしきれ。今日のあなたは舞鶴魂にとりつかれるでしょう",
        "由々しき事態です。今のあなたには勉強時間が足りなさすぎる",
        "課題課題課題課題課題課題課題課題課題課題題題課題課題課題課題課題",
        "あなたは計画性がないです。計画をたてて、今後の戦に備えましょう。",
        "その日は必ず来ますが、まだ先になりそうです。別のその日を探しましょう。",
        "舞鶴プライドが高すぎます。もっと他人を尊重しましょう。",
        "あなたは休みすぎです。そんなあなたには、サタセミの受講をおすすめします。"
    ]
    colors = ["赤", "青", "緑"]
    subjects = ["論国", "古典", "言文", "現国", "数１", "数２", "数３", "数A", "数B", "数C", "C英", "E英", "化学", "物理", "生物", "日本史", "地理", "世界史", "公共", "体育", "家庭科", "情報", "舞ステ", "書道", "音楽", "美術"]
    year = random.randint(1, 100)
    subject = random.choice(subjects)
    
    fortune = random.choice(fortunes)
    color = random.choice(colors)
    return fortune, color, year, subject

# Streamlit UI
st.title("omzh占い")
st.write("ようこそomzh占いへ。ここではあなたの運勢を、信頼できない私が占ってみせましょう。信じれば、あたります。この占いについて、悪い評価をした場合には、１０００万の罰金を科すのでご了承ください。")

if "fortune" not in st.session_state:
    st.session_state.fortune = ""
    st.session_state.color = ""
    st.session_state.year = ""
    st.session_state.subject = ""

def show_fortune():
    fortune, color, year, subject = generate_fortune()
    st.session_state.fortune = fortune
    st.session_state.color = color
    st.session_state.year = year
    st.session_state.subject = subject

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
    st.write(f"#### 今日の教科: {st.session_state.subject}")
    
    if st.button("もう一度占う"):
        show_fortune()
