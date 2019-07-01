from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1_element = browser.find_element_by_id("num1")
num2_element = browser.find_element_by_id("num2")
num1 = int(num1_element.text)
num2 = int(num2_element.text)
answer = num1 + num2

select_ans = Select(browser.find_element_by_id("dropdown"))
select_ans.select_by_value(str(answer))

submit_btn = browser.find_element_by_xpath('//button[text()="Отправить"]')
submit_btn.click()
