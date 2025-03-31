import dataman.mh_data_man
import numpy as np
import pandas as pd
import tensorflow as tf
import debug_out
import dataman
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import warnings

pd.options.plotting.backend = "plotly"

import streamlit as st


def baseline():
    all_mh_df = pd.read_json(r"../output/data/processed/match-history/compressed/all_countries.json")
    dataman.mh_data_man.set_df_goal_cols(df=all_mh_df)

    # ez szar lesz mer nem home / away nincs nézve
    all_mh_df["gut"] = all_mh_df["Goal_X"] >= all_mh_df["Goal_Y"]



    with st.container(border=True):
        st.write(all_mh_df.head(15))
        st.write('Min:', all_mh_df["all_goals"].min())
        st.write('Max:', all_mh_df["all_goals"].max())
        st.write('Átlag:', all_mh_df["all_goals"].mean())
        st.write('Medián:', all_mh_df["all_goals"].median())
        st.write('Szórás:', all_mh_df["all_goals"].std())
        st.write('describe', all_mh_df.describe())
        st.write('hist?', all_mh_df["all_goals"].hist(bins=1000))
        st.write("false! accuracy:", all_mh_df["gut"].value_counts()[True] / len(all_mh_df))


def sckiittest():
    warnings.filterwarnings('ignore')

    # Corrected URL for the dataset
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    titanic_data = pd.read_csv(url)

    # Drop rows with missing 'Survived' values
    titanic_data = titanic_data.dropna(subset=['Survived'])

    # Features and target variable
    X = titanic_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
    y = titanic_data['Survived']

    # Encode 'Sex' column
    X.loc[:, 'Sex'] = X['Sex'].map({'female': 0, 'male': 1})

    # Fill missing 'Age' values with the median
    X.loc[:, 'Age'].fillna(X['Age'].median(), inplace=True)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize RandomForestClassifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

    # Fit the classifier to the training data
    rf_classifier.fit(X_train, y_train)

    # Make predictions
    y_pred = rf_classifier.predict(X_test)

    # Calculate accuracy and classification report
    accuracy = accuracy_score(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred)

    # Print the results
    print(f"Accuracy: {accuracy:.2f}")
    print("\nClassification Report:\n", classification_rep)

    # Sample prediction
    sample = X_test.iloc[0:1]  # Keep as DataFrame to match model input format
    prediction = rf_classifier.predict(sample)

    # Retrieve and display the sample
    sample_dict = sample.iloc[0].to_dict()
    print(f"\nSample Passenger: {sample_dict}")
    print(f"Predicted Survival: {'Survived' if prediction[0] == 1 else 'Did Not Survive'}")

    

if __name__ == "main":
    pass