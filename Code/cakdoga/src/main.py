import subprocess
import sys
import argparse
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

def run_streamlit_app(headless, port):
    streamlit_main_page_path = os.path.abspath('stream/main_page.py')
    
    # Path to the Python interpreter in your virtual environment
    venv_python = sys.executable
    
    subprocess.run([venv_python, "-m", "streamlit", "run", streamlit_main_page_path, f"--server.headless={headless}", f"--server.port={port}"])
    

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Run a Streamlit app with custom arguments.")
    
    parser.add_argument('--headless', type=bool, default=False, help="Run Streamlit in headless mode (no browser).")
    parser.add_argument('--port', type=int, default=8501, help="Specify the port for Streamlit to run on.")
    
    args = parser.parse_args()
    run_streamlit_app(args.headless, args.port)
