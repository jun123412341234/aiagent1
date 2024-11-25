# 분류 모델 웹앱 만들기
import streamlit as st
# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model__2_.pkl')
# 2. 모델 설명
st.title('선형 linear_regression_model__2_.pkl 통한 의료비 예측')
st.subheader('의료비를 어떻게 예측할 수 있을까?')
col1,col2,col3 = st.columns(3)  
# 3. 데이터시각화
with col1:
      st.subheader('데이터시각화1(히트맵)')
      st.image('시각화1.png')   # 이미지 불러오기
  
# 4. 모델 활용
with col2:
    st.subheader('정보 입력(사용자의 정보를 학습하지 않습니다)')
    a = st.number_input('나이는 몇살입니까?',value=0)
    b = st.selectbox('성별은 무엇인가요?(여성=0,남성=1)',[0,1])
    c = st.number_input('bmi 수치는 몇인가요?',value=22.5)
    d = st.number_input('자녀는 몇명인가요?',value=0)
    e = st.selectbox('흡연을 한적이 있습니까?(X=0,O=1)',[0,1])
    f = st.selectbox('거주 지역은 어디인가요?(남서,북서,남동,북동)',[0,1,2,3])
# 5. 모델 설명
with col3:
    st.subheader('모델 설명')
    st.write('기계학습 알고리즘 - 선형 회귀')
    st.write('학습 데이터 출처 : https://www.kaggle.com/code/ruslankl/health-care-cost-prediction-w-linear-regression/input')
    st.write('훈련 데이터 : 개')
    st.write('테스트 데이터 : 개')
      
if st.button('점수 예측'):
    input_data = [[a,b,c,d,e,f]]
    p = model.predict(input_data)
    st.write('인공지능이 예상한 당신의 점수는',p)
