from pathlib import Path

import pandas as pd
import streamlit as st


products = [
    {
        "name": "Marshall MAJOR V",
        "actual_price": 19980,
        "price": 8,
        "review": 8,
        "use": 9,
        "sound": 9,
        "comfort": 8,
        "ease": 8,
        "usage": "音楽鑑賞・通勤・通学",
        "usage_tags": ["通勤・通学", "音楽鑑賞"],
        "genre": "ロック・バンド",
        "genre_tags": ["ロック・バンド"],
        "sound_profiles": ["迫力がある・重低音が強い"],
        "noise_canceling": False,
        "wired": True,
        "ai_reason": "長時間使えるバッテリーと折りたたみやすいデザインが特徴です。",
        "image": "image/imgrc0107048115.webp",
        "best_for": "デザインとバッテリー性能を重視する人",
        "review_good": "バッテリーが長持ちし、持ち運びやすい点が魅力です。",
        "review_bad": "ノイズキャンセリングを重視する人には向いていません。",
        "review_translation": "充電の手間を減らしたい人向けですが、電車内の騒音対策を重視する場合は注意が必要です。",
        "review_source": "Marshall公式製品情報を初心者向けに要約",
    },
    {
        "name": "Sony WH-CH520",
        "actual_price": 7700,
        "price": 10,
        "review": 4,
        "use": 9,
        "sound": 7,
        "comfort": 9,
        "ease": 9,
        "usage": "通勤・通学・勉強",
        "usage_tags": ["通勤・通学", "勉強・作業"],
        "genre": "J-POP・アニソン",
        "genre_tags": ["J-POP・アニソン・女性ボーカル"],
        "sound_profiles": ["ボーカルがはっきり聞こえる", "バランスよく自然"],
        "noise_canceling": False,
        "wired": False,
        "ai_reason": "価格を抑えながら、基本的な機能を使いやすくまとめたモデルです。",
        "image": "image/01_43b793100.jpg",
        "best_for": "初めてのワイヤレスヘッドフォンを低価格で試したい人",
        "review_good": "軽く、ボタン操作が分かりやすく、バッテリーも長持ちします。",
        "review_bad": "ノイズキャンセリング機能は搭載されていません。",
        "review_translation": "操作の簡単さを重視する初心者向けですが、騒がしい場所での使用には注意が必要です。",
        "review_source": "Sony公式製品情報を初心者向けに要約",
    },
    {
        "name": "audio-technica ATH-S220BT",
        "actual_price": 6490,
        "price": 10,
        "review": 4,
        "use": 9,
        "sound": 7,
        "comfort": 9,
        "ease": 8,
        "usage": "通勤・通学・勉強・オンライン授業",
        "usage_tags": ["通勤・通学", "勉強・作業", "ゲーム"],
        "genre": "J-POP・アニソン",
        "genre_tags": ["J-POP・アニソン・女性ボーカル"],
        "sound_profiles": ["ボーカルがはっきり聞こえる", "バランスよく自然"],
        "noise_canceling": False,
        "wired": True,
        "ai_reason": "軽量で、有線とワイヤレスの両方に対応しています。",
        "image": "image/branch_3114_image_27.jpg",
        "best_for": "低価格とバッテリー性能、有線接続を重視する人",
        "review_good": "軽量で、最大約60時間使える点が魅力です。",
        "review_bad": "ノイズキャンセリング機能はなく、対応コーデックはSBCです。",
        "review_translation": "勉強やオンライン授業には使いやすい一方、高機能な騒音対策を求める人には物足りない場合があります",
        "review_source": "audio-technica公式製品情報を初心者向けに要約",
    },
    {
        "name": "Sony WH-CH720N",
        "actual_price": 18810,
        "price": 8,
        "review": 4,
        "use": 9,
        "sound": 8,
        "comfort": 10,
        "ease": 8,
        "usage": "通勤・通学・勉強・作業",
        "usage_tags": ["通勤・通学", "勉強・作業", "映画・動画", "音楽鑑賞"],
        "genre": "幅広いジャンル",
        "genre_tags": [
            "J-POP・アニソン・女性ボーカル",
            "ロック・バンド",
            "クラシック・映画音楽",
        ],
        "sound_profiles": ["ボーカルがはっきり聞こえる", "バランスよく自然"],
        "noise_canceling": True,
        "wired": True,
        "ai_reason": "軽量で、ノイズキャンセリングにも対応しています。",
        "image": "image/WH-CH720N.jpg",
        "best_for": "電車や集中したい場所で長時間使いたい人",
        "review_good": "軽さとノイズキャンセリングを両立し、長時間使いやすいモデルです。",
        "review_bad": "1万円以下の商品と比べると価格が高くなります。",
        "review_translation": "価格よりも、騒音対策と装着感を重視する初心者に向いています。",
        "review_source": "Sony公式製品情報を初心者向けに要約",
    },
    {
        "name": "Sony ULT WEAR (WH-ULT900N)",
        "actual_price": 33000,
        "price": 2,
        "review": 8,
        "use": 8,
        "sound": 10,
        "comfort": 8,
        "ease": 7,
        "usage": "音楽鑑賞・通勤・通学",
        "usage_tags": ["通勤・通学", "音楽鑑賞", "映画・動画"],
        "genre": "ロック・HIPHOP・EDM",
        "genre_tags": ["ロック・バンド", "HIPHOP・EDM"],
        "sound_profiles": ["迫力がある・重低音が強い"],
        "noise_canceling": True,
        "wired": True,
        "ai_reason": "迫力のある重低音とノイズキャンセリングが特徴です。",
        "image": "image/alljapan-online-shop_4548736156425.jpg",
        "best_for": "重低音と迫力を最優先したい人",
        "review_good": "重低音の迫力があり、ノイズキャンセリングにも対応しています。",
        "review_bad": "自然で控えめな低音を好む人には、低音が強すぎる可能性があります。",
        "review_translation": "ライブのような迫力を楽しみたい人向けですが、音のバランスを重視する場合は試聴がおすすめです。",
        "review_source": "Sony公式製品情報を初心者向けに要約",
    },
]


