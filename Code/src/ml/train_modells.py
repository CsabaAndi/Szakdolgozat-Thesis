import numpy as np
import pandas as pd
import joblib
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import Callback, EarlyStopping
import data_man.data_adapter as data_adapter
import stats.wdl_counter as wdl_counter
from config_class import Config


pd.options.plotting.backend = "plotly"

config = Config()
config.set_side_team("Arsenal")

config.set_config_dict(
    {
        "Side-checkbox": False,
        "Side-value": "All ",
        "Side-team": "Dev-team",
        "League-checkbox": False,
        "Wdl-checkbox": False,
        "Wdl-value": "Win",
        "Goal-checkbox": False,
        "Goal-mode": "between",
        "Goal-between-all-low": 0,
        "Goal-between-all-high": 100,
        "Goal-between-x-low": 0,
        "Goal-between-x-high": 100,
        "Goal-between-y-low": 0,
        "Goal-between-y-high": 100,
        "Goal-sort-checkbox": False,
        "Goal-sort-column": "all_goals",
        "Goal-sort-order": "Ascending",
        "Date-checkbox": False,
        "Date-start-end-format": r"%d/%m/%Y",
        "Date-sort": False,
        "Date-filter-start": "",
        "Date-filter-end": "",
        "Date-sort-order": "Ascending",
    }
)

class StreamlitLogger(Callback):
    def __init__(self, log_callback):
        super().__init__()
        self.log_callback = (
            log_callback
        )

    def on_epoch_end(self, epoch, logs=None):
        log_line = f"Epoch {epoch+1}/{self.params['epochs']} ━ "
        log_line += f"accuracy: {logs['accuracy']:.4f} - loss: {logs['loss']:.4f} - "
        log_line += f"val_accuracy: {logs['val_accuracy']:.4f} - val_loss: {logs['val_loss']:.4f}\n"
        self.log_callback(log_line) 

def load_data():
    path = r"../../Data/datasets/football-data-co-uk/Cleaned-Data/Main-Leagues/seasons_combined/Seasons_leagues_combined.csv"
    df = wdl_counter.filter_and_sort_df(
        data_adapter.adapt(path, extended_ml_model=True)
    )
    df = df.drop(columns=["wdl"], errors="ignore")

    return df

def train_keras_model(
    output_type="HDA",
    model_path="../trained-modells/modells/keras_model.h5",
    scaler_path="../trained-modells/scalers/keras_scaler.pkl",
    log_callback=None,
):
    df = load_data()

    logger = StreamlitLogger(log_callback)

    match output_type:
        case "HDA":
            result_mapping = {"H": 0, "D": 1, "A": 2}
            activation_three = "softmax"
            loss_function = "sparse_categorical_crossentropy"
            output_units = 3
            X = df[["B365H", "B365D", "B365A"]].values
            y = df["FTR"].map(result_mapping).values

        case "1X2":
            result_mapping = {"H": 1, "D": 1, "A": 0}
            activation_three = "sigmoid"
            loss_function = "binary_crossentropy"
            output_units = 1

            X = df[["B365H", "B365D", "B365A"]].values
            y = df["FTR"].map(result_mapping).values
            y = y.astype(np.float32 if output_units == 1 else np.int32)
        case _:
            raise ValueError("Invalid output_type")

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    model = Sequential(
        [
            Dense(16, activation="relu", input_shape=(3,)),
            Dense(8, activation="relu"),
            Dense(output_units, activation=activation_three),
        ]
    )

    model.compile(optimizer="adam", loss=loss_function, metrics=["accuracy"])

    early_stopping = EarlyStopping(
        monitor="val_loss", patience=5, restore_best_weights=True
    )

    model.fit(
        X_train,
        y_train,
        epochs=50,
        validation_split=0.2,
        batch_size=16,
        verbose=1,
        callbacks=[early_stopping, logger],
    )

    model_path = f"../trained-modells/modells/keras-model-{output_type}.h5"
    scaler_path = f"../trained-modells/scalers/keras-scaler-{output_type}.pkl"

    model.save(model_path)
    joblib.dump(scaler, scaler_path)

    test_accuracy = model.evaluate(X_test, y_test, verbose=0)[1]
    st.write(f"Model trained. Test Accuracy: {test_accuracy:.2%}")

def train_rf_model(
    output_type="HDA",
    model_path="../trained-modells/modells/rf_model.pkl",
    scaler_path="../trained-modells/scalers/rf_scaler.pkl",
):
    df = load_data()

    match output_type:
        case "HDA":
            result_mapping = {"H": 0, "D": 1, "A": 2}
        case "1X2":
            result_mapping = {"H": 1, "D": 1, "A": 0}
        case _:
            raise ValueError("Invalid output_type")

    X = df[["B365H", "B365D", "B365A"]].values
    y = df["FTR"].map(result_mapping).values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    st.write(f"Random Forest model trained. Accuracy: {accuracy:.2%}")

    model_path = f"../trained-modells/modells/rf-model-{output_type}.pkl"
    scaler_path = f"../trained-modells/scalers/rf-scaler-{output_type}.pkl"

    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)


if __name__ == "main":
    pass
