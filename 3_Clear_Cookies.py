from selenium import webdriver

browser=webdriver.Chrome()
browser.get("http://phptravels.com")
browser.maximize_window()
browser.implicitly_wait(30)
browser.delete_all_cookies()
browser.quit()