import streamlit as st
import pandas as pd
import joblib

# Page Configuration
st.set_page_config(
    page_title="Heart Health Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Models
model = joblib.load("knn_heart_model.pkl")
scaler = joblib.load("heart_scaler.pkl")
expected_columns = joblib.load("heart_columns.pkl")

# Custom CSS Styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stContainer {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
    }
    .header {
        text-align: center;
        color: #E74C3C;
        font-size: 2.8em;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .subheader {
        text-align: center;
        color: #95A5A6;
        font-size: 1.1em;
        margin-bottom: 30px;
    }
    .input-section {
        background-color: #F8F9FA;
        border-left: 4px solid #E74C3C;
        padding: 20px;
        border-radius: 5px;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='header'>❤️ Heart Health Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>🔬Heart Disease Risk Assessment</div>", unsafe_allow_html=True)

st.markdown("---")

# Info Section
with st.expander("ℹ️ About This Tool", expanded=False):
    st.info("""
    This application uses a trained K-Nearest Neighbors (KNN) model to predict your risk of heart disease 
    based on your health indicators. Please consult with a healthcare professional for medical advice.
    """)

st.markdown("<div class='input-section'><b>📋 Enter Your Health Information</b></div>", unsafe_allow_html=True)

# Input Fields in Organized Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("👤 Demographics")
    age = st.slider("Age (years)", 18, 100, 40, help="Your age in years")
    sex = st.selectbox("Sex", ['M', 'F'], format_func=lambda x: 'Male ♂️' if x == 'M' else 'Female ♀️')

with col2:
    st.subheader("🩸 Blood Metrics")
    cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200, help="Total cholesterol level")
    resting_bp = st.number_input("Resting BP (mm Hg)", 80, 200, 120, help="Resting blood pressure")
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120", [0, 1], 
                              format_func=lambda x: 'Yes ✓' if x == 1 else 'No ✗',
                              help="Is fasting blood sugar > 120 mg/dL?")

with col3:
    st.subheader("💗 Cardiac Indicators")
    max_hr = st.slider("Max Heart Rate (bpm)", 60, 220, 150, help="Maximum heart rate achieved")
    exercise_angina = st.selectbox("Exercise Angina", ["Y", "N"],
                                   format_func=lambda x: 'Yes ✓' if x == 'Y' else 'No ✗',
                                   help="Chest pain induced by exercise?")

st.markdown("")

# Additional Parameters
col4, col5, col6 = st.columns(3)

with col4:
    chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"],
                             format_func=lambda x: {
                                 "ATA": "Atypical Angina",
                                 "NAP": "Non-anginal Pain",
                                 "TA": "Typical Angina",
                                 "ASY": "Asymptomatic"
                             }[x])

with col5:
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"],
                              format_func=lambda x: {
                                  "Normal": "Normal",
                                  "ST": "ST-T Abnormality",
                                  "LVH": "Left Ventricular Hypertrophy"
                              }[x])

with col6:
    oldpeak = st.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0,
                       help="ST segment depression induced by exercise relative to rest")

st.markdown("")

col7, col8 = st.columns(2)
with col7:
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"],
                           format_func=lambda x: {
                               "Up": "Upsloping ↗️",
                               "Flat": "Flat →",
                               "Down": "Downsloping ↘️"
                           }[x])

# Prediction Button
st.markdown("---")

col_button1, col_button2, col_button3 = st.columns([1, 2, 1])
with col_button2:
    predict_button = st.button("🔍 Analyze Heart Health", use_container_width=True, key="predict")

if predict_button:
    try:
        raw_input = {
            'Age': age,
            'RestingBP': resting_bp,
            'Cholesterol': cholesterol,
            'FastingBS': fasting_bs,
            'MaxHR': max_hr,
            'Oldpeak': oldpeak,
            'Sex_' + sex: 1,
            'ChestPainType_' + chest_pain: 1,
            'RestingECG_' + resting_ecg: 1,
            'ExerciseAngina_' + exercise_angina: 1,
            'ST_Slope_' + st_slope: 1
        }
        input_df = pd.DataFrame([raw_input])

        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[expected_columns]

        scaled_input = scaler.transform(input_df)
        prediction = model.predict(scaled_input)[0]

        st.markdown("---")
        st.markdown("<h2 style='text-align: center;'>📊 Prediction Results</h2>", unsafe_allow_html=True)
        st.markdown("")

        if prediction == 1:
            col_res1, col_res2, col_res3 = st.columns([1, 2, 1])
            with col_res2:
                st.error("🚨 HIGH RISK - Heart Disease Likely", icon="⚠️")
                st.markdown("""
                ### Important Notice:
                Based on the analyzed health indicators, there is a **high risk** of heart disease.
                
                **Please take the following steps:**
                - 🏥 Schedule an appointment with a cardiologist immediately
                - 📋 Get a comprehensive cardiac evaluation
                - 💊 Follow your doctor's treatment recommendations
                - 🚫 Avoid strenuous activities until cleared by a doctor
                """)
        else:
            col_res1, col_res2, col_res3 = st.columns([1, 2, 1])
            with col_res2:
                st.success("✅ LOW RISK - Heart Health Looks Good!", icon="💚")
                st.markdown("""
                ### Great News!
                Based on the analyzed health indicators, your heart disease risk appears to be **low**.
                
                **Maintain your health:**
                - 🏃 Continue regular exercise (150 mins/week)
                - 🥗 Maintain a healthy diet (low sodium, high fiber)
                - 🧘 Manage stress through meditation or yoga
                - 🏥 Get regular health check-ups annually
                """)
    
    except Exception as e:
        st.error(f"❌ Error during prediction: {str(e)}")
        st.info("Please check that all input files are loaded correctly.")

