from selenium import webdriver

driver=webdriver.Firefox()
driver.get("file:///C:/Users/ADMIN/PycharmProjects/7_Class_16_2_2018/HTML/Table.html")
driver.maximize_window()
driver.implicitly_wait(30)

ele=driver.find_elements_by_xpath("//*[@id='Employe']/thead/tr/th")
print(len(ele))
#first_part="//[@id='Employe']/thead/tr/th["
#econd_part="]"