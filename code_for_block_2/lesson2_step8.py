from selenium import webdriver
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

name_input = browser.find_element_by_name("firstname")
sirname_input = browser.find_element_by_name("lastname")
mail_input = browser.find_element_by_name("email")

name_input.send_keys("Name")
sirname_input.send_keys("Sirname")
mail_input.send_keys("mail@mail.com")

file_input = browser.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла
file_input.send_keys(file_path)

submit_btn = browser.find_element_by_xpath('//button[text()="Отправить"]')
submit_btn.click()