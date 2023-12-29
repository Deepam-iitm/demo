import streamlit as st

def calculate_score(ga, p1, p2, roe, end):
    score = 0.1 * ga + 0.2 * p1 + 0.2 * p2 + 0.2 * roe + 0.3 * end
    return score

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 50 <= score < 60:
        return 'E'
    elif 40 <= score < 50:
        return 'F'
    else:
        return 'Fail'

st.title('Calculate SCORE and Grade')

ga = st.number_input('Enter GA:')
p1 = st.number_input('Enter P1:')
p2 = st.number_input('Enter P2:')
roe = st.number_input('Enter ROE:')
end = st.number_input('Enter END:')

if st.button('Calculate'):
    score = calculate_score(ga, p1, p2, roe, end)
    grade = calculate_grade(score)
    st.write(f"The calculated SCORE is: {score}")
    st.write(f"The corresponding GRADE is: {grade}")
