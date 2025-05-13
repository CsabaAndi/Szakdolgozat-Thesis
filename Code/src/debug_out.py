from contextlib import contextmanager
import time
import config_class as config_class


@contextmanager
def timed():
    start_time = time.time()
    yield
    end_time = time.time()
    print(
        "Total execution time: \033[31;1;4m{}\033[0m sec".format(end_time - start_time)
    )


def print_df(df):
    config = config_class.Config()
    if config.get_debug() is True:
        print(
            df.to_markdown(
                tablefmt="grid", numalign="center", stralign="center", index=False
            )
        )
