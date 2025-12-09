
## 🤖 AI 기반 머신러닝 맛집 추천 시스템 (AI-Based Machine Learning Restaurant Recommendation System)
 

이 프로젝트는 지하철역, 음식 종류, 예산, 연령층 별 맛집을 추천해주는
AI 기반 머신러닝 맛집 추천 시스템 입니다.

(This project is an AI-powered machine learning restaurant recommendation system that suggests the best places to eat based on subway station, cuisine type, budget, and age group.)

---

## 🎯 프로젝트 목표 (Project Goals)

이 프로젝트는 단순 식당 추천이 아니라,

✔ 사용자 행동·선호 분석을 반영한 개인화 추천 시스템 구축
✔ 리뷰 기반 예측 모델을 활용한 머신러닝 추천 엔진 개발
✔ 사용자가 브라우저에서 바로 사용할 수 있는 실용적인 UI 제공
✔ 인간-AI 협업 서비스 설계 강의 과제 목적에 부합하는 프로덕트 형태 구현

데이터 기반 의사결정 + 사용자 중심 UX + AI 추천 기술
3가지를 모두 충족하는 완성형 프로젝트가 목표입니다.


---

## ✨ 기능 소개 (Features)

🧠 1. 리뷰 기반 머신러닝 추천 엔진

     식당 리뷰, 평점, 메뉴 특성 데이터를 활용

    ML 모델의 predict_score로 식당 품질을 예측

사용자 예산과 가격대 차이까지 고려하여 정확도 상승

📍 2. 사용자 조건 필터링

사용자가 입력한 조건을 기반으로 필터링 후 추천:

조건	설명
📍 위치	지하철역 단위 필터링
🍱 음식종류	한식/일식/카페/베트남 등
💰 예산	유저 예산 - 식당 가격차 가중치 반영
👤 연령층	연령대별 선호도 반영 가능

필터링 이후 점수를 계산하여 TOP 5 추천 제공.

🏆 3. TOP 1 최종 추천 + 2~5위 추천

별도 박스 디자인으로 가장 추천하는 식당을 강조

기타 추천 식당도 리뷰까지 포함해 보여줌

Markdown + HTML 조합으로 깔끔한 시각 출력

💻 4. Gradio Web UI

브라우저에서 즉시 확인 가능한 모델 UI

Dropdown/Slider 기반 직관적 UX

클릭 한 번으로 AI 추천 경험 제공

📊 5. 가중치 기반 점수 계산

사용자 예산 반영 + 머신러닝 예측 점수 결합:

최종 점수 = 예측점수(70%) + 예산 적합도(30%)


보다 현실성 있는 추천 결과가 나오도록 설계함.



---

## 🧱 앞으로 만들 기능

1. 리뷰 데이터 수집 (네이버/카카오/배달앱 등)
2. 텍스트 전처리 (이모지, 특수문자 제거 등)
3. 한국어 감성 분석 모델 적용 (KoBERT, HuggingFace 등)
4. 메뉴별 평균 감성 점수 계산
5. 가게별 메뉴 추천 함수 구현
6. (선택) SHAP으로 "어떤 단어가 긍정/부정에 영향을 주는지" 설명

---

## 📂 프로젝트 구조(예정)

```bash
menu-recommendation-ai/
├── README.md
├── docs/
│   ├── 01_introduction.md
│   ├── 02_data_collection.md
│   ├── 03_preprocessing.md
│   ├── 04_modeling.md
│   ├── 05_results.md
│   └── 06_conclusion.md
├── src/
│   ├── data_collect.py
│   ├── preprocessing.py
│   ├── sentiment_model.py
│   ├── recommendation.py
│   └── analysis.ipynb
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample_reviews.csv
└── images/
    ├── system_architecture.png
    └── example_output.png

---
```

## 📂 프로젝트 구조(예정)
