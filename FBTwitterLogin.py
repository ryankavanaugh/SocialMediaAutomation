#=============================================================================================
#               Written in SELENIUM & PYTHON 3 By Ryan Kavanaugh
# INFO-> Program to login robo tester facebook account, login robo tester twitter account,
#       go to celebrity twitter page, and send my friend Ted a facebook friend request. <-
#=============================================================================================

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
#from selenium import time

    #Tools to disable web notifications in facebook
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--enable-save-password-bubble=false")

    #Open up facebook in chrome browser
url = "https://www.facebook.com/"
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)

    #Assign variables to text fields
firstName = driver.find_element_by_id("u_0_1")
lastName = driver.find_element_by_id("u_0_3")
email = driver.find_element_by_id("u_0_6")
password = driver.find_element_by_id("u_0_d")
month = Select(driver.find_element_by_id('month'))
day = Select(driver.find_element_by_id('day'))
year = Select(driver.find_element_by_id('year'))
gender = driver.find_element_by_id('u_0_h').click()
email2 = driver.find_element_by_id('u_0_9')

    #Input all of the user's information to sign them up for an account
firstName.send_keys("Timothy")
lastName.send_keys("Tehstah")
email.send_keys('TimothyTehstah@gmail.com')
email2.send_keys('TimothyTehstah@gmail.com') #This is for section confirming spelling of user email.
password.send_keys('Test12345$')
month.select_by_visible_text('Sep')
day.select_by_visible_text('27')
year.select_by_value('1991')

    #Create Account Button
driver.find_element_by_id('u_0_l').click()

    #Wait for main page to load
driver.implicitly_wait(6)

#===================================================================
#           Twitter     Section
#===================================================================

#Open Up Twitter
twitterurl = "https://twitter.com/TheRealTank"
twitterurldriver = webdriver.Chrome(chrome_options=chrome_options)
twitterurldriver.get(twitterurl)

twittername = twitterurldriver.find_element_by_class_name('js-signin-email')
twittername.send_keys('timothytehstah@gmail.com')
twitterpass = twitterurldriver.find_element_by_name('session[password]')
twitterpass.send_keys('Test12345$')
#
twitterurldriver.find_element_by_class_name('js-submit').click()

#Wait for browser to load
twitterurldriver.implicitly_wait(6)

#============================================================
#             Go To Ted's Page/Friend Request Ted
#============================================================

    #Take browser to Ted's page
driver.get('https://www.facebook.com/theodore.warner?ref=br_rs')

    #Adds Ted as a friend!
driver.find_element_by_id('u_0_13').click()

#=============================================================
#                          The End
#=============================================================

