import subprocess
import sys
import os
import psutil
import platform

# Global reference for the subprocess
datanode_subprocess = None

def run_datanode_app(arg_loop = False, arg_page = 2):
    global datanode_subprocess

    # Define the path to the src folder
    src_path = os.path.abspath('../webscrape-app/datanode/src')

    command = ["npx", "ts-node", "scraper.ts", "-l", f"{arg_loop}", "-p", f"{str(arg_page)}"]
    
    # Run datanode
    if platform.system() == 'Windows':
        # Windows
        datanode_subprocess = subprocess.Popen(command, shell=True, cwd=src_path)
    else:  
        # Linux, macOS, or other systems
        datanode_subprocess = subprocess.Popen(command, shell=False, cwd=src_path)
        
    datanode_subprocess.wait()
    

"""
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
"""
    
def terminate_datanode_app():
    global datanode_subprocess
    
    if datanode_subprocess:
        try:
            # Get the parent PID of the subprocess
            parent_pid = datanode_subprocess.pid
            
            # Use psutil to find child processes of the parent PID
            parent_process = psutil.Process(parent_pid)
            
            # Ensure the process is running
            if parent_process.is_running():
                # Attempt to terminate child processes gracefully
                for child in parent_process.children(recursive=True):
                    try:
                        child.terminate()  # Try gracefully first
                        child.wait(timeout=5)  # Wait for child to terminate gracefully (timeout of 5 seconds)
                    except psutil.NoSuchProcess:
                        print(f"Child process {child.pid} has already terminated.")
                    except psutil.TimeoutExpired:
                        print(f"Child process {child.pid} did not terminate gracefully, force killing...")
                        child.kill()  # Force kill if needed

                # Finally, terminate the parent process if it’s still alive
                parent_process.terminate()
                parent_process.wait(timeout=5)  # Ensure the parent process terminates properly
                print("Parent process terminated successfully.")
            else:
                print(f"Process with PID {parent_pid} is not running.")
                
    
        except psutil.NoSuchProcess:
            print(f"Process with PID {parent_pid} no longer exists.")
        except psutil.AccessDenied:
            print(f"Access denied to process {parent_pid}.")
        except psutil.ZombieProcess:
            print(f"Process {parent_pid} is a zombie process and already terminated.")
        except Exception as e:
            print(f"Error while terminating process: {e}")

        # Set subprocess to None to ensure it's no longer referenced
        datanode_subprocess = None
    else:
        print("No datanode subprocess to terminate.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        function_name = sys.argv[1]
        globals()[function_name]()
    else:
        print("No function specified.")