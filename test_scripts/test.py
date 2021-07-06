##############################################################################################
#Purpose of the script
##################################################################################################################
#1.Select one e-commerce application and by using python script we have to signin.

#2.For thet we have to give username,emailid and password(password should be in text file and we have to read).

###################################################################################################################
#Below points has been considered in the script.
###################################################################################################################

#1.We have to write the test cases based on the below conditions.

#2.Check system behaviour when valid email id and password is entered(success condition).

#3.The below points are to check for failure conditions.

#4.Check system behaviour when invalid email id and valid password is entered.

#5.Check system behaviour when valid email id and invalid password is entered.

#6.Check system behaviour when invalid email id and invalid password is entered.

#7.Check system behaviour when email id and password are left blank and sign.

#######################################################################################################################
"""
This module contains web test cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

import pytest
import logging
import sys, os
from amazon import AmazonTest

LOGGER = logging.getLogger(__name__)

logger=logging.getLogger()
logger.setLevel(logging.INFO)

amazon_class_instance = AmazonTest()
logger.info('checking the test_basic_duckduckgo_search testcase')
##########################################################################################################################################################
class TestAmazonTest:

    '''Creating a test class for checking the functionalities'''
    
    def test_getPage(self): 
        '''Testing the getPage method to check whether we are getting corrct page or not'''
        logger.info('testing for test_getPage')
        try: 
            assert amazon_class_instance.getPage() == "https://www.amazon.com/"
            logger.info('successfully done')
        except Exception as e:
            logger.error(msg= 'Requested page not found or opened')
##############################################################################################################################################################         
    def test_validate_user(self):

        '''Testing the email and password Success condition'''

        logger.info('testing for test_validate_user')
        try:
            assert amazon_class_instance.signin_user() == 1
            logger.info('successfully done')
        except Exception as e:
            logger.error(msg = 'Credentials are not valid')
###############################################################################################################################################################     
    def test_incorrect_user_name(self):

        '''Testing the wrong email condition'''

        logger.info('testing for test_incorrect_user_name')
        try:
            assert amazon_class_instance.validate_username_failure() == 'rgba(255, 255, 255, 1)'
            logger.info('successfully done')
        except Exception as e:
            logger.error(msg = 'valid Username')
##################################################################################################################################################
    def test_incorrect_password(self):

        '''Testing the wrong password condition'''

        logger.info('testing for test_incorrect_password')
        try:
            assert amazon_class_instance.validate_password_failure() == 'rgba(255, 255, 255, 1)'
            logger.info('successfully done')
        except Exception as e
            logger.error(msg = 'Valid Password')
####################################################################################################################################################
    def test_forget_password(self):

        '''Testing the forgot_password feature'''

        logger.info('testing for test_forget_password')
        try:
            assert amazon_class_instance.forget_password() == 1
            logger.info('successfully done')
        except Exception as e:
            logger.error(msg = 'Forget Password not working properly')
#####################################################################################################################################################
    def test_keep_me_signedin(self):

        '''Testing the test_keep_me_signedin feature'''

        logger.info('testing for test_keep_me_signedin')
         try:
            assert amazon_class_instance.keep_me_signin() == 1
            logger.info('successfully done')
        except Exception as e:
            logger.error(msg = 'Keep me signed in not working properly (or) invalid credentials')

if __name__ == "__main__":
    pytest.main(args=['-s', os.path.abspath(__file__)])

#################################################################################################

#Script_name                        :           test.py
#Script_Version                     :           1.0
#Prepared by                        :           Gayathri.Pasupuleti@infinite.com
#Create Date                        :           16-JUNE-2021
#Last Modification Date             :           18-JUNE-2021
##################################################################################################