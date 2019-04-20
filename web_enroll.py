from selenium import webdriver
import unittest
import time

print("Opening the campus Portal")

#Need to use chrome driver not the direct extension
#Use http://chromedriver.chromium.org/downloads to download.
#Use the file Path
driver = webdriver.Chrome(executable_path = r'C:\Users\Pavan\Documents\Python Scripts\chromedriver.exe');

username = input("Enter User Name: ")
password = input("Enter password: ")

#Enter the campus portal
driver.get('https://my.fullerton.edu/')

#Full screen
driver.maximize_window()

#Search element username by id and populate it
uname = driver.find_element_by_id('username')
uname.send_keys(username)

#Search element password by id and populate it
pwd = driver.find_element_by_id('password')
pwd.send_keys(password)

#To tackle multiple windows being opened in the future
window_before = driver.window_handles[0]

window_before_title = driver.title
print(window_before_title)

sub = driver.find_element_by_class_name("LoginButton").click()

main_window = driver.current_window_handle
driver.find_element_by_id('986552').click()
child = driver.window_handles[1]
driver.switch_to.window(child)
#print ("Child Window ID is : %s" %child)
print("Child Window Title is : %s " %(driver.title))
#driver.find_element_by_xpath('//*[@id="gobutton"]').click()
#driver.find_element_by_id('DERIVED_SSS_SCL_SSS_GO_4$83$').click()
#Quit the browser
driver.quit()
