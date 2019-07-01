from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer_input = browser.find_element_by_id("answer")
answer_input.send_keys(y)

checkbox_robot = browser.find_element_by_id("robotCheckbox")
checkbox_robot.click()

radio_robot = browser.find_element_by_id("robotsRule")
radio_robot.click()

submit_btn = browser.find_element_by_xpath('//button[text()="Отправить"]')
submit_btn.click()
