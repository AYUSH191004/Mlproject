import logging
import os
from datetime import datetime

Log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logfile",Log_file)
os.makedirs(log_path,exist_ok=True)
Logfile_path=os.path.join(Log_file,log_path)
logging.basicConfig(filename=Logfile_path,level=logging.info,format="[%(asctime)s]- %(lineno)d %(name)s -%(levelname)s %(message)")
