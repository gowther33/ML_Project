"""
Here we create our custom exceptions
"""

import sys
from src.logger import logging

# Whenever an exception occurs this message will be displayed
def error_message_detail(error, error_details:sys):
    # It returns 3 things the 3rd will give us on which file and line exception occurred
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(file_name, exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details=error_details)

    def __str___(self):
        return self.error_message
    
# test
if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as E:
        logging.info("Divide by Zero")
        raise CustomException(E, sys)
