import os
import numpy as np
import pandas as pd
from keras.models import load_model

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")

def load_models():
    mutation_model = load_model(os.path.join(MODEL_DIR, "UTUC_mutation_FNN_model.h5"))
    rna_model = load_model(os.path.join(MODEL_DIR, "UTUC_rna_FNN_model.h5"))
    return mutation_model, rna_model

def predict_group(mutation_file, rna_file):
    mutation_model, rna_model = load_models()
    mutation_data = pd.read_csv(mutation_file, sep='\t', index_col=0)
    rna_data = pd.read_csv(rna_file, sep='\t', index_col=0)
    mutation_input = mutation_data.T.values
    rna_input = rna_data.T.values
    mutation_pred = mutation_model.predict(mutation_input)
    rna_pred = rna_model.predict(rna_input)
    average_pred = (mutation_pred + rna_pred) / 2
    predicted_labels = np.argmax(average_pred, axis=1)
    sample_ids = mutation_data.columns
    result_df = pd.DataFrame({
        'Sample_ID': sample_ids,
        'Predicted_Group': ['SNF' + str(i+1) for i in predicted_labels]
    })
    return result_df