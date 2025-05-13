import plotly.express as px
import streamlit as st
from config_class import Config


unique_id = {"value": 20007984564}

def wdl_graph(data):
    config = Config()
    title = f"{config.get_country()} | {config.get_league()} | Wins/Draws/Losses"

    fig = px.histogram(
        data,
        x="team",
        y=["won", "draw", "lost"],
        barmode="group",
        text_auto=True,
        labels={"team": "Team Name"},
        color_discrete_map={"won": "green", "draw": "yellow", "lost": "red"},
        title=title,
    ).update_layout(yaxis_title="W/D/L Counts", template="plotly_dark")

    fig.data[0].name = "Wins"
    fig.data[1].name = "Draws"
    fig.data[2].name = "Losses"

    with st.container(border=True):
        st.plotly_chart(fig, key=unique_id["value"])

    unique_id["value"] += 1
