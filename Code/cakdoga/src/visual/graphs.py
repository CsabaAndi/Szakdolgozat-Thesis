#import plotly.graph_objects as go
import plotly.express as px

from CONFIG import Config
import streamlit as st


UNIQUE_ID = 2000 #gráfoknak kell egy UID

config = Config()

# ----------------------------------------------------------- [ Match Histroy ] ------------------------------------------------------------

# tezstelésre jo muxik , de nagyon kell a refactor rá
def wdl(data):
    global UNIQUE_ID
    Configuration = config.get_match_history_config()
    TITLE =  f"Match history - w/d/l data | {config.get_country()}"
    fig = px.histogram(data, x="team", y=["won", "draw", "lost"], barmode='group', text_auto=True,  
                       #labels={"team": "Teams"},
                       labels={"test": "asd"},
                       color_discrete_map={"won": "green", "draw": "yellow", "lost": "red"},
                       title=TITLE).update_layout(yaxis_title="W/D/L Counts",
                       template="plotly_dark")
    fig.add_annotation(
        text=f"""FILTERS: <br>  Side: {Configuration["Side-checkbox"]}<br>  Team: {Configuration["Side-value"]}<br>  League: {Configuration["League-checkbox"]}<br>  WDL: {Configuration["Wdl-checkbox"]}<br>    Value: {Configuration["Wdl-value"]}<br>  Date:<br>    From: {Configuration["Date-filter-start"]}<br>        To: {Configuration["Date-filter-end"]}""",
        align='left',
        showarrow=False,
        xref='paper',
        yref='paper',
        x=1.04,
        y=0.8,
        bordercolor='black',
        borderwidth=0
    )

    #fig.show()
    with st.container(border=True):
        st.plotly_chart(fig, key=UNIQUE_ID)
    UNIQUE_ID += 1



# ----------------------------------------------------------- [ Match Histroy ] ------------------------------------------------------------


# --------------------------------------------------------------- [ Tables ] ---------------------------------------------------------------


def tmp():
    pass


# --------------------------------------------------------------- [ Tables ] ---------------------------------------------------------------
