import generate_clean_json.preclean
import stats.wdl_counter as stats_wdl
import stats.filter_and_sort_df as stats_filter_sort
import generate_clean_json
from config_class import Config


config = Config()


def select_mode(filepath):
    match config.get_mode():
        case "Data":
            call_data_clean_to_file(filepath)
        case "Stat":
            call_stat(filepath)
        case "FilterSort":
            call_filter_sort(filepath)


def call_stat(filepath):
    if config.get_debug is True:
        print(f"Filepath: {filepath}")

    stats_wdl.df_wdl_counter(stats_filter_sort.filter_and_sort_df(filepath))

def call_filter_sort(filepath):
    if config.get_debug is True:
        print(f"Filepath: {filepath}")

    stats_filter_sort.filter_and_sort_df(filepath)

def call_data_clean_to_file(filepath):
    if config.get_debug is True:
        print(f"Filepath: {filepath}")

    generate_clean_json.preclean.clean_all()


if __name__ == "__main__":
    pass
