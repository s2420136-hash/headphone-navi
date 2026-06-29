import streamlit as st
import pandas as pd

# 1. 商品データの定義（新田さんのCSVデータを基に作成）
products = [
    {"name": "Marshall MAJOR V", "actual_price": 19980, "price": 8, "review": 8, "use": 9, "sound": 9, "comfort": 10, "usage": "音楽鑑賞・映画", "genre": "ロック・クラシック", "reason": "軽量で長時間利用しやすく、操作もわかりやすいため初心者に向いている"},
    {"name": "Sony WH-CH520", "actual_price": 7700, "price": 10, "review": 4, "use": 9, "sound": 7, "comfort": 10, "usage": "通学・勉強", "genre": "J-pop", "reason": "操作が簡単で装着感も良く、ヘッドホンデビュー向け"},
    {"name": "audio-technica ATH-S220BT", "actual_price": 6490, "price": 10, "review": 4, "use": 9, "sound": 7, "comfort": 10, "usage": "通学・勉強", "genre": "J-pop・アニソン", "reason": "価格はやや高めだが音質とバッテリー性能が高く、長く使いたい初心者向け"},
    {"name": "Sony WH-CH720N", "actual_price": 18810, "price": 8, "review": 4, "use": 9, "sound": 8, "comfort": 10, "usage": "通学・勉強・作業", "genre": "なんでも", "reason": "ノイキャン搭載で移動中や作業中も快適。軽量で初心者でも使いやすい"},
    {"name": "Sony ULT WEAR (WH-ULT900N)", "actual_price": 33000, "price": 2, "review": 8, "use": 8, "sound": 10, "comfort": 8, "usage": "音楽鑑賞・通学", "genre": "ロック・EDM", "reason": "重低音とノイズキャンセリングが特徴。音楽を迫力ある音で楽しみたい初心者向け。"}
]

# アプリのタイトル
st.title("🎧 ヘッドフォンナビ")
st.subheader("〜レビュー翻訳で失敗しない選び方〜")
st.write("いくつかの質問に答えるだけで、あなたにピッタリの「失敗しないヘッドフォン」を提案します！")
st.caption("※価格は目安です。販売店や時期によって変わる場合があります。")

st.divider()

# ユーザーの重視度（重み）の初期化
w_use = 0
w_comfort = 0
w_price = 0
w_sound = 0
w_review = 0

# --- 質問パート（新田さんの設計を再現） ---
st.header("📋 診断質問")

q1 = st.selectbox("Q1. 主にどんな場面で使いますか？", ["通学・電車", "勉強・作業", "ゲーム", "映画・動画鑑賞", "音楽をじっくり楽しみたい"])
if q1 == "通学・電車":
    w_use += 10
    w_comfort += 5
    w_review += 5
elif q1 == "勉強・作業":
    w_comfort += 10
    w_use += 5
elif q1 == "ゲーム":
    w_use += 10
    w_sound += 5
elif q1 == "映画・動画鑑賞":
    w_sound += 10
    w_comfort += 5
elif q1 == "音楽をじっくり楽しみたい":
    w_sound += 15

q2 = st.selectbox("Q2. いちばん不安なのはどれですか？", ["高すぎて失敗すること", "音が思っていたのと違うこと", "長時間つけて疲れること", "接続がうまくいかないこと"])
if q2 == "高すぎて失敗すること": w_price += 10
elif q2 == "音が思っていたのと違うこと": w_sound += 10
elif q2 == "長時間つけて疲れること": w_comfort += 10
elif q2 == "接続がうまくいかないこと": w_review += 10

q3 = st.multiselect("Q3. よく聴く音楽は？（複数選択可）", ["J-POP・アニソン・女性ボーカル", "ロック・バンド", "HIPHOP・EDM", "クラシック・映画音楽", "特に決まっていない"])
if "J-POP・アニソン・女性ボーカル" in q3:
    w_sound += 5
    w_review += 3

if "ロック・バンド" in q3:
    w_sound += 8

if "HIPHOP・EDM" in q3:
    w_sound += 10

if "クラシック・映画音楽" in q3:
    w_sound += 8
    w_comfort += 3

if "特に決まっていない" in q3:
    w_review += 5

