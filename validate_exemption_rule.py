import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from generate_synthetic_data import generate_synthetic_data

def predict_exemption(row):
    # Regra simples: isento se exemption_type != 'None'
    return row['exemption_type'] != 'None'

def validate_rule(df):
    df['predicted_flag'] = df.apply(predict_exemption, axis=1)
    y_true = df['exemption_flag']
    y_pred = df['predicted_flag']

    acc = accuracy_score(y_true, y_pred)
    tn, fp, fn, tp = confusion_matrix(
        y_true, y_pred, labels=[False, True]
    ).ravel()

    print(f"Acurácia: {acc:.2%}")
    print(f"True Negatives: {tn}")
    print(f"False Positives: {fp}")
    print(f"False Negatives: {fn}")
    print(f"True Positives: {tp}")

if __name__ == '__main__':
    df = generate_synthetic_data()
    validate_rule(df)
