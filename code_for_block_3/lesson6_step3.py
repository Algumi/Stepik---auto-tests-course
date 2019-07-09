import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


answer = math.log(int(time.time()))

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', False)
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)


class TestParamert(object):
    @pytest.mark.parametrize('link', links)
    def test_guest_should_see_login_link(self, browser: webdriver, wait: WebDriverWait, link):
        browser.get(link)
        input = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))

        answer = math.log(int(time.time()))
        input.send_keys(str(answer))

        submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
        submit_btn.click()

        wait.until(EC.element_to_be_clickable((By.XPATH, './/button[text()="Решить снова"]')))
        black_line = browser.find_element_by_class_name("smart-hints__feedback")
        if black_line.text != "Correct!":
            with open("answer_6_3.txt", "a") as f:
                f.write(black_line.text)
        assert black_line.text == "Correct!", 'Text in optional feedback is not "Correct!"'

    def test_print_result(self):
        with open("answer_6_3.txt") as f:
            print(f.read())