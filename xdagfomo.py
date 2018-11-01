from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.common.action_chains as a
from time import sleep
from urllib.request import urlretrieve
#You should be using Robot to send all of your key presses to the system level Alert. Including your user and PW.
#A security dialogue is not a JavaScript level dialogue box
driver = webdriver.Firefox()
driver.get('http://fomoxdag.xdagpark.com/archive.html')#http://fomoxdag.xdagpark.com/')
sleep(5)
site=driver.find_elements_by_xpath("//span[@class='font-weight-bold play-item-value']")
for el in site:#div/p[@class='color-pink']/text()"):
    print (el.get_attribute('innerHTML'), end='')
for c1 in site:
	print(str(c1))
	print(c1.get_attribute('text'))#.get_attribute('text'))
#content=driver.find_element_by_class_name('color-pink')
for c1 in site:
	print(c1.get_attribute("innerhtml"))
actions = a.ActionChains(driver)
actions.send_keys(Keys.ESCAPE)
actions.perform()
#print (driver.page_source)
#//div[contains(@class, "myClass")]/img/@src
#https://homeport.rccl.com/people-finder/?query=85000731&pg=2