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

with col1:
      st.subheader('데이터시각화1')
      st.image('____________' )   # 이미지 불러오기
    col1:
      st.subheader('데이터시각화1')
      st.image('____________' )   # 이미지 불러오기
  
# 4. 모델 활용

with col2:
    st.subheader('사용자 정보 입력')
    a = st.selectbox('나이는 몇살입니까?',value=0)
    b = st.selectbox('성별은 무엇인가요?',['female,male'])
    c = st.selectbox('bmi 수치는 몇인가요?',value=22.5)
    d = st.selectbox('자녀는 몇명인가요?',value=0)
    e = st.selectbox('흡연을 한적이 있습니까?',['yes,no'])
    f = st.selectbox('거주 지역은 어디인가요?',['southwest,southeast,northwest,northeast'])

# 5. 모델 설명

with col3:
    st.subheader('모델 설명')
    st.write('기계학습 알고리즘 - 선형 회귀')
    st.write('학습 데이터 출처 : https://www.kaggle.com/code/ruslankl/health-care-cost-prediction-w-linear-regression/input')
    st.write('훈련 데이터 : 개')
    st.write('테스트 데이터 : 개')
   
