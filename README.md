# Healthcare Premium Amount Predictor 🏥💰

An interactive Streamlit web app that predicts healthcare insurance premium amounts based on user details and medical history using trained machine learning models.

## 🌐 Live App

👉 [Try the app here](https://healthcare-premium-amount-predictor.streamlit.app/)

---

## 📌 Features

✅ User-friendly form-based input  
✅ Personalized prediction using ML models  
✅ Age-based model segmentation for improved accuracy  
✅ Instant premium amount prediction in the browser  
✅ Interactive display of transformed features  
✅ Fully deployed on Streamlit Cloud

---

## 🚀 About This Project

This app lets users enter personal and medical information (like age, BMI category, smoking status, income, medical history, etc.) to get an instant prediction of their likely healthcare insurance premium. It uses:

- Separate machine learning models for different age groups (<=26 and >26)  
- Feature engineering and transformation pipeline  
- Streamlit for the web interface and deployment

It's designed to help visualize and test how different risk factors impact insurance premium pricing.

---

## 🛠️ Tech Stack

- **Python 3.10+**  
- **Streamlit**  
- **pandas**  
- **scikit-learn**  
- **joblib**

---

## 💻 How to Run Locally

1️⃣ Clone the repository:

```bash
git clone https://github.com/aryanzutshi2004/ml_prj_healthcare_premium_prediction.git
cd ml_prj_healthcare_premium_prediction

2️⃣ Install dependencies:
pip install -r requirements.txt

3️⃣ Run the Streamlit app:
streamlit run app/main.py