q4 = st.radio("Q4. 音のイメージはどちらが好みですか？", ["迫力がある・重低音が強い", "ボーカルがはっきり聞こえる", "バランスよく自然", "よくわからない"])
if q4 == "迫力がある・重低音が強い":
    w_sound += 10
elif q4 == "ボーカルがはっきり聞こえる":
    w_sound += 8
    w_review += 3
elif q4 == "バランスよく自然":
    w_sound += 7
    w_review += 5
elif q4 == "よくわからない":
    w_review += 5

q5 = st.radio("Q5. 電車や外で使う予定はありますか？", ["よくある", "ときどきある", "ほとんどない"])
if q5 == "よくある": w_use += 5

q6 = st.radio("Q6. 1回の使用時間はどれくらい？", ["30分以内", "1〜2時間", "3時間以上"])
if q6 == "3時間以上": w_comfort += 10
elif q6 == "1〜2時間": w_comfort += 5

q7 = st.radio("Q7. ゲームや動画で「音と映像のズレ」は気になりますか？", ["とても気になる", "少し気になる", "あまり気にしない"])
if q7 == "とても気になる": w_use += 5

q8 = st.radio("Q8. 価格の目安は？", ["1万円以下がいい", "1〜2万円くらい", "2万円以上でもOK"])
if q8 == "1万円以下がいい": w_price += 15
elif q8 == "1〜2万円くらい": w_price += 8

q9 = st.radio("Q9. 見た目はどのくらい重視しますか？", ["とても重視する", "ある程度重視する", "あまり気にしない"])
# 見た目は直接スコアにないため、こだわり度として全体に少し影響させるか、今回はMarshall等の特定ブランドに裏で加点するロジックも組めます（今回はシンプルに維持）

q10 = st.radio("Q10. 初めて買うので、どれが安心ですか？", ["レビューが多く評価が安定しているもの", "有名ブランド", "とにかくコスパが良いもの", "わかりやすく説明されているもの"])
if q10 == "レビューが多く評価が安定しているもの": w_review += 10
elif q10 == "とにかくコスパが良いもの": w_price += 5

st.divider()

# --- 推薦ロジックの計算パート ---
if st.button("✨ 診断結果を見る"):
    st.header("🏆 あなたにおすすめのヘッドフォン TOP3")
    st.caption(
    "失敗しにくさ適合度は、価格・用途・音の好み・装着感・"
    "レビューの条件が、あなたの回答にどれくらい合っているかを表す診断スコアです。"
    "商品の性能や品質を直接評価した点数ではありません。"
    )
    # 各商品の適合度スコアを計算
    scored_products = []
    for p in products:
        # 適合度 = (商品スコア * ユーザーの重み) の総和
        score = (p["price"] * w_price) + (p["review"] * w_review) + (p["use"] * w_use) + (p["sound"] * w_sound) + (p["comfort"] * w_comfort)
        
        if q8 == "1万円以下がいい" and p["actual_price"] > 10000:
            continue

        if q8 == "1〜2万円くらい" and not (10000 <= p["actual_price"] <= 20000):
            continue

        # 画面表示用にデータをコピー
        p_score = p.copy()
        p_score["match_score"] = score
        scored_products.append(p_score)
    
    # スコアが高い順にソートしてTOP3を抽出
    top_3 = sorted(scored_products, key=lambda x: x["match_score"], reverse=True)[:3]
    
    # 結果の表示
    for rank, item in enumerate(top_3, 1):
        st.subheader(f"第{rank}位: {item['name']}")
        match_reasons = []

    if q8 == "1万円以下がいい" and item["actual_price"] <= 10000:
        match_reasons.append("希望する予算内")

    if q6 == "3時間以上" and item["comfort"] >= 8:
        match_reasons.append("長時間でも使いやすい")

    if q5 == "よくある" and item["use"] >= 8:
        match_reasons.append("外出や通学に向いている")

    if match_reasons:
        st.success("あなたに合うポイント：" + "・".join(match_reasons))
    col1, col2 = st.columns(2)
    with col1:
            st.write(f"**価格目安:** {item['actual_price']:,}円")
            st.write(f"**主な用途:** {item['usage']}")
            st.write(f"**得意なジャンル:** {item['genre']}")
    with col2:
            st.write(f"**失敗しにくさ適合度:** {item['match_score']} 点")
        
    st.info(f"💡 **初心者へのおすすめ理由:**\n{item['reason']}")
    st.divider()
