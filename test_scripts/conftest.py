# Purpose of the script
##############################################################################################
# 1.Sending the input for test files
##############################################################################################
# contents of the script:
##############################################################################################
# 1. To store the data in the log file..
##############################################################################################

import pytest
from datetime import datetime, date
import logging

logger=logging.getLogger(__name__)

 ''' To store the error methods in a log file'''
 
def pytest_assertrepr_compare(left, right):
    # if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
    logger.info(msg='')
    logger.error('Comparing Foo instances:','   vals: %s != %s\n' % (left, right))
    return ['Comparing Foo instances:','   vals: %s != %s\n' % (left, right)]


def pytest_configure(config):
    '''Creates a log file if log file is not mentioned in the .ini file'''
    if not config.option.log_file:
        timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H_%M_%S')
        #This will create a new log filw with current datestamp
        config.option.log_file = 'test.log'


###################################Script Details#######################################################################

# Script name               :       conftest.py
# Script version            :       1.0
# Prepared By               :       Gayathri.Pasupuleti@gmail.com
# Create Date               :       15-june-2021
# Last Modification Date    :       18-june-2021

##########################################################################################################
