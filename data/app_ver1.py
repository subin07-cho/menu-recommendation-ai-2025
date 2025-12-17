import gradio as gr
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split

# =========================
# 1. 데이터 로드 (HF용)
# =========================
df = pd.read_excel("Restaurants.xlsx")
df['가격대'] = pd.to_numeric(df['가격대'], errors='coerce')

# =========================
# 2. ML 모델 (LightGBM)
# =========================
ideal_budget = 12000
df['budget_diff'] = abs(df['가격대'] - ideal_budget)

df['label'] = np.where(
    (df['평점'] >= 4.0) & (df['budget_diff'] <= 3000),
    1, 0
)

df_ml = pd.get_dummies(df, columns=['음식종류', '연령층', '방문목적'])
X = df_ml.drop(columns=['식당명', '리뷰', '위치(지하철역)', 'label'])
y = df_ml['label']

X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

model = lgb.LGBMClassifier(n_estimators=300, learning_rate=0.05, force_col_wise=True)
model.fit(X_train, y_train)

df['predict_score'] = model.predict_proba(X)[:, 1]

# =========================
# 3. 메뉴 맵
# =========================
menu_map = {
    "양식": {"밥": [], "면": ["파스타", "크림파스타"], "국물": [], "튀김": ["치킨"], "구이": ["스테이크"]},
    "일식": {"밥": ["초밥"], "면": ["라멘"], "국물": ["나베"], "튀김": ["가라아게"], "구이": []},
    "중식": {"밥": ["볶음밥"], "면": ["짜장면"], "국물": ["마라탕"], "튀김": ["탕수육"], "구이": []},
    "한식": {"밥": ["비빔밥"], "면": ["냉면"], "국물": ["김치찌개"], "튀김": [], "구이": ["삼겹살"]}
}
all_menus = sorted({m for c in menu_map.values() for v in c.values() for m in v})

# =========================
# 4. 🎯 오늘의 맛집 운세 (완전 숨김 → STOP 시 등장)
# =========================
def spin_menu(spinning):
    if not spinning:
        return "", gr.update()
    menu = np.random.choice(all_menus)
    return "", menu   # ❗ 회전 중엔 글자 완전 숨김


def stop_spin(last_menu):
    candidates = df[df["리뷰"].astype(str).str.contains(last_menu, na=False)]
    if candidates.empty:
        result = f"### 🍽️ 선택된 메뉴\n## **{last_menu}**\n❌ 맛집 없음"
    else:
        top = candidates.sort_values("평점", ascending=False).iloc[0]
        result = f"""
<div style="font-size:52px; font-weight:900; color:#ff8c00; text-align:center;">
🍽️ {last_menu}
</div>

### ⭐ 오늘의 당첨 맛집
**{top['식당명']}**  
📍 {top['위치(지하철역)']}  
⭐ 평점: {top['평점']}  

💬 {top['리뷰']}
"""
    return False, gr.update(active=False), result, gr.update(visible=True)


def retry_spin():
    return True, gr.update(active=True), "", gr.update(visible=False)

# =========================
# 5. 🍽️ AI 메뉴 추천 (버튼 UI 복구)
# =========================
def recommend_menu(food, texture):
    menus = sum(menu_map[food].values(), []) if texture == "전체" else menu_map[food].get(texture, [])
    if not menus:
        return "❌ 해당 조건 메뉴 없음"

    menu = np.random.choice(menus)
    c = df[df["리뷰"].astype(str).str.contains(menu, na=False)]

    if c.empty:
        return f"""
<div style="font-size:42px; font-weight:900; color:#ff8c00; text-align:center;">
🍽️ {menu}
</div>
<p style="text-align:center;">❌ 맛집 없음</p>
"""

    top = c.sort_values("평점", ascending=False).iloc[0]

    return f"""
<div style="
    font-size:52px;
    font-weight:900;
    color:#ff8c00;
    text-align:center;
    text-shadow:0 0 12px rgba(255,140,0,0.8);
    margin-bottom:20px;
">
🍽️ {menu}
</div>

### ⭐ 추천 맛집
**{top['식당명']}**  
📍 {top['위치(지하철역)']}  
⭐ 평점: {top['평점']}  

💬 {top['리뷰']}
"""


