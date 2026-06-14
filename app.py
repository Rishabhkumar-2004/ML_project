import streamlit as st
import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier

# 1. Page Configuration
st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓", layout="centered")

st.title("🎓 Student Performance Prediction Model")
st.write("This app predicts student status based on key lifestyle and academic metrics.")
st.markdown("---")

# 2. Data Load & Model Training
@st.cache_resource
def train_model():
    # Folder ki koi bhi .csv file automatic uthana
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    if not csv_files:
        raise FileNotFoundError("Folder me koi bhi .csv data file nahi mili!")
        
    df = pd.read_csv(csv_files[0])
    df.columns = df.columns.str.strip()  # Remove extra spaces
    
    # Target Column setup (Last column)
    target_col = df.columns[-1]
    
    # --- YAHAN HUM FALTU COLUMNS KO DROP KAR RAHE HAIN ---
    unwanted_cols = ['Timestamp', 'Username', 'University', 'Degree', target_col]
    X = df.drop(columns=[col for col in unwanted_cols if col in df.columns], errors='ignore')
    
    # Baaki bache text columns ko numeric categories me convert karna
    for col in X.select_dtypes(include=['object']).columns:
        X[col] = X[col].astype('category').cat.codes
        
    # Numerical columns filter karna training ke liye
    X = X.select_dtypes(include=[np.number])
    
    y = df[target_col].astype('category').cat.codes  # Safe classification mapping
    
    # Model Train karna
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    return model, list(X.columns), list(df[target_col].astype('category').cat.categories)

# Model initialization
try:
    model, feature_list, target_classes = train_model()
except Exception as e:
    st.error(f"❌ Error training model: {e}")
    st.stop()

# 3. Dynamic Frontend UI (Sirf kaam ke features dikhenge)
st.subheader("📋 Enter Student Metrics:")
user_inputs = {}

cols = st.columns(2)
for idx, feature in enumerate(feature_list):
    with cols[idx % 2]:
        # Beautiful formatting ke liye underscores ko space se badal diya
        display_name = feature.replace('_', ' ')
        user_inputs[feature] = st.number_input(f"Enter {display_name}:", value=0.0)

st.markdown("---")

# 4. Prediction Button
if st.button("🔮 Predict Status", use_container_width=True):
    input_array = np.array([[user_inputs[f] for f in feature_list]])
    prediction = model.predict(input_array)
    predicted_label = target_classes[prediction[0]]
    
    st.subheader("🎯 Result:")
    st.success(f"Predicted Student Category/Status: **{predicted_label}**")