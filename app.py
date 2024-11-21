# 분류 모델 웹앱 만들기

import streamlit as st
import joblib as jl
model = joblib.load('linear_regression_model.pkl')

# 1. 기계학습 모델 파일 로드

#model = jl.load('')

# 2. 모델 설명

st.title('선형 회귀를 통한 의료비 예측')
st.subheader('의료비를 어떻게 예측할 수 있을까?')
col1,col2,col3 = st.columns(3)  

# 3. 데이터시각화

# 4. 모델 활용

