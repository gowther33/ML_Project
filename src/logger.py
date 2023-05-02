import logging
import os
from datetime import datetime

# Get date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%M_%S')}.log"
# Get filename
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# Even if the dir exists keep on appending in it
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Change functionality of logging
# format is message format: timestamp lineNumber name logLevelName message

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")