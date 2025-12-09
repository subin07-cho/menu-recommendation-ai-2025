안녕하세요!  
저희는 한양대학교 ‘인간-인공지능 협업 제품·서비스 설계’ 수업을 수강 중인 학생들입니다.  
이번 프로젝트는 AI를 활용해 실제로 유의미한 가치를 만들어내고, 더 많은 분들이 사용할 수 있는 오픈소스 프로젝트를 목표로 하고 있습니다.  
저희의 시스템이 흥미롭거나, 재미있거나, 도움이 되셨다면 별(⭐️) 한 번씩 눌러주시면 큰 힘이 됩니다!  
감사합니다 😊💙  





        
## 🤖 AI 기반 머신러닝 맛집 추천 시스템 (AI-Based Machine Learning Restaurant Recommendation System)
 

이 프로젝트는 지하철역, 음식 종류, 예산, 연령층에 따라 사용자에게 적합한 맛집을 추천해주는
AI 기반 머신러닝 맛집 추천 시스템 입니다.

(This project is an AI-powered machine learning restaurant recommendation system that suggests the best places to eat based on subway station, cuisine type, budget, and age group.)

---

## 🎯 프로젝트 목표 (Project Goals)


✔ 사용자 행동 및 선호 분석을 반영한 개인화 추천 시스템 구축

✔ 리뷰 기반 예측 모델을 활용한 머신러닝 추천 엔진 개발

✔ 사용자가 브라우저에서 바로 사용할 수 있는 실용적인 Web UI 제공

이 프로젝트는 단순한 식당 추천을 넘어서,  
데이터 기반 의사결정 + 사용자 중심 UX + AI 추천 기술  
3가지를 모두 충족하는 것을 목표로 합니다.



---

## ✨ 기능 소개 (Features)

🧠 1. 리뷰 기반 머신러닝 추천 엔진

     식당 위치, 가격, 식당 리뷰, 평점, 메뉴 등의 데이터를 활용

     머싱러닝 모델의 'predict_score'로 식당 품질을 예측

     사용자 예산과 식당 가격대 차이 등을 함께 고려하여 추천 정확도 상승

📍 2. 사용자 조건 필터링

    사용자가 입력한 조건을 기반으로 필터링 후 추천:

     📍      위치         ->   지하철역 단위 필터링
     🍱    음식종류	     ->   한식 / 일식 / 카페 / 베트남 등
     💰      예산	     ->   사용자의 예산, 식당의 가격 차이를 반영
     👤     연령층	     ->   연령대별 선호도 반영 가능

    필터링 이후, 점수를 계산하여 **TOP 5 식당을 추천**합니다.


🏆 3. TOP 1 최종 추천 + 2~5위 추천

    별도 박스 디자인으로 AI가 가장 추천하는 1등 식당을 강조 표시 
    
    2~5위 식당도 리뷰와 함께 함께 보여주어 다양한 선택지 제공
    
    Gradio의 Markdown + HTML 조합으로 시각적으로 깔끔한 출력

💻 4. Gradio Web UI
 
    브라우저에서 즉시 확인 가능한 모델 UI
    
    Dropdown/Slider 기반 직관적 UX
    
    버튼 클릭 한 번으로 AI 맛집 추천 경험을 제공

📊 5. 가중치 기반 점수 계산

    사용자 예산 반영 + 머신러닝 예측 점수 결합:
    
    ** 최종 점수 = 예측점수(70%) + 예산 적합도(30%)
    
    이렇게 설계함으로써,  
    맛의 품질 + 사용자 예산에 맞는지, 이 두 가지를 함께 고려한 추천이 가능합니다.

---


## 📂 프로젝트 폴더 구조
```
📁 ai-restaurant-recommender
│
├── 📁 data
│     └── Restaurants.xlsx   # 리뷰 데이터
│
├── 📁 src
│     ├── recommend_ai.py                 # AI 추천 함수
│     └── ui_gradio.py                    # Gradio Web UI 실행 파일
│
├── app.py                                 # 통합 실행 파일 (선택)
│
├── requirements.txt                       # 필요한 라이브러리
│
└── README.md                              # 프로젝트 설명서 (현재 문서)
```
---


## 🌐 Gradio Web UI 코드(요약)
```
 with gr.Blocks() as demo:
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
```
---

## 🏁 실행 방법

✅ 1) 로컬 환경에서 실행
```
 1. 필요한 라이브러리 설치:
   pip install -r requirements.txt
   또는
   pip install pandas gradio

2. 데이터 파일 위치 확인:
/data/Restaurants.xlsx

3. Gradio UI 실행:
python src/ui_gradio.py
```
실행 후, 터미널에 출력되는 URL로 접속하면
브라우저에서 추천 시스템을 사용할 수 있습니다.

✅ 2) Colab 환경에서 실행 (선택)
```
1. Colab에서 이 레포지토리를 클론하거나 코드를 복사해서 사용
2. Restaurants.xlsx 파일 업로드
3. ui_gradio.py 또는 관련 셀 실행
4. Gradio가 생성해주는 외부 접속 링크로 들어가서 사용
```
---
## 📌 결과

사용자가 위치, 음식 종류, 예산, 연령층을 선택하면
→ 조건에 맞는 식당 중 점수가 높은 상위 5곳을 추천
→ 그 중 1등 식당을 강조 표시하고,
→ 각 식당의 리뷰와 평점을 함께 보여줍니다.

스크린샷 예시(추가 예정):

## 팀원
---
김희은, 조수빈, 최정은
