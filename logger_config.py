# logger_config.py
import logging
import os
from datetime import datetime

# Create logs directory
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Generate timestamped log file name
log_filename = datetime.now().strftime("mpt_%Y-%m-%d_%H-%M-%S.log")
log_path = os.path.join(log_dir, log_filename)

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(name)s] %(message)s',
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler()
    ]
)
