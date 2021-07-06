'''Implementing methods for signin with valid credentials to the amazon application'''

from selenium import webdriver
import time

# Storing the Driver, webpage url and username inside a dictionary
DATA = {"Driver": webdriver.Chrome("/usr/local/bin/chromedriver"),
           "URL": "https://www.amazon.com",
           "username": "gayathri.p.214@gmail.com",
           }

''' Reading the data from the text file and storing it inside a variable.'''

with open('password.txt', 'r') as f:
    password = f.read()

class AmazonTest:

    '''Creating a class for checking the functionality.'''

    def __init__(self):
        
        self.driver = DATA["Driver"]
        self.URL = DATA["URL"]
        self.user = DATA["username"]
        self.password = str(password)
        self.Is_loggedin = False

###########################################################################################################################
    def getPage(self):

        '''To check Whether we are browsing the correct Page'''

        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.current_url = self.driver.current_url
        return self.current_url
#############################################################################################################################
    def user_name(self):

        ''' To Fill the username checkbox with given username.'''

        self.user_input = self.driver.find_element_by_id("ap_email").send_keys(self.user)
#############################################################################################################################
    def continue_click(self):

        '''To click the continue button automatically'''

        self.continue_check = self.driver.find_element_by_id("continue").click()
###############################################################################################################################                            
    def password_user(self):

        '''To fill the password checkbox automatically'''

        self.pass_input = self.driver.find_element_by_id("ap_password").send_keys(self.password)
##################################################################################################################################
    def account_list(self):

        '''Traverse through the given web page and click on the signin link.'''

        self.driver.get('https://www.amazon.com')
        self.nav_account_list = self.driver.find_element_by_id("nav-link-accountList").click()

########################################################################################################################################### 
    def submit_button(self):

        '''To click the submit button automatically'''

        self.submit_button = self.driver.find_element_by_id("signInSubmit").click()
###########################################################################################################################################       
    def get_color(self):

        '''To get the colour of the required element in webpage.'''

        element = self.driver.find_element_by_id('auth-error-message-box')
        res = element.value_of_css_property('background-color')
        return res
############################################################################################################################################
    def signin_user(self):

        ''' To Validate whether the given username and password are correct or not'''
        
        # Calling the account_list method
        self.account_list()
        time.sleep(3)
        # Calling the user_name() method
        self.user_name()
        time.sleep(1)
        # Calling the continue_click() method
        self.continue_click()
        time.sleep(1)
        # Calling the password_user() method
        self.password_user()
        time.sleep(1)
        # Calling the submit_button() method
        self.submit_button()
        time.sleep(1)

        # trying to check whether the username is present or not
        try:
            self.nav_account_list = self.driver.find_element_by_id("nav-your-amazon").click()
            return True
        except Exception:
            return False
############################################################################################################################################
    def validate_username_failure(self):

        '''To check whether the username is correct or not.'''

        # Calling the account_list method
        self.account_list()
        time.sleep(3)
        # Calling the user_name() method
        self.user_name()
        time.sleep(1)
        # Calling the continue_check() method
        self.continue_click()
        time.sleep(1)
        # Calling the get_color method and storing the result in the colour variable
        colour = self.get_color()
        return colour
##############################################################################################################        
    def validate_password_failure(self):

        '''To check whether the password is correct or not'''
            
         # Calling the account_list method
        self.account_list()
        time.sleep(3)
        # Calling the user_name() method
        self.user_name()
        time.sleep(3)
        # Calling the continue_check() method
        self.continue_click()
        time.sleep(3)
        # Calling the password_user() method
        self.password_user()
        time.sleep(3)
        # Calling the submit_button() method
        self.submit_button()
        # Calling the get_color method and storing the result in the colour variable
        colour = self.get_color()
        return colour
        
#####################################################################################################################
    def forget_password(self):

        ''' To Check whether is forget password is working properly or not.'''

        # Calling the account_list method
        self.account_list()
        time.sleep(3)
        # Calling the user_name() method
        self.user_name()
        time.sleep(1)
        # Calling the continue_check() method
        self.continue_click()
        time.sleep(1)
        # Trying to check whether the forget password is working or not
        try:
            # Clicking on the forget password button
            forget_password_link = self.driver.find_element_by_id("auth-fpp-link-bottom").click()
            # Calling the continue_check() method
            self.continue_click()
            time.sleep(50)
            # Clicking the submit button
            click = self.driver.find_element_by_id('cvf-submit-otp-button').click()
            # Assigning the new password 
            new_pass = 'abc@123'
            # Entering the new password in the required field
            new_password = self.driver.find_element_by_id("ap_fpp_password").send_keys(new_pass)
            retype_password = self.driver.find_element_by_id("ap_fpp_password_check").send_keys(new_pass)

            # Calling the Continue_click() method
            self.continue_click()
            return True
        except Exception as e:
            return False

############################################################################################################################
    def keep_me_signin(self):

        '''To check whether keep me signed in button is working properly or not.'''
        
        self.account_list()
        time.sleep(3)
        self.user_name()
        time.sleep(3)
        self.continue_click()
        time.sleep(3)
        self.password_user()
        time.sleep(3)

        try:
            check_box = self.driver.find_element_by_xpath('//*[@id="authportal-main-section"]/div[2]/div/div/div/form/div/div[2]/div/div/label/div/label/input').click()
            return True
        except Exception :
            return False
            
obj1 = AmazonTest()
obj1.getPage()
obj1.user_name()
#obj1.continue_click()
#obj1.password_user()