from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) 

 

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")   
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input2 = browser.find_element(By.XPATH, '//input[@id="answer"]')
    input2.send_keys(y)


    button = browser.find_element(By.TAG_NAME, "button")   
    button.click()

    print(browser.switch_to.alert.text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла