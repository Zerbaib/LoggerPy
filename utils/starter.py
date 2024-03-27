import os
from utils.var import *
from datetime import datetime

def get_next_log_file():
    log_folder = log_folder_path
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    for i in range(max_log_files):
        log_file = os.path.join(log_folder, f"{i}.log")
        if not os.path.exists(log_file):
            os.mknod(log_file)
            return log_file
    raise Exception("Maximum number of log files reached.")

def get_last_log_file():
    log_folder = log_folder_path
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    for i in range(10000):
        log_file = os.path.join(log_folder, f"{i}.log")
        if not os.path.exists(log_file):
            return os.path.join(log_folder, f"{i-1}.log")
    raise Exception("Maximum number of log files reached.")