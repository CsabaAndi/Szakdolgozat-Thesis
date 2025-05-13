import subprocess
import sys
import os
from pathlib import Path


root_path = Path(__file__).resolve()
sys.path.append(str(root_path.parents[1]))
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"


def run_streamlit_app(headless, port):
    streamlit_main_page_path = Path("stream/webapp.py").resolve()
    venv_python = sys.executable

    subprocess.run(
        [
            venv_python,
            "-m",
            "streamlit",
            "run",
            streamlit_main_page_path,
            f"--server.headless={headless}",
            f"--server.port={port}",
        ]
    )


if __name__ == "__main__":
    run_streamlit_app(False, 8501)
