import joblib
import numpy as np
import streamlit as st
from keras.models import load_model


def predict_from_model(example_odds, output_type="HDA"):
    model = load_model(f"../trained-modells/modells/keras-model-{output_type}.h5")
    scaler = joblib.load(f"../trained-modells/scalers/keras-scaler-{output_type}.pkl")

    match output_type:
        case "HDA":
            inverse_mapping = {0: "H", 1: "D", 2: "A"}
        case "1X2":
            inverse_mapping = {1: "1X", 0: "X2"}
        case _:
            raise ValueError(f"Unsupported output_type: {output_type}")

    example = np.array(example_odds).reshape(1, -1)
    example_scaled = scaler.transform(example)

    pred = model.predict(example_scaled)

    if output_type == "HDA":
        pred_label_index = np.argmax(pred)
    else:
        pred_label_index = int(pred[0][0] > 0.5)

    decoded_label = inverse_mapping[pred_label_index]

    st.write(f"Input odds: {example_odds}")
    st.write(f"Predicted result: {decoded_label}")

    return decoded_label

def predict_rf(
    example_odds,
    output_type="HDA",
    model_path="../trained-modells/modells/rf_model.pkl",
    scaler_path="../trained-modells/scalers/rf_scaler.pkl",
):
    match output_type:
        case "HDA":
            inverse_mapping = {0: "H", 1: "D", 2: "A"}
        case "1X2":
            inverse_mapping = {1: "1X", 0: "X2"}
        case _:
            raise ValueError("Invalid output_type")

    model_path = f"../trained-modells/modells/rf-model-{output_type}.pkl"
    scaler_path = f"../trained-modells/scalers/rf-scaler-{output_type}.pkl"

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    example = np.array([example_odds])
    example_scaled = scaler.transform(example)

    prediction = model.predict(example_scaled)[0]
    decoded = inverse_mapping[prediction]

    st.subheader("Random Forest Prediction")
    st.write(f"Input odds: {example_odds}")
    st.write(f"Predicted result: **{decoded}**")
