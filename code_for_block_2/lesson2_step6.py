from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = int(x_element.text)
answer = math.log(abs(12 * math.sin(x)))

answer_input = browser.find_element_by_id("answer")
answer_input.send_keys(str(answer))

checkbox_robot = browser.find_element_by_id("robotCheckbox")
checkbox_robot.click()

radio_robot = browser.find_element_by_id("robotsRule")
browser.execute_script("arguments[0].scrollIntoView(true);", radio_robot)
radio_robot.click()

submit_btn = browser.find_element_by_xpath('//button[text()="Отправить"]')
browser.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
submit_btn.click()
