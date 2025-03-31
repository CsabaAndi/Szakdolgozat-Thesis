import subprocess
import sys

def run_streamlit_app():
    # Path to your Streamlit app script
    script_path = "main_page.py"
    
    # Path to the Python interpreter in your virtual environment
    venv_python = sys.executable  # This gets the current Python interpreter (from the venv)
    
    # Run the Streamlit app using subprocess
    subprocess.run([venv_python, "-m", "streamlit", "run", script_path])

if __name__ == "__main__":
    run_streamlit_app()