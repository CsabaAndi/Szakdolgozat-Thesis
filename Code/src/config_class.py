import debug_out
import pandas as pd


class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self._mode = ""
        self._table_type = ""
        self._stat_config_dict = {"init", "initalized"}
        self._loop = False
        self._country = "Unspecified"
        self._debug = False
        self._initialized = True

    def set_debug(self, debug_bool):
        self._debug = debug_bool

    def get_debug(self):
        return self._debug

    def set_loop(self, loop_var):
        self._loop = loop_var

    def get_loop(self):
        return self._loop

    def set_country(self, country_str):
        self._country = country_str

    def get_country(self):
        return self._country

    def set_league(self, league_str="Unspecified"):
        self._league = league_str

    def get_league(self):
        return self._league

    def set_side_team(self, team_name):
        if isinstance(self._stat_config_dict, dict):
            self._stat_config_dict["Side-team"] = team_name

    def get_side_team(self):
        return self._stat_config_dict.get("Side-team", None)

    def set_mode(self, mode_var):
        self._mode = mode_var

    def get_mode(self):
        return self._mode

    def set_config_dict(self, config_dict: dict):
        self._stat_config_dict = config_dict

    def get_config_dict(self):
        return self._stat_config_dict

    def print_config(self):
        config_df = pd.DataFrame(
            self._stat_config_dict.items(), columns=["Config-Keys", "Config-Values"]
        )
        debug_out.print_df(config_df)
