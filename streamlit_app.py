import streamlit as st
import random

def generate_fortune():
    fortunes = [
        "しまれねばれがんばれおしきれ。今日のあなたには舞鶴魂があるので、安心してください。",
        "由々しき事態です。今のあなたには勉強が足りません。",
        "課題課題課題課題課題課題課題課題課題課題",
        "あなたは計画性がないです。計画を立てて今後の戦に備えましょう。",
        "その日は必ず来ますが、まだ先になりそうです。別のその日を迎えましょう。",
        "舞鶴プライドが高すぎます。もっと他人を尊重し、適切な舞鶴プライドを保ちましょう。",
        "あなたは休みすぎです。そんなあなたには、サタセミの受講をおすすめします。",
        "あなたは今日誰かに怒られる可能性が高いです。あなたにの知らないところで誰かがブチギレています。",
        "数学を解いても、あなたが考えるほど簡単ではありません。まだ修行が足りません。",
        "あなたはいつもいつまでも三年n学期です。nが自然数だと思ったあなたは退学です。",
        "あなたはいつもの1024倍かわいいです。つまり普段は､､､？",
        "今日のあなたは言語道断です。勉強して、勉強して勉強しましょう。",
        "あなたは道から外れています。自学の道を訪れましょう",
        "今日はあなたの魅力が絶好調。朝日に映えてそびえたつでしょう。",
        "あなたは運動不足です。開閉ジャンプを20回しましょう。",
        "あなたは感謝が足りません。道を譲ってもらったらお辞儀をしましょう。",
        "明日のお昼ご飯は私が決めます。舞鶴高校3階で販売される唐揚げ弁当を買いましょう。",
        "今日あなたは10人程度友達をなくします。フレンドのからむすを食べると良いでしょう。",
        "今日のあなたは寒いです。土手ランをして熱くなりましょう。",
        "勉強せずに占いをするとはちゃちゃらおかしいです。",
        "ケシカスの出し過ぎに注意。押し花ならぬオシカスで趣深い生活を心がけて。",
        "今日は絶好の船日和ですドラゴンボートに乗りましょう。",
        "黒板が曲がっています。うねうねしないようにしましょう。"

    ]
    
    
    colors = ["赤", "青", "緑"]
    year = random.randint(1, 100)
    tamasii = ["しまれ","ねばれ","がんばれ","おしきれ","しまれねばれ","しまれがんばれ","しまれおしきれ",
               "しまれおしきれ","ねばれがんばれ","ねばれおしきれ","がんばれおしきれ","しまれがんばれねばれ","しまれがんばれおしきれ",
               "がんばれねばれおしきれ","しまれがんばれねばれおしきれ",]
    kyouka = ["数１","数２","数３","数A","数B","数C","現国","言語文化","論国","古典","文学",
              "C英","論表","物理","生物","化学","日本史","地理","世界史","公共","情報","舞ステ","家庭科","書道","音楽","美術",
              "体育"]
    spot = ["教室","体育館","駐輪場","グラウンド","多目的","体育館","テニスコート","プール","同窓会館","而立会館",
            "昇降口","図書館","進路指導室","会議室","事務室","購買","渡り廊下","自学の道","トイレ","保健室",
            "化学室","物理室","生物室","地歴教室","数学教室","コンピューター室","ゴミ捨て場","茶道室","武道場",
            "コンピューター室","被服室","調理室","職員室","書道室","音楽室","美術室","音楽室","視聴覚室","放送室",]
    item = ["シャーペン","消しゴム","ジェットストリーム","舞鶴帽子","舞鶴扇子","購買のパン","イチゴオレ","鯛茶漬け",
            "ドデカミン","学ラン","カーディガン","校章","スリッパ","お弁当","日替わり弁当","かつ丼","あゆみ","学習時間調査",
            "自転車","体操服","鉛筆","進研模試","全統模試","テストの答案","iPad","教科書","化学セミナー","良問の風","サクシード",
            "Leap","Be","Engage","古語単","現単","パンダ","レジェンド","生物ノート","ルーズリーフ","体育館シューズ","イヤホン",
            "唐揚げ","合服",]    
    fortune = random.choice(fortunes)
    color = random.choice(colors)
    maizuru = random.choice(tamasii)
    subjects = random.choice(kyouka)
    spots = random.choice(spot)
    items = random.choice(item)
    return fortune, color, year, maizuru, subjects, spots, items

# Streamlit UI
st.title("omzh占い")
st.write("ようこそomzh占いへ。ここではあなたの運勢を、信頼できない私が占ってみせましょう。信じれば、あたります。この占いについて、悪い評価をした場合には、１０００万の罰金を科すのでご了承ください。")

if "fortune" not in st.session_state:
    st.session_state.fortune = ""
    st.session_state.color = ""
    st.session_state.year = ""
    st.session_state.maizuru = ""
    st.session_state.subjects = ""
    st.session_state.spots = ""
    st.session_state.items = ""

def show_fortune():
    fortune, color, year, maizuru, subjects, spots, items = generate_fortune()
    st.session_state.fortune = fortune
    st.session_state.color = color
    st.session_state.year = year
    st.session_state.maizuru = maizuru
    st.session_state.subjects = subjects
    st.session_state.spots = spots
    st.session_state = items

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
    st.write(f"#### ❤️今日の学年カラー: {st.session_state.color}")
    st.write(f"#### ❤️今日のあなたは…{st.session_state.year}回生")
    st.write(f"#### ❤️今日の舞鶴魂:{st.session_state.maizuru}")
    st.write(f"#### ❤️勉強してください:{st.session_state.subjects}")
    st.write(f"#### ❤️パワースポット:{st.session_state.spots}")
    st.write(f"#### ❤️ラッキーアイテム:{st.session_state.items}")
    
    if st.button("もう一度占う"):
        show_fortune()
