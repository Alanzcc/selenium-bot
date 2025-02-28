# This bot was created following https://www.lambdatest.com/learning-hub/install-selenium-python tutorial for python selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://lambdatest.github.io/sample-todo-app/")
driver.set_window_size(1366, 768)
driver.find_element(By.NAME, "li1").click()
driver.find_element(By.NAME, "li4").click()
driver.find_element(By.ID, "sampletodotext").click()
driver.find_element(By.ID, "sampletodotext").send_keys("Drink water")
driver.find_element(By.ID, "addbutton").click()
driver.find_element(By.ID, "sampletodotext").click()
driver.find_element(By.ID, "sampletodotext").send_keys("Study programming")
driver.find_element(By.ID, "addbutton").click()
driver.find_element(By.ID, "sampletodotext").click()
driver.find_element(By.ID, "sampletodotext").send_keys("Workout")
driver.find_element(By.ID, "addbutton").click()
driver.find_element(By.ID, "sampletodotext").click()
driver.find_element(By.ID, "sampletodotext").send_keys("meeting with robert")
driver.find_element(By.ID, "addbutton").click()
element = driver.find_element(By.ID, "addbutton")
driver.find_element(By.NAME, "li6").click()
driver.find_element(By.NAME, "li7").click()
driver.find_element(By.NAME, "li2").click()
driver.find_element(By.NAME, "li3").click()
driver.find_element(By.NAME, "li5").click()
driver.find_element(By.NAME, "li9").click()
driver.find_element(By.NAME, "li8").click()
driver.quit()