# =========================
# 6. 🚇 지하철역별 맛집 추천 (Top1 + 2~5위)
# =========================
def recommend_ai(region, food_type, budget, age):
    f = df[
        (df["위치(지하철역)"] == region) &
        (df["음식종류"] == food_type) &
        (df["가격대"].between(budget-3000, budget+3000))
    ]

    if f.empty:
        return "❌ 조건에 맞는 식당 없음"

    f = f.copy()
    f["final_score"] = f["predict_score"]
    result = f.sort_values("final_score", ascending=False).head(5)

    top = result.iloc[0]

    output = f"""
## 🏆 AI 추천 1위
**{top['식당명']}**  
📍 {top['위치(지하철역)']}  
⭐ 평점: {top['평점']}  
💬 {top['리뷰']}

---
### 📌 그 외 추천 식당
"""

    for _, row in result.iloc[1:].iterrows():
        output += f"""
⭐ **{row['식당명']}**  
💰 {int(row['가격대'])}원 | ⭐ {row['평점']}  
💬 {row['리뷰']}

"""
    return output

# =========================
# 7. UI
# =========================
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 AI 메뉴 & 맛집 추천 시스템")

    with gr.Tabs():

        # 🎯 오늘의 맛집 운세
        with gr.Tab("🎯 오늘의 맛집 운세"):
            spinning = gr.State(True)
            last_menu = gr.State("")
            stop = gr.Button("🎰 STOP")
            retry = gr.Button("🔄 다시 하기", visible=False)
            result = gr.Markdown()

            timer = gr.Timer(0.01, active=True)
            timer.tick(spin_menu, inputs=[spinning], outputs=[gr.Markdown(visible=False), last_menu])

            stop.click(stop_spin, inputs=[last_menu], outputs=[spinning, timer, result, retry])
            retry.click(retry_spin, outputs=[spinning, timer, result, retry])

        # 🍽️ AI 메뉴 추천 (버튼)
        with gr.Tab("🍽️ AI 메뉴 추천"):
            selected_food = gr.State(None)
            selected_texture = gr.State(None)

            gr.Markdown("### 음식 대분류")
            with gr.Row():
                bw = gr.Button("🍝 양식", elem_classes="fixed-btn")
                bj = gr.Button("🍣 일식", elem_classes="fixed-btn")
                bc = gr.Button("🥟 중식", elem_classes="fixed-btn")
                bk = gr.Button("🍚 한식", elem_classes="fixed-btn")

            gr.Markdown("### 메뉴 속성")
            with gr.Row():
                tr = gr.Button("밥", elem_classes="fixed-btn")
                tn = gr.Button("면", elem_classes="fixed-btn")
                ts = gr.Button("국물", elem_classes="fixed-btn")
                tf = gr.Button("튀김", elem_classes="fixed-btn")
                tg = gr.Button("구이", elem_classes="fixed-btn")
                ta = gr.Button("전체", elem_classes="fixed-btn")

            # ✅ 결과는 "버튼 아래"
            menu_output = gr.Markdown("❗ 버튼을 선택하면 아래에 추천이 나와요!")

            def set_food(food):
                return (
                    food,
                    *(gr.update(variant="primary") if food == x else gr.update(variant="secondary")
                      for x in ["양식", "일식", "중식", "한식"])
                )

            bw.click(lambda: set_food("양식"), outputs=[selected_food, bw, bj, bc, bk])
            bj.click(lambda: set_food("일식"), outputs=[selected_food, bw, bj, bc, bk])
            bc.click(lambda: set_food("중식"), outputs=[selected_food, bw, bj, bc, bk])
            bk.click(lambda: set_food("한식"), outputs=[selected_food, bw, bj, bc, bk])

            def set_texture(tex):
                return (
                    tex,
                    *(gr.update(variant="primary") if tex == x else gr.update(variant="secondary")
                      for x in ["밥", "면", "국물", "튀김", "구이", "전체"])
                )

            for btn, tex in zip([tr, tn, ts, tf, tg, ta],
                                ["밥", "면", "국물", "튀김", "구이", "전체"]):
                btn.click(lambda t=tex: set_texture(t),
                          outputs=[selected_texture, tr, tn, ts, tf, tg, ta]
                ).then(
                    recommend_menu,
                    inputs=[selected_food, selected_texture],
                    outputs=menu_output
                )


        # 🚇 지하철역별 추천
        with gr.Tab("🚇 지하철역별 맛집 추천"):
            gr.Markdown("## 🤖 AI 기반 머신러닝 맛집 추천 시스템")

            region = gr.Dropdown(
                choices=sorted(df["위치(지하철역)"].unique()),
                label="지하철역 선택"
            )
            food_type = gr.Dropdown(
                choices=sorted(df["음식종류"].unique()),
                label="음식 종류"
            )
            budget = gr.Slider(
                5000, 30000, value=12000, step=500,
                label="예산(원)"
            )
            age = gr.Dropdown(
                choices=sorted(df["연령층"].unique()),
                label="연령층"
            )

            btn = gr.Button("🔍 AI 추천받기")
            output_box = gr.Markdown()

            btn.click(
                recommend_ai,
                inputs=[region, food_type, budget, age],
                outputs=output_box
            )

demo.launch()
