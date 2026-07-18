# ❤️ Heart Health Predictor

An AI-powered heart disease risk assessment application built with Streamlit and Machine Learning.

## 📋 Features

- **Interactive UI**: User-friendly interface with emojis and organized input sections
- **AI Predictions**: Uses K-Nearest Neighbors (KNN) model trained on heart disease data
- **Health Indicators**: Analyzes age, blood pressure, cholesterol, heart rate, and more
- **Actionable Advice**: Provides recommendations based on risk level

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/heart_disease_predictor.git
cd heart_disease_predictor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## 📊 Model Information

- **Algorithm**: K-Nearest Neighbors (KNN)
- **Input Features**: 11 health indicators
- **Output**: Binary classification (High Risk / Low Risk)
- **Accuracy**: Based on trained model performance

## 📥 Input Parameters

- **Age**: 18-100 years
- **Sex**: Male / Female
- **Chest Pain Type**: ATA, NAP, TA, ASY
- **Resting Blood Pressure**: 80-200 mm Hg
- **Cholesterol**: 100-600 mg/dL
- **Fasting Blood Sugar**: Yes/No (> 120 mg/dL)
- **Resting ECG**: Normal, ST, LVH
- **Max Heart Rate**: 60-220 bpm
- **Exercise-Induced Angina**: Yes/No
- **ST Depression**: 0-6.0
- **ST Slope**: Up, Flat, Down

## ⚠️ Disclaimer

**This tool is for educational and informational purposes only.** It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare professional for medical decisions.

## 📦 Files Required

Make sure these model files are in the project directory:
- `knn_heart_model.pkl` - Trained KNN model
- `heart_scaler.pkl` - Feature scaler
- `heart_columns.pkl` - Expected feature columns

## 🔗 Deploy on Streamlit Cloud

1. Push this repository to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your GitHub repo, branch, and `app.py`
5. Click "Deploy"

## 📝 License

MIT License - feel free to use and modify

## 👨‍💻 Author

Created with ❤️ for heart health awareness

---

**Note**: Ensure all `.pkl` files are present before running the application.
