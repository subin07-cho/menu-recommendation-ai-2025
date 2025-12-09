
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
