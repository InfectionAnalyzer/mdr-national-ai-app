import pickle

# Load models
def load_model(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

# Dictionary of all models by task
models = {
    'MDR_Present': load_model('MDR_Present_model.pkl'),
    'Dose_Error': load_model('Dose_Error_model.pkl'),
    'Timing_Error': load_model('Timing_Error_model.pkl'),
    'Route_Error': load_model('Route_Error_model.pkl'),
    'Resistance_Type': load_model('Resistance_Type_model.pkl'),
    'Infection_Onset': load_model('Infection_Onset_model.pkl'),
    'Antibiotic_Response': load_model('Antibiotic_Response_model.pkl'),
    'Resistance_Progression': load_model('Resistance_Progression_model.pkl'),
    'LMIC_Policy_Simulation': load_model('LMIC_Policy_Simulation_model.pkl'),
    'Economic_Impact': load_model('Economic_Impact_model.pkl'),
    'RL_Policy_Q_table': load_model('RL_Policy_Q_table.pkl')
}

def predict(task, input_df):
    if task in models:
        model = models[task]
        return model.predict(input_df)
    else:
        raise ValueError("Unknown task: " + task)
