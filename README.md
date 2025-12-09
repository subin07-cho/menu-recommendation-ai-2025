# 🤖 AI-Based Machine Learning Restaurant Recommendation System

This project is an AI-powered machine learning restaurant recommendation system that suggests the best places to eat based on subway station, cuisine type, budget, and age group.


# 🤖 AI 기반 머신러닝 맛집 추천 시스템

이 프로젝트는 지하철역, 음식 종류, 예산, 연령층 별 맛집을 추천해주는
AI 기반 머신러닝 맛집 추천 시스템 입니다.

---

## 🎯 목표

- 리뷰 텍스트(예: "김치볶음밥이 진짜 맛있어요")를 수집하고
- 각 메뉴에 대한 **긍정/부정 감성 점수**를 계산한 뒤
- 가게별로 **추천 메뉴 TOP 3**를 뽑아주는 AI 모델을 만드는 것

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
