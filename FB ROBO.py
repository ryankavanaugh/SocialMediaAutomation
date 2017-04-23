from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
#from selenium import time


#Tools to disable web notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--enable-save-password-bubble=false")




#Connect to facebook#################################
url = "https://www.facebook.com/"
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)

#Assign variables to text fields    1w       34d
firstName = driver.find_element_by_id("u_0_1")
lastName = driver.find_element_by_id("u_0_3")
email = driver.find_element_by_id("u_0_6")
password = driver.find_element_by_id("u_0_d")
month = Select(driver.find_element_by_id('month'))
day = Select(driver.find_element_by_id('day'))
year = Select(driver.find_element_by_id('year'))

#Selecting gender
gender = driver.find_element_by_id('u_0_h').click()

#Extra email
email2 = driver.find_element_by_id('u_0_9')

#Input all of the user's information
firstName.send_keys("Ryan")
lastName.send_keys("Kavanaugh")
email.send_keys('rjkavanaugh@gmail.com')
password.send_keys('Hulk1234')
month.select_by_visible_text('Aug')
day.select_by_visible_text('16')
year.select_by_value('1991')
    #Email confirmation
email2.send_keys('rjkavanaugh@gmail.com')

#Create Account Button
driver.find_element_by_id('u_0_l').click()


#Find Ted!!!777777777777777777777777777777777777777777777777777777777777777
driver.implicitly_wait(6)

    #assign a variable to the search bar for ted's name
tedsearch = driver.find_element_by_class_name("_1frb")

    #Type in ted's info
tedsearch.send_keys('Ted Warner New York')

    #click the search button
driver.find_element_by_class_name("_585_").click()

    #Wait for the page to load
driver.implicitly_wait(6)

driver.get('https://www.facebook.com/theodore.warner?ref=br_rs')

#ASKS TED TO BE MY FRIEND!!!!!!!
#driver.find_element_by_id('u_0_13').click()

#777777777777777777777777777777777777777777777777777777777777777777777777

# #Open Up Twitter #####################################
twitterurl = "https://twitter.com/TheRealTank"
#



twitterurldriver = webdriver.Chrome(chrome_options=chrome_options)
#
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})

twitterurldriver.get(twitterurl)
#
twitterurldriver.maximize_window()
#
twittername = twitterurldriver.find_element_by_class_name('js-signin-email')
twittername.send_keys('rjkavanaugh@gmail.com')
#
twitterpass = twitterurldriver.find_element_by_name('session[password]')
twitterpass.send_keys('Hulk1234')
#
twitterurldriver.find_element_by_class_name('js-submit').click()
#

twitterurldriver.implicitly_wait(6)

twitterurldriver.find_element_by_id('menu-0').click()
#
# #share the link
#link = twitterurldriver.find_element_by_class_name('js-dropdown-toggle')
#
#link.select_by_visible_text('Copy link to Tweet')