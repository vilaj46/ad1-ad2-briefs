import psutil
import os


def check_server():
    current_pid = os.getpid()
    for proc in psutil.net_connections():
        if 5000 == proc.laddr[1] and proc.pid != current_pid:
            try:
                p = psutil.Process(proc.pid)
                p.terminate()
            except:
                pass
