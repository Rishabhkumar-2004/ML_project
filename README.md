# 🎓 Student Performance Prediction Model

An interactive End-to-End Machine Learning Web Application built using **Python, Scikit-Learn, Pandas, and Streamlit**. This project dynamically analyzes student lifestyle, attendance, and habits to classify and predict their final academic status/performance category.

---

## 🎯 Project Objective
The main goal of this project is to understand how a student's daily routines, attendance levels, and study habits impact their overall academic performance. By leveraging a **Random Forest Classifier**, the system trains on historic student data and predicts a new student's performance category instantly through an interactive web dashboard.

---

## 🛠️ Tech Stack & Architecture

The project is built on a modular three-tier structure completely driven by Python:

1. **Data Processing & Engineering (Pandas & NumPy):** Automatic cleaning and handling of raw CSV datasets. It automatically strips whitespace and handles column mapping.
2. **Machine Learning Brain (Scikit-Learn):** Powered by a **Random Forest Classifier** achieving an outstanding accuracy of **~92.41%**. It handles dynamic category encoding for categorical target classes.
3. **Interactive Web UI (Streamlit):** A clean, elegant frontend dashboard that dynamically generates numeric inputs and form fields based on the filtered dataset features.

---

## 🚀 Key Features

* **📦 Zero-Configuration Dynamic Loading:** The script automatically scans the project directory for any `.csv` data file and trains itself without requiring manual file path hardcoding.
* **⚡ Ultra-Fast Caching (`@st.cache_resource`):** Uses Streamlit's advanced caching mechanisms so the machine learning model is trained only once, keeping the web app lightning fast on page reloads.
* **🧹 Intelligent Feature Filtering:** Automatically detects and drops non-predictive columns (like *Timestamp, Username, University, Degree*) to prevent model overfitting and keep the UI clean.
* **🖥️ Responsive Layout:** Dual-column responsive input interface with customized formatting for standard user entry.

---

## 📂 Project Structure
```bash
ML_project/
├── app.py                  # Main Streamlit Web Application Code
├── student life data.csv   # Student Lifestyle & Academic Dataset
└── README.md               # Project Documentation File

🔧 Installation & How to Run
1. Prerequisites
Ensure you have Python installed, or use the Anaconda Navigator / Anaconda Prompt.

2. Install Required Libraries
Open your terminal/command prompt inside the project folder and run:

Bash
pip install streamlit pandas numpy scikit-learn
3. Run the Web Application
Execute the following command in your terminal to launch the Streamlit local server:

Bash
python -m streamlit run app.py
This will automatically open a new tab in your web browser at http://localhost:8501 with your live interactive app!
