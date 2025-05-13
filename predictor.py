
import joblib

models = {
    "MDR_Present": joblib.load("MDR_Present_model.pkl"),
    "Dose_Error": joblib.load("Dose_Error_model.pkl"),
    "Timing_Error": joblib.load("Timing_Error_model.pkl"),
    "Route_Error": joblib.load("Route_Error_model.pkl"),
    "Resistance_Type": joblib.load("Resistance_Type_model.pkl"),
    "Infection_Onset": joblib.load("Infection_Onset_model.pkl"),
    "Antibiotic_Response": joblib.load("Antibiotic_Response_model.pkl"),
    "Resistance_Progression": joblib.load("Resistance_Progression_model.pkl"),
    "RL_Policy_Q_table": joblib.load("RL_Policy_Q_table.pkl"),
    "LMIC_Policy_Simulation": joblib.load("LMIC_Policy_Simulation_model.pkl"),
    "Economic_Impact": joblib.load("Economic_Impact_model.pkl"),
}

def predict(model_name, features):
    model = models[model_name]
    return model.predict(features)
