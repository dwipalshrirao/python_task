import datetime
import logging
import logging.handlers

LOG_FILENAME = 'log_file.log'

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME,mode='a', maxBytes=2*1024*1024, backupCount=100)


my_logger.addHandler(handler)
for i in range(100000):
    my_logger.debug(f'{datetime.datetime.now()} this is log data')
    
