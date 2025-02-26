from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) 

 

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 25).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) 
    button1 = browser.find_element(By.ID, "book")
    button1.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input2 = browser.find_element(By.XPATH, '//input[@id="answer"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
    input2.send_keys(y)


    button2 = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)   
    button2.click()

    print(browser.switch_to.alert.text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла