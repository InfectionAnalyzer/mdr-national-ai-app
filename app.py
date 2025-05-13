import streamlit as st
import pandas as pd
from predictor import predict

st.set_page_config(layout="wide")
st.title("Future: MDR Risk & Antibiotic Misuse Prediction")

uploaded_file = st.file_uploader("Upload Patient CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    features = df.drop(columns=[
        'MDR_Present', 'Dose_Error', 'Timing_Error', 'Route_Error', 'Resistance_Type'
    ], errors='ignore')

    st.subheader("Predictions")

    # Core predictions
    df['MDR_Predicted'] = predict("MDR_Present", features)
    df['Dose_Error'] = predict("Dose_Error", features)
    df['Timing_Error'] = predict("Timing_Error", features)
    df['Route_Error'] = predict("Route_Error", features)
    df['Resistance_Type'] = predict("Resistance_Type", features)

    # Show predictions
    st.dataframe(df.head(50))

    # Download output
    st.download_button("Download Results", df.to_csv(index=False), file_name="mdr_predictions.csv")
else:
    st.info("Please upload a CSV to begin.")