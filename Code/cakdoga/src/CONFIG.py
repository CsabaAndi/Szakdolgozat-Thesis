import debug_out
import pandas as pd
# -------------------------------------------------------- [ Filter / Sort / etc ] ---------------------------------------------------------


class Config:
    _instance = None  # Singleton instance
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return

        # Initialize all config properties
        self._mode = "asd"
        self._table_type = ""
        self._mh_config_dict = {"asd", "asd"}

        self._loop = False
        self._country = "Placeholder"

        self._debug = False

        self._initialized = True
    
    # ---------------------------- [todo] ------------------------------
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

    # ------------------------- Mode Configuration -------------------------
    def set_mode(self, mode_var):
        self._mode = mode_var
        
    def get_mode(self):
        return self._mode

    # ---------------------- Table Type Configuration ----------------------
    def set_table_type(self, table_mode_var):
        self._table_type = table_mode_var
        
    def get_table_type(self):
        return self._table_type

    # -------------------- Match History Configuration ---------------------
    def set_match_history_config(self, config_dict: dict):
        self._mh_config_dict = config_dict
        
    def get_match_history_config(self):
        return self._mh_config_dict

    # ------------------------ Common Functionality ------------------------
    def print_config(self):

        print(f"Current Mode: {self._mode}")
        print(f"Table Type: {self._table_type}")
        
        print("\nMatch History Configuration:")
        config_df = pd.DataFrame(self._mh_config_dict.items(), 
                               columns=["Config-Keys", "Config-Values"])
        
        debug_out.print_df(config_df)

# ----------------------------[ Terminal Colors ]-----------------------------
COLORS = {
    "BLACK": '\033[30m',
    "RED": '\033[31m',
    "GREEN": '\033[32m',
    "YELLOW": '\033[33m',
    "BLUE": '\033[34m',
    "MAGENTA": '\033[35m',
    "CYAN": '\033[36m',
    "RESET": '\033[0m'
    # ... (rest of color definitions)
}


# -------------------------------------------------------- [ Filter / Sort / etc ] ---------------------------------------------------------


# ----------------------------[ Colors for terminal ]-----------------------------

COLORS = {
    "BLACK": '\033[30m',
    "RED": '\033[31m',
    "GREEN": '\033[32m',
    "YELLOW": '\033[33m', # orange on some systems
    "BLUE": '\033[34m',
    "MAGENTA": '\033[35m',
    "CYAN": '\033[36m',
    "LIGHT_GRAY": '\033[37m',
    "DARK_GRAY": '\033[90m',
    "BRIGHT_RED": '\033[91m',
    "BRIGHT_GREEN": '\033[92m',
    "BRIGHT_YELLOW": '\033[93m',
    "BRIGHT_BLUE": '\033[94m',
    "BRIGHT_MAGENTA": '\033[95m',
    "BRIGHT_CYAN": '\033[96m',
    "WHITE": '\033[97m',

    "RESET": '\033[0m' # called to return to standard terminal text color
}

# ----------------------------[ Colors for terminal ]-----------------------------