# ここに追加する
def make_ai_reason(item, q1, q2, q3, q5, q7):
    reasons = []

    if q7 == "1万円以下がいい" and item["actual_price"] <= 10000:
        reasons.append("予算を抑えたい人に選びやすい価格です")
    elif q7 == "1〜2万円くらい" and item["actual_price"] <= 20000:
        reasons.append("希望する価格帯に近く、購入候補にしやすいです")

    matched_usage = []
    for use in q1:
        if use in item["usage_tags"]:
            matched_usage.append(use)

    if matched_usage:
        reasons.append(f"{'・'.join(matched_usage)}で使いやすい特徴があります")

    if q3 in item["sound_profiles"]:
        reasons.append(f"{q3}音が好みの人に向いています")

    if q5 == "3時間以上" and item["comfort"] >= 8:
        reasons.append("長時間でも使いやすい点が魅力です")

    review_point = item["review_translation"]

    if reasons:
        main_reason = "、".join(reasons[:2])
        return f"{item['name']}は、{main_reason}。{review_point}"
    else:
        return f"{item['name']}は、{item['usage']}に使いやすいヘッドフォンです。{review_point}"
    
st.title("🎧 ヘッドフォンナビ")
st.subheader("レビュー・製品情報を初心者向けに翻訳")
st.write("いくつかの質問から、あなたに合うヘッドフォン選びをサポートします。")
st.caption("※価格は目安です。販売店や時期によって変わる場合があります。")
st.divider()

st.header("📋 診断質問")

q1 = st.multiselect(
    "Q1. 主にどんな場面で使いますか？（複数選択可）",
    [
        "通勤・通学",
        "勉強・作業",
        "音楽鑑賞",
        "映画・動画",
        "ゲーム",
        "ランニング・ウォーキング",
    ],
)

q2 = st.multiselect(
    "Q2. よく聴く音楽は？（複数選択可）",
    [
        "J-POP・アニソン・女性ボーカル",
        "ロック・バンド",
        "HIPHOP・EDM",
        "クラシック・映画音楽",
        "特に決まっていない",
    ],
)

q3 = st.radio(
    "Q3. 音のイメージはどちらが好みですか？",
    [
        "迫力がある・重低音が強い",
        "ボーカルがはっきり聞こえる",
        "バランスよく自然",
        "よくわからない",
    ],
)

q4 = st.radio(
    "Q4. 電車や外で使う予定はありますか？",
    [
        "よくある",
        "ときどきある",
        "ほとんどない",
    ],
)

q5 = st.radio(
    "Q5. 1回の使用時間はどれくらいですか？",
    [
        "30分以内",
        "1〜2時間",
        "3時間以上",
    ],
)

q6 = st.radio(
    "Q6. ゲームや動画で音と映像のズレは気になりますか？",
    [
        "とても気になる",
        "少し気になる",
        "あまり気にならない",
        "全く気にならない",
    ],
)

q7 = st.radio(
    "Q7. 価格の目安は？",
    [
        "1万円以下がいい",
        "1〜2万円くらい",
        "2万円以上でもOK",
    ],
)

q8 = st.radio(
    "Q8. 初めて買う際、特に重視するものは？",
    [
        "レビュー評価",
        "価格の安さ",
        "装着感",
        "操作の分かりやすさ",
    ],
)

st.divider()

