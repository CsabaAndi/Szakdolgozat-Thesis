import streamlit as st
import generate_clean_json.generate_big_data as bigdata
from ml import train_modells, predictions
from config_class import Config


config = Config()

with st.sidebar:
    st.header("Predict outcome based on odds")
    st.header("Train Modells", help="asd")
    onextwo_rb = st.radio(
        label="Mode", options=["HDA", "1X2"], horizontal=True, key=6845687678
    )
    start_train = st.button(label="Trai: Keras", type="secondary")
    start_train_rf = st.button(label="Train: RF", type="secondary")

    st.header("Predict", help="Predict using the trained modells")

    h_odds = st.number_input(
        label="Home Odds",
        min_value=0.0,
        max_value=10.0,
        value=2.0,
        step=1.0,
        key=10000000,
    )
    d_odds = st.number_input(
        label="Draw Odds",
        min_value=0.0,
        max_value=10.0,
        value=2.0,
        step=1.0,
        key=15000000,
    )
    a_odds = st.number_input(
        label="Away Odds",
        min_value=0.0,
        max_value=10.0,
        value=2.0,
        step=1.0,
        key=20000000,
    )

    start_predict = st.button(label="Predict: Keras", type="secondary")
    start_predict_rf = st.button(label="Predict: RF", type="secondary")

if start_train:
    log_area = st.empty()

    def log_callback(msg):
        log_area.text(msg)

    with st.container():
        with st.spinner("Training model"):
            model = train_modells.train_keras_model(
                onextwo_rb, log_callback=log_callback
            )
    st.success("Training complete!")

if start_train_rf:
    with st.container():
        with st.spinner("Training model"):
            model = train_modells.train_rf_model(onextwo_rb)
    st.success("Training complete!")

if start_predict:
    with st.container():
        with st.spinner("Predicting..."):
            predictions.predict_from_model(
                [h_odds, d_odds, a_odds], output_type=onextwo_rb
            )
    st.success("Prediction complete!")

if start_predict_rf:
    with st.container():
        with st.spinner("Predicting..."):
            predictions.predict_rf([h_odds, d_odds, a_odds], output_type=onextwo_rb)
    st.success("Prediction complete!")
