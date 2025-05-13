import subprocess
import psutil
import platform
import streamlit as st
from pathlib import Path


ws_subprocess = None

def run_ws_demo():
    global ws_subprocess

    src_path = Path("../webscrape-app/src").resolve()
    command = ["npx", "tsx", "scraper.ts"]

    if platform.system() == "Windows":
        ws_subprocess = subprocess.Popen(command, shell=True, cwd=src_path)
    else:
        ws_subprocess = subprocess.Popen(command, shell=False, cwd=src_path)

    ws_subprocess.wait()


def terminate_ws_demo():
    global ws_subprocess

    if ws_subprocess:
        try:
            parent_process = psutil.Process(ws_subprocess.pid)

            if parent_process.is_running():
                for child_procs in parent_process.children(recursive=True):
                    try:
                        child_procs.terminate()
                        child_procs.wait(timeout=8)
                    except psutil.NoSuchProcess:
                        pass
                    except psutil.TimeoutExpired:
                        child_procs.kill()
                        
                parent_process.terminate()
                parent_process.wait(timeout=8)        
        except Exception as e:
            st.error("Error while terminating Demo: {e}")
            
        ws_subprocess = None


if __name__ == "__main__":
    pass
