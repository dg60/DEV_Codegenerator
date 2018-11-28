
import logging

logging.basicConfig(filename='app.log',
                    filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('This will get logged to a file')