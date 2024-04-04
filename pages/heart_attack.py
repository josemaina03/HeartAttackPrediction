import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('C:\\Users\\revolve 810\\Desktop\\projo\\heart_attack.pkl', 'rb'))

def heart():
    st.title("Heart Attack Prediction")

    col1, col2 = st.columns(2)  

    with col1:
        age = st.text_input("Age", max_chars=3)
        gender = st.text_input("Gender (0 for female, 1 for male)", max_chars=3)
        rbp = st.text_input("Resting Blood Pressure(90-120 mmhg)", max_chars=3)
        chol = st.text_input("Cholesterol( bmi sensor result ,200-239mg/dl)", max_chars=3)
        fbs = st.text_input("Fasting Blood Sugar(70-100mg/dl)", max_chars=3)
        rer = st.text_input("Resting Electrocardiographic Result(test for heart rhythm and rate when at rest, 49-100 for men,55-108 for women)", max_chars=3)
       
    with col2:
        heart_rate = st.text_input("Heart Rate Achieved(beats per minutes,60-100)", max_chars=3)
        exercise_induced = st.text_input("Exercise Induced(discomfort that occurs during exercise ,190-210)", max_chars=3)
        depression = st.text_input("Depression Induced(depression caused by exercise relarive to rest,64-70)", max_chars=3)
        slp = st.text_input("Slope of peak exercise(shift relative to exercise induced incrementsin heart rate ,60-80)", max_chars=3)
        cor_artery_anomaly = st.text_input("Coronary Artery Anomaly(artery that has a defect,0-3)", max_chars=3)

        if st.button('Predict'):
            # Validate gender input
            if gender not in ['0', '1']:
                st.error("Gender can either be 0 or 1.")
                return
            
            # Convert input values to numeric types, handling empty strings
            try:
                # Convert each input field to float or handle empty strings
                age = float(age) if age.strip() else None
                gender = float(gender) if gender.strip() else None
                rbp = float(rbp) if rbp.strip() else None
                chol = float(chol) if chol.strip() else None
                fbs = float(fbs) if fbs.strip() else None
                rer = float(rer) if rer.strip() else None
                heart_rate = float(heart_rate) if heart_rate.strip() else None
                exercise_induced = float(exercise_induced) if exercise_induced.strip() else None
                depression = float(depression) if depression.strip() else None
                slp = float(slp) if slp.strip() else None
                cor_artery_anomaly = float(cor_artery_anomaly) if cor_artery_anomaly.strip() else None
                
                # Enforce limits not to exceed 300
                age = min(age, 300) if age is not None else None
                gender = min(gender, 300) if gender is not None else None
                rbp = min(rbp, 300) if rbp is not None else None
                chol = min(chol, 300) if chol is not None else None
                fbs = min(fbs, 300) if fbs is not None else None
                rer = min(rer, 300) if rer is not None else None
                heart_rate = min(heart_rate, 300) if heart_rate is not None else None
                exercise_induced = min(exercise_induced, 300) if exercise_induced is not None else None
                depression = min(depression, 300) if depression is not None else None
                slp = min(slp, 300) if slp is not None else None
                cor_artery_anomaly = min(cor_artery_anomaly, 300) if cor_artery_anomaly is not None else None
                
                # Create input array
                input_data = np.array([[age, gender, rbp, chol, fbs, rer,
                                         heart_rate, exercise_induced, depression, slp,
                                         cor_artery_anomaly]])
            except ValueError:
                st.error("Please provide valid numeric inputs.")
                return
        
            # Making prediction
            prediction_probability = model.predict_proba(input_data)[0][1] * 100  # Probability of having a heart attack
            st.success(f"The chance of having a heart attack is approximately {prediction_probability:.2f}%.")

            # Recommendations based on prediction
            if prediction_probability >= 50:
                st.info("Your chance of having a heart attack is relatively high. It's important to consult with a healthcare professional for further evaluation and advice.")
            else:
                st.info("Your chance of having a heart attack is relatively low. However, maintaining a healthy lifestyle with regular exercise and a balanced diet is always beneficial for heart health.")

if __name__ == "__main__":
    heart()
