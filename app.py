
import streamlit as st
import pandas as pd
from predictor import predict

st.set_page_config(page_title="MDR Risk & Misuse AI", layout="centered")
st.title("MDR & Antibiotic Misuse AI (India)")

st.markdown("Upload patient data to predict MDR risk, resistance type, misuse patterns, and policy impact.")

uploaded_file = st.file_uploader("Upload Patient CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    features = df.drop(columns=[
        'MDR_Present', 'Dose_Error', 'Timing_Error', 'Route_Error',
        'Resistance_Type', 'Infection_Onset', 'Antibiotic_Response',
        'Resistance_Progression', 'RL_Policy_Q_table',
        'LMIC_Policy_Simulation', 'Economic_Impact'
    ], errors='ignore')

    st.success("Data loaded. Generating predictions...")

    df['MDR_Predicted'] = predict("MDR_Present", features)
    df['Dose_Error'] = predict("Dose_Error", features)
    df['Timing_Error'] = predict("Timing_Error", features)
    df['Route_Error'] = predict("Route_Error", features)
    df['Resistance_Type'] = predict("Resistance_Type", features)
    df['Infection_Onset'] = predict("Infection_Onset", features)
    df['Antibiotic_Response'] = predict("Antibiotic_Response", features)
    df['Resistance_Progression'] = predict("Resistance_Progression", features)
    df['RL_Policy_Q_table'] = predict("RL_Policy_Q_table", features)
    df['LMIC_Policy_Simulation'] = predict("LMIC_Policy_Simulation", features)
    df['Economic_Impact'] = predict("Economic_Impact", features)

    st.subheader("Top Predictions (Preview)")
    st.dataframe(df.head(20))

    st.download_button("Download Full Results", df.to_csv(index=False), "mdr_predictions.csv")
else:
    st.info("Upload a CSV file to begin.")
