from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os

# pip install selenium
# pip install webdriver_manager

def setup_class(cls):
    cls.driver = webdriver.Chrome(ChromeDriverManager().install())
    
filename =   os.path.join(os.path.dirname('__file__'),'target_1.png')
serch_value= str(input("search value:"))
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.save_screenshot(filename)

print(driver.title)
form = driver.find_element(By.ID, "APjFqb")
print(form)
form.send_keys(serch_value)
form.send_keys(Keys.ENTER)



