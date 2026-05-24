from datetime import datetime
import os
import logging

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
log_file = os.path.join(os.path.dirname(__file__), LOG_FILE)
logging.basicConfig(filename=log_file, encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                level = logging.DEBUG)

logging.debug("Detailed diagnostic information.")
logging.info("Confirmation that things are working.")
logging.warning("An unexpected issue occurred.")