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
    return random.choice(fortunes)

def generate_color():
    return random.choice(["赤", "青", "緑"])

def generate_year():
    return random.randint(1, 100)

def generate_maizuru_spirit():
    options = ["しまれ", "がんばれ", "ねばれ", "おしきれ"]
    return random.sample(options, random.randint(1, 4))

def generate_subject():
    subjects = ["数１", "数２", "数３", "数A", "数B", "数C", "現国", "言語文化", "論国", "古典", "文学", "C英", "論表", "物理", "生物", "化学", "日本史", "地理", "世界史", "公共", "情報", "舞ステ", "家庭科", "書道", "音楽", "美術", "体育"]
    return random.choice(subjects)

def generate_power_spot():
    spots = ["教室", "体育館", "駐輪場", "グラウンド", "多目的", "テニスコート", "プール", "同窓会館", "而立会館", "昇降口", "図書館", "進路指導室", "会議室", "事務室", "購買", "渡り廊下", "自学の道", "トイレ", "保健室", "化学室", "物理室", "生物室", "地歴教室", "数学教室", "コンピューター室", "ゴミ捨て場", "茶道室", "武道場", "被服室", "調理室", "職員室", "書道室", "音楽室", "美術室", "視聴覚室", "放送室"]
    return random.choice(spots)

st.title("omzh占い")
st.write("ようこそomzh占いへ。ここではあなたの運勢を、信頼できない私が占ってみせましょう。信じれば、あたります。この占いについて、悪い評価をした場合には、１０００万の罰金を科すのでご了承ください。")

if st.button("占う", key="fortune_button", help="占いを生成します"):
    st.session_state.fortune = generate_fortune()
    st.session_state.color = generate_color()
    st.session_state.year = generate_year()
    st.session_state.spirit = generate_maizuru_spirit()
    st.session_state.subject = generate_subject()
    st.session_state.spot = generate_power_spot()

if "fortune" in st.session_state:
    st.subheader("占いの結果")
    st.write(f"**{st.session_state.fortune}**")
    st.write(f"今日の学年カラー: {st.session_state.color}")
    st.write(f"今日のあなたは… {st.session_state.year}回生")
    st.write(f"今日の舞鶴魂: {', '.join(st.session_state.spirit)}")
    st.write(f"今日の教科: {st.session_state.subject}")
    st.write(f"今日のパワースポット: {st.session_state.spot}")
    if st.button("もう一度占う", key="retry_button"):
        st.session_state.clear()
