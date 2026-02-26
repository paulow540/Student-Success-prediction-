import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.pkl')
st.title('Can We Predict Student Success')
st.header('What is Student Success?')
st.write('Student success is a term used to describe the achievement of educational goals by students')



# Columns 
final_score = st.number_input('Final Score', min_value=37.0, max_value=100.0, value=50.0,format='%.0f')
grade = st.selectbox('Grade', ['A', 'B', 'C', 'D', 'F'])
previous_score = st.number_input('Previous Score', min_value=40.0, max_value=95.0, value=50.0,format='%.0f')
math_prev_score = st.number_input('Math Previous Score', min_value=30.0, max_value=104.0, value=50.0,format='%.0f')
science_prev_score = st.number_input('Science Previous Score', min_value=30.0, max_value=100.0, value=50.0,format='%.0f')
language_prev_score = st.number_input('Language Previous Score', min_value=27.0, max_value=108.0, value=50.0,format='%.0f')
daily_study_hours = st.number_input('Daily Study Hours', min_value=1.0, max_value=5.0, value=2.0,format='%.1f')
attendance_percentage = st.number_input('Attendance Percentage', min_value=47.0, max_value=99.0, value=78.9,format='%.0f')
homework_completion_rate = st.number_input('Homework Completion Rate', min_value=51.0, max_value=111.0, value=70.7,format='%.0f')    
sleep_hours = st.number_input('Sleep Hours', min_value=4.5, max_value=10.0, value=7.0,format='%.1f')    
screen_time_hours = st.number_input('Screen Time Hours', min_value=1.0, max_value=6.0, value=2.0,format='%.1f')    
physical_activity_minutes = st.number_input('Physical Activity Minutes', min_value=30.0, max_value=120.0, value=49.6,format='%.0f')  
motivation_score = st.number_input('Motivation Score', min_value=4.0, max_value=10.0, value=4.8,format='%.1f')  
exam_anxiety_score = st.number_input('Exam Anxiety Score', min_value=1.0, max_value=9.0, value=3.0,format='%.1f')  
parent_education_level =st.selectbox('Parent Education Level', ['High School', 'Bachelor', 'Master'])  
study_environment = st.selectbox('Study Environment', ['Quiet', 'Noisy', 'Moderate'])


# prediction
if st.button('Predict'):
    grade_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4}
    parent_education_mapping = {'High School': 1, 'Bachelor': 2, 'Master': 3}
    study_environment_mapping = {'Quiet': 2, 'Noisy': 1, 'Moderate': 0}

    grade_encoded = grade_mapping[grade]
    parent_education_encoded = parent_education_mapping[parent_education_level]
    study_environment_encoded = study_environment_mapping[study_environment]

    input_data = np.array([[final_score, grade_encoded, previous_score, math_prev_score, science_prev_score,
                            language_prev_score, daily_study_hours, attendance_percentage, homework_completion_rate,
                            sleep_hours, screen_time_hours, physical_activity_minutes,
                            motivation_score, exam_anxiety_score, parent_education_encoded,
                            study_environment_encoded]])
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.success('The student is likely to succeed!')
    else:
        st.error('The student is unlikely to succeed.')