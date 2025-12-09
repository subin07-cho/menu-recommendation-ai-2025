
## 🤖 AI 기반 머신러닝 맛집 추천 시스템 (AI-Based Machine Learning Restaurant Recommendation System)
 

이 프로젝트는 지하철역, 음식 종류, 예산, 연령층 별 맛집을 추천해주는
AI 기반 머신러닝 맛집 추천 시스템 입니다.

(This project is an AI-powered machine learning restaurant recommendation system that suggests the best places to eat based on subway station, cuisine type, budget, and age group.)

---

## 🎯 프로젝트 목표 (Project Goals)


✔ 사용자 행동 및 선호 분석을 반영한 개인화 추천 시스템 구축

✔ 리뷰 기반 예측 모델을 활용한 머신러닝 추천 엔진 개발

✔ 사용자가 브라우저에서 바로 사용할 수 있는 실용적인 UI 제공

이 프로젝트는 단순 식당 추천이 아니라, 데이터 기반 의사결정 + 사용자 중심 UX + AI 추천 기술 3가지를 모두 충족하는 것이 프로젝트가 목표입니다.


---

## ✨ 기능 소개 (Features)

🧠 1. 리뷰 기반 머신러닝 추천 엔진

     식당 위치, 식당 종류, 가격, 식당 리뷰, 평점, 메뉴 특성 등의 데이터를 활용

     ML 모델의 predict_score로 식당 품질을 예측

     사용자 예산과 가격대 차이까지 여러 부분을 고려하여 정확도 상승

📍 2. 사용자 조건 필터링

    사용자가 입력한 조건을 기반으로 필터링 후 추천:

            조건	       |           설명
     📍 위치               |  지하철역 단위 필터링
     🍱 음식종류	       |  한식/일식/카페/베트남 등
     💰 예산	           |  유저 예산, 식당 가격차 가중치 반영
     👤 연령층	           |  연령대별 선호도 반영 가능

    필터링 이후 점수를 계산하여 TOP 5 추천 제공함

🏆 3. TOP 1 최종 추천 + 2~5위 추천

    별도 박스 디자인으로 가장 추천하는 식당을 강조
    
    기타 추천 식당도 리뷰까지 포함해 다양한 식당을 보여줌
    
    Markdown + HTML 조합으로 깔끔한 시각 출력

💻 4. Gradio Web UI
 
    브라우저에서 즉시 확인 가능한 모델 UI
    
    Dropdown/Slider 기반 직관적 UX
    
    클릭 한 번으로 AI 추천 경험 제공

📊 5. 가중치 기반 점수 계산

    사용자 예산 반영 + 머신러닝 예측 점수 결합:
    
    최종 점수 = 예측점수(70%) + 예산 적합도(30%)