if st.button("✨ 診断結果を見る", type="primary"):
    weights = {
        "price": 5,
        "review": 5,
        "use": 5,
        "sound": 5,
        "comfort": 5,
        "ease": 5,
    }

    # Q4 外で使う予定
    if q4 == "よくある":
        weights["use"] += 5

    # Q5 使用時間
    if q5 == "1〜2時間":
        weights["comfort"] += 5
    elif q5 == "3時間以上":
        weights["comfort"] += 10

    # Q8 初めて買う際に重視するもの
    priority_weights = {
        "レビュー評価": "review",
        "価格の安さ": "price",
        "装着感": "comfort",
        "操作の分かりやすさ": "ease",
    }
    weights[priority_weights[q8]] += 10

    scored_products = []
    selected_genres = [genre for genre in q2 if genre != "特に決まっていない"]

    for product in products:
        # Q7 価格フィルター
        if q7 == "1万円以下がいい" and product["actual_price"] > 10000:
            continue

        if q7 == "1〜2万円くらい" and not 10000 <= product["actual_price"] <= 20000:
            continue

        base_score = sum(product[key] * weight for key, weight in weights.items())
        max_score = 10 * sum(weights.values())

        usage_bonus = 0
        if q1:
            usage_matches = len(set(q1) & set(product["usage_tags"]))
            usage_bonus = 20 * usage_matches / len(q1)
            max_score += 20

        genre_bonus = 0
        if selected_genres:
            genre_matches = len(set(selected_genres) & set(product["genre_tags"]))
            genre_bonus = 15 * genre_matches / len(selected_genres)
            max_score += 15

        sound_bonus = 0
        if q3 != "よくわからない":
            sound_bonus = 10 if q3 in product["sound_profiles"] else 2
            max_score += 10

        outdoor_bonus = 0
        if q4 == "よくある":
            outdoor_bonus = 10 if product["noise_canceling"] else 3
            max_score += 10
        elif q4 == "ときどきある":
            outdoor_bonus = 5 if product["noise_canceling"] else 2
            max_score += 5

        latency_bonus = 0
        if q6 == "とても気になる":
            latency_bonus = 5 if product["wired"] else 0
            max_score += 5
        elif q6 == "少し気になる":
            latency_bonus = 3 if product["wired"] else 0
            max_score += 3

        raw_score = base_score + usage_bonus + genre_bonus + sound_bonus + outdoor_bonus + latency_bonus
        match_score = round(raw_score / max_score * 100)

        scored_product = product.copy()
        scored_product["match_score"] = min(match_score, 100)
        scored_products.append(scored_product)

    top_products = sorted(
        scored_products,
        key=lambda item: item["match_score"],
        reverse=True,
    )[:3]

    result_count = len(top_products)

    if result_count == 0:
        st.warning("選択した価格帯に該当する商品がありません。")
    else:
        st.header(f"🏆 あなたへのおすすめ TOP{result_count}")
        st.caption(
            "適合度は、予算・用途・装着感・音の好みなどと商品の特徴との一致度です。"
            "商品の品質そのものを評価した点数ではありません。"
        )

        comparison_rows = []

        for rank, item in enumerate(top_products, 1):
            with st.container(border=True):
                st.subheader(f"第{rank}位　{item['name']}")

                image_col, detail_col = st.columns([1, 2])

                with image_col:
                    image_path = Path(item["image"])
                    if image_path.exists():
                        st.image(str(image_path), use_container_width=True)
                    else:
                        st.caption("商品画像を準備中です。")

                with detail_col:
                    st.write(f"**価格目安：** {item['actual_price']:,}円")
                    st.write(f"**適合度：** {item['match_score']}／100点")
                    st.write(f"**向いている人：** {item['best_for']}")

                match_reasons = []

                if q7 == "1万円以下がいい" and item["actual_price"] <= 10000:
                    match_reasons.append("希望する予算内")

                if q5 == "3時間以上" and item["comfort"] >= 8:
                    match_reasons.append("長時間利用に向いている")

                if set(q1) & set(item["usage_tags"]):
                    match_reasons.append("希望する利用場面と一致")

                if q4 == "よくある" and item["noise_canceling"]:
                    match_reasons.append("屋外で使いやすいノイズキャンセリング対応")

                if match_reasons:
                    st.success("あなたに合うポイント：" + "・".join(match_reasons))

                ai_reason = make_ai_reason(item, q1, q2, q3, q5, q7)
                st.info(f"**AI推薦理由：** {ai_reason}")

                st.markdown("#### 製品情報を初心者向けに翻訳")
                st.write(f"**良かった点：** {item['review_good']}")
                st.write(f"**気になる点：** {item['review_bad']}")
                st.write(f"**つまり：** {item['review_translation']}")
                st.caption(item["review_source"])

            comparison_rows.append(
                {
                    "順位": rank,
                    "商品名": item["name"],
                    "価格": f"{item['actual_price']:,}円",
                    "適合度": f"{item['match_score']}／100",
                    "向いている人": item["best_for"],
                    "気になる点": item["review_bad"],
                }
            )

        st.subheader("商品の比較")
        st.dataframe(
            pd.DataFrame(comparison_rows),
            hide_index=True,
            use_container_width=True,
        )