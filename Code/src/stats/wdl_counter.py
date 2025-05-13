import pandas as pd
import visuals.graphs as graphs
import utils
from config_class import Config


def df_wdl_counter(df: pd.DataFrame) -> pd.DataFrame:
    config = Config()
    side_team = config.get_config_dict().get("Side-team", "Unknown")

    wdl_count = df["wdl"].value_counts().to_dict()

    win = wdl_count.get("win", 0)
    draw = wdl_count.get("draw", 0)
    lose = wdl_count.get("lose", 0)

    df_wdl = pd.DataFrame(
        [
            {
                "team": side_team,
                "won": str(win),
                "draw": str(draw),
                "lost": str(lose),
            }
        ]
    )

    if config.get_debug():
        print(
            f"---------------[{utils.COLORS['WHITE']}{side_team}{utils.COLORS['RESET']}]--------------------\n"
            f"won: {utils.COLORS['GREEN']}{win}{utils.COLORS['RESET']}, "
            f"draw: {utils.COLORS['YELLOW']}{draw}{utils.COLORS['RESET']}, "
            f"lost: {utils.COLORS['RED']}{lose}{utils.COLORS['RESET']}\n"
            f"---------------------------------------"
        )

    graphs.wdl_graph(df_wdl)

    return df_wdl


if __name__ == "__main__":
    pass
