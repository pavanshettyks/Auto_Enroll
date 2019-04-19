from selenium import webdriver
import unittest
import time

print("Opening the campus Portal")

driver = webdriver.Chrome(executable_path = r'C:\Users\Pavan\Documents\Python Scripts\chromedriver.exe');


#text_area = driver.find_element_by_id('textarea')
#text_area.send_keys("This text is send using Python code.")
username = input("Enter User Name: ")
password = input("Enter password: ")

driver.get('https://my.fullerton.edu/')
uname = driver.find_element_by_id('username')
uname.send_keys(username)

pwd = driver.find_element_by_id('password')
pwd.send_keys(password)


window_before = driver.window_handles[0]

window_before_title = driver.title
print(window_before_title)

sub = driver.find_element_by_class_name("LoginButton").click()

#Quit
driver.quit()
