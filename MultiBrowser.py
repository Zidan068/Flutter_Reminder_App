from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\shiha\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe")
driver.get("http://127.0.0.1")
time.sleep(5)
driver.close()