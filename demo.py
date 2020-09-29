from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Kute\Python\Python Selenium Course Udemy\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.close()