from selenium import webdriver
import math
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

open_btn = browser.find_element_by_xpath('//button[text()="Хочу отправиться в волшебное путешествие"]')
open_btn.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_id("input_value")
x = int(x_element.text)
answer = math.log(abs(12 * math.sin(x)))

answer_input = browser.find_element_by_id("answer")
answer_input.send_keys(str(answer))

submit_btn = browser.find_element_by_xpath('//button[text()="Отправить"]')
submit_btn.click()