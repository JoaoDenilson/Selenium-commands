import time
from selenium import webdriver

browser = webdriver.Chrome()
#maximize_window()
browser.maximize_window()
#get()
browser.get('https://google.com')
#refresh
browser.refresh()
browser.get('https://www.saucedemo.com/')
time.sleep(2)
#back
browser.back()
time.sleep(2)
#Forward
browser.forward()
time.sleep(2)
#---- New window
# browser.switch_to.new_window("tab")
# time.sleep(2)
# closer
# browser.close()
# time.sleep(2)
# quit
browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
time.sleep(2)
browser.quit()