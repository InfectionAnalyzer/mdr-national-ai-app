# MDR & Antibiotic Misuse AI Dashboard (India)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mdr-policy-dashboard-ghmkblvtkknlrjaazkh4to.streamlit.app)

This dashboard supports:
- MDR prediction
- Dose, Timing, Route misuse errors
- Resistance mechanism classification
- Infection onset, antibiotic response prediction
- Resistance progression, economic modeling
- LMIC policy simulation

## Deployment (Mobile-Friendly)

**Upload files manually to GitHub**

1. Use GitHub mobile or Termux to push all files in root.
2. Deploy to [Streamlit Cloud](https://streamlit.io/cloud)

## Local Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Files
- `app.py`, `predictor.py`
- `requirements.txt`, `README.md`
- All `.pkl` models
