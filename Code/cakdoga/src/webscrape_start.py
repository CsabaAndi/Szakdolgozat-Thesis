import subprocess
import sys
import os
import psutil

# Global reference for the subprocess
datanode_subprocess = None

def run_datanode_app():
    global datanode_subprocess

    # Define the path to the src folder
    src_path = os.path.abspath('../webscrape-app/datanode/src')

    command = ["npx", "ts-node", "scraper.ts"]

    # Run datanode
    datanode_subprocess = subprocess.Popen(command, shell=False, cwd=src_path)
    
    return datanode_subprocess


def terminate_datanode_app():
    global datanode_subprocess
    
    if datanode_subprocess:
        # Get the parent PID of the subprocess
        parent_pid = datanode_subprocess.pid
        
        # Use psutil to find child processes of the parent PID
        parent_process = psutil.Process(parent_pid)
        
        # Kill the parent process and all its child processes
        for child in parent_process.children(recursive=True):  # Include child processes
            child.terminate()  # Try gracefully first
        
        # Finally kill the parent process if needed
        parent_process.terminate()
        parent_process.wait()  # Ensure it terminates properly
        print("Process terminated")
    datanode_subprocess = None


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        function_name = sys.argv[1]
        globals()[function_name]()
    else:
        print("No function specified.")