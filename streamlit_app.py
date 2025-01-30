import streamlit as st
import random

def generate_fortune():
    fortunes = [
        "しまれがんばれねばれおしきれ。今日のあなたには舞鶴魂があるので、安心してください",
        "由々しき事態です。今のあなたには勉強時間が足りなさすぎる",
        "課題課題課題課題課題課題課題課題課題課題題題課題課題課題課題課題",
        "あなたは計画性がないです。計画をたてて、今後の戦に備えましょう。",
        "その日は必ず来ますが、まだ先になりそうです。別のその日を探しましょう。",
        "舞鶴プライドが高すぎます。もっと他人を尊重し、適切な舞鶴プライドを保ちましょう。",
        "あなたは休みすぎです。そんなあなたには、サタセミの受講をおすすめします。",
        "あなたは今日誰かに怒られる可能性が高いです。あなたの知らないところで誰かがぶちぎれています",
        "数学を解いても、あなたが考えるほど簡単な答えではないでしょう。まだ修行が足りません。",
        "あなたはいつでもいつまでも三年ｎ学期です。ｎが自然数だと思ったあなたは退学です。",
        "あなたはいつもの１０２４倍かわいいです。つまり普段は､､､？",
        "今日のあなたは言語道断です。勉強をして、勉強をして、そして勉強してください。"、
        "あなたは道から外れています。自学の道を訪れましょう。"、
        "今日はあなたの魅力が絶好調。朝日に映えてそびえたつでしょう。"、
        "あなたは運動不足です。開閉ジャンプを20回しましょう。"、
        "あなたは感謝が足りません。道を譲ってもらったらお辞儀をしましょう。"、
        "明日の昼ごはんは私が決めます。舞鶴高校3階で販売される唐揚げ弁当を買いましょう。"、
        "今日あなたは10人程度友達をなくすでしょう。フレンドのからむすを食べると良いでしょう。"、
        "今日のあなたは寒いです。土手ランをして熱くなりましょう。"、
        "勉強せずに占いをするとはちゃんちゃらおかしいです。"、
        "ケシカスの出し過ぎに要注意。押し花ならぬオシカスで趣深い生活を心がけて。"、
        "今日は絶好の船日和です。ドラゴンボートに乗りましょう。"、
        "黒板が曲がっています。うねうねしないようにしましょう。"
   
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
