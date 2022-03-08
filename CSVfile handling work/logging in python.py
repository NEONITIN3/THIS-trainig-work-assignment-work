''''''
# there are 5 standard levels indicating the severity of events
from venv import logger

"""The logging module in Python is a ready-to-use and powerful module that is
designed to meet the needs of beginners as well as enterprise teams. It is used
by most of the third-party Python libraries, so you can integrate your log messages with
the ones from those libraries to produce a homogeneous log for your application."""

import logging
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

"""Notice that the debug() and info() messages didn’t get logged. 
This is because, by default, the logging module logs the messages with a severity 
level of WARNING or above"""


# level of configuration

# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will get logged')

# exception  Information
# a = 5
# b = 0
#
# try:
#   c = a / b
# except Exception as e:
#   logging.warning("Exception occurred", exc_info=True)
# #So
#
# a = 5
# b = 0
# try:
#   c = a / b
# except Exception as e:
#   logging.exception("Exception occurred")
#
#classes and function

"""logging module whenever its functions are called directly like this: logging.debug(). 
You can 
define your own logger by creating an object of the Logger class,"""

"""The most commonly used classes defined in the logging module are the following:

1.Logger:      This is the class whose objects will be used in the  
               application code directly to call the functions.

2.LogRecord: Loggers automatically create LogRecord objects that have
          all the information related to the event being logged, like the name of the logger, 
          the function, the line number, the message, and more.

3.Handler: Handlers send the LogRecord to the required output 
          destination, like the console or a file. Handler is a base for subclasses 
           like StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and more. 
          These subclasses send the logging outputs to corresponding destinations, 
          like sys.stdout or a disk file.

4.Formatter: This is where you specify the format of the output by 
          specifying a string format that lists out the attributes 
          that the output should contain.
"""




#
import logging

# logger = logging.getLogger('example_logger')
# logger.critical('This is a warning')
#
'''This creates a custom logger named example_logger, but unlike the root logger,
the name of a custom logger is not part of the default output format'''
#Create a custom logger

# logger = logging.getLogger(__name__)

# Create handlers
# c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('file.log')
# c_handler.setLevel(logging.WARNING)
# f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# f_format = logging.Formatter('%(asctime)s -"nitin" - %(levelname)s - %(message)s')
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)

# Add handlers to the logger
# logger.addHandler(c_handler)
# logger.addHandler(f_handler)
#
# logger.warning('This is a warning')
# logger.error('This is an error')
n=8
m=0
if n==m:
    print("neo")
else:
    f_handler = logging.FileHandler('file.log')
    f_format = logging.Formatter('%(asctime)s -"nitin" - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    logger.warning('This is a warning')
