import logging
from datetime import datetime
import os

LOG_DIR = "housing logs"  #creating a directory name for all the logs
curr_time_stamp = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}" 
log_file_name=f"log_{curr_time_stamp}.log"

#creating a directory
os.makedirs(LOG_DIR,exist_ok=True)
file_path=os.path.join(LOG_DIR,log_file_name)

#configuring the logging, which can be imported in app.py
logging.basicConfig(filename=file_path,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s -%(message)s',
level=logging.INFO)