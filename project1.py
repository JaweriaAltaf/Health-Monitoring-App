import streamlit as st
import pandas as pd

st.title("Health Monitoring App ⛨")
st.write("""
         This app helps users check their Body Mass Index (BMI) 
         or Blood Pressure status based on the option they select. 
         It takes the necessary input from the user, calculates the result, 
         and displays it along with storing previous entries.""")

if "bmi_data" not in st.session_state:
    st.session_state.bmi_data= pd.DataFrame(columns=["Name","Height","Weight","BMI"])

if "bp_data" not in st.session_state:
    st.session_state.bp_data = pd.DataFrame(columns=["Name","Age","Systolic", "Diastolic"])

select = st.selectbox("Choose what you want.", ["Select ","BMI Calculator","Blood Pressure Checker"])

if select == "BMI Calculator":
    st.subheader("BMI CALCULATOR")
    st.write("Let's calculate your BMI")
    name = st.text_input("Enter your name:")
    height = st.number_input("Enter your Height (in centimetres):", min_value=1)
    weight = st.number_input("Enter your Weight(in kilograms):", min_value=2.4 , max_value=635.9)
    if st.button("Check" , type="primary"):
        if name in st.session_state.bmi_data["Name"].values:
            st.warning("⚠️This name is already exist , use another name!")
        elif(height > 0 and weight > 0):
            height_m = height / 100
            BMI = weight / height**2


            if BMI < 18.5:
                st.warning("Underweight💛")
                st.write(f"Your BMI value is: {BMI}")
                st.write("""
                    💬 You are wonderfully unique, but your body may need a little more nourishment. 🍲\n
                    👉 Eat balanced meals with proteins, good fats & carbs (eggs, milk, rice, nuts).\n
                    👉 Avoid skipping meals — try 3 meals + 2 snacks daily. 🍎\n
                    👉 Stay hydrated 💧 and do light strength exercises 💪 to build muscle mass.\n
                    👉 Stay hydrated 💧 and do light strength exercises 💪 to build muscle mass.
                    """)
            elif BMI <= 25:
                st.info("Normal weight")
                st.write(f"Your BMI value is: , {BMI}")

                st.write("""
                    💬 You are in a healthy range — great job maintaining balance! 🌈\n
                    👉 Continue eating a balanced diet 🥗 with fruits, veggies, and lean proteins.\n
                    👉 Stay active — at least 30 mins of exercise daily (walk, yoga, cycling). 🚴‍♀️\n
                    👉 Get enough sleep 😴 and manage stress 🌸\n
                    🌿 Goal: Maintain your current healthy lifestyle and keep shining! 🌟
                    """)
            elif BMI < 30:
                st.warning("Overweight ")
                st.write(f"Your BMI value is: , {BMI}")
                st.write("""
                    💬 Your body just needs a little more care and movement — you have got this! 💪\n
                    👉 Focus on portion control 🍽️ and avoid sugary or fried foods.\n
                    👉 Try light exercises like brisk walking or swimming 🏊‍♀️\n
                    👉 Drink plenty of water 💧 and eat more veggies & whole grains.\n
                    🌻 Goal: Slowly reduce weight with consistency, not pressure — progress matters! 🌞
                    """)
            
            else:
                st.error("Obese ")
                st.write(f"Your BMI value is: {BMI}")
                st.write("""
                    💬 You are strong and capable — small steps can lead to big changes! 🌹\n
                    👉 Start with short walks 🚶‍♂️ and increase activity gradually.\n
                    👉 Choose healthy meals — grilled, baked, or steamed foods instead of fried ones. 🥦\n
                    👉 Get proper rest, avoid stress eating 🍫, and seek medical or nutrition advice if needed. 🩺\n
                    🌼 Goal: Improve your overall health, energy, and happiness — one positive change at a time! 🌟
                    """)
            
            new_data = pd.DataFrame({
                "Name": [name],
                "Height": [height],
                "Weight": [weight],
                "BMI":[BMI]
            })
            st.session_state.bmi_data = pd.concat([st.session_state.bmi_data,new_data])
    if not st.session_state.bmi_data.empty:
        st.subheader("📋 BMI Records")
        st.dataframe(st.session_state.bmi_data)       
        st.subheader("📊 BMI Comparison Chart")
        st.bar_chart(st.session_state.bmi_data.set_index("Name")["BMI"])

if select == "Blood Pressure Checker":
    st.subheader("Blood Pressure Checker")
    st.write("Let's calculate your Blood Pressure")

    name = st.text_input("Enter your name: ")
    age = st.number_input("Enter your age:",min_value=0,max_value=100)
    systolic = st.number_input("Enter your Systolic Pressure:", min_value=50.0 , max_value=250.0)
    diastolic = st.number_input("Enter your diastolic Pressure:", min_value=30.0, max_value=150.0)
    if st.button("Check", type="primary"):
        if name in st.session_state.bp_data["Name"].values:
            st.warning("⚠️This name is already exist , use another name!")
            
        elif systolic < 90 or diastolic < 60:
            category = "Low Blood Pressure(Hypotension)"
            suggestion = "💧 Drink plenty of water, eat balanced meals, and avoid standing up too quickly!"
            st.warning(f"Your BP is {systolic}/{diastolic} mmHg \n{category} \nSuggestion: {suggestion}")
        elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
            category="Normal Blood Pressure"
            suggestion= "🌿 Great job! Maintain a healthy diet, exercise regularly, and keep monitoring your BP."
            st.info(f"Your BP is {systolic}/{diastolic} mmHg \n{category} \nSuggestion: {suggestion}")
        elif 120 < systolic <= 139 or 80 < diastolic <= 89:
            category = "Pre-High Blood Pressure (Elevated)"
            suggestion = "⚠️ Keep an eye on your diet and stress. Regular walks and less salt can help keep it normal."
            st.warning(f"Your BP is {systolic}/{diastolic} mmHg \n{category} \nSuggestion: {suggestion}")
        elif 140 <= systolic <= 180 or 90 <= diastolic <= 120:
            category = "High Blood Pressure (Hypertension Stage 1-2)"
            suggestion = "💊 Reduce salt intake, avoid stress, exercise daily, and check BP regularly!"
            st.error(f"Your BP is {systolic}/{diastolic} mmHg \n{category} \nSuggestion: {suggestion}")
        elif systolic > 180 or diastolic > 120:
            category = "Severe High Blood Pressure (Hypertensive Crisis)"
            suggestion = "🚨 Seek medical attention immediately! This could be dangerous."
            st.error(f"Your BP is {systolic}/{diastolic} mmHg \n{category} \nSuggestion: {suggestion}")
        else:
            category = "Unknown / Invalid Reading"
            suggestion = "❗Please enter valid systolic and diastolic values within the normal range."

        new_entry = pd.DataFrame({
            "Name": [name],
            "Age":[age],
            "Systolic": [systolic],
            "Diastolic":[diastolic],
            "Blood Pressure": [category]
        })
        st.session_state.bp_data = pd.concat([st.session_state.bp_data,new_entry])

    if not st.session_state.bp_data.empty:
        st.subheader("📋 Blood Pressure Records")
        st.dataframe(st.session_state.bp_data)
