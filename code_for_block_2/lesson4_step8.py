from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(chrome_options=opt)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена не будет равна 10000
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000"))

# нажатие на кнопку бронирования
button = browser.find_element_by_id("book")
button.click()

# математическая капча
x_element = browser.find_element_by_id("input_value")
x = int(x_element.text)
answer = math.log(abs(12 * math.sin(x)))

answer_input = browser.find_element_by_id("answer")
answer_input.send_keys(str(answer))

submit_btn = browser.find_element_by_xpath('//button[text()="Отправить"]')
submit_btn.click()
